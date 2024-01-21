import numpy as np
import cv2
from skimage.filters import threshold_local
from PIL import Image
import os


class TransformImage:
    def __init__(self, input_data):
        if isinstance(input_data, str):
            self.original = Image.open(input_data)
            self.imgorg = cv2.imread(input_data)
        elif isinstance(input_data, np.ndarray):
            self.original = Image.fromarray(cv2.cvtColor(input_data, cv2.COLOR_BGR2RGB))
            self.imgorg = input_data
        else:
            raise ValueError("Input must be a file path or an image array")
        self.width_ratio = None
        self.height_ratio = None
        self.img = None
        self.gray = None
        self.edged = None
        self.contour = None
        self.aprox = None
        self.scanned = None
        self.bw_scanned = None
        self.manual_contour_points = []

    def resizeImage(self, base_width=500, base_height=500):
        """Resize the image maintaining aspect ratio."""
        self.width_ratio = base_width / self.original.size[0]
        self.height_ratio = base_height / self.original.size[1]
        dim = (
            int(self.original.size[0] * self.width_ratio),
            int(self.original.size[1] * self.height_ratio),
        )
        self.img = cv2.resize(self.imgorg, dim, interpolation=cv2.INTER_AREA)
        return self.img

    def toGray(self):
        """Convert the image to grayscale."""
        if self.img is None:
            self.resizeImage()
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        return self.gray

    def blurGray(self, blur_size=(5, 5)):
        """Apply Gaussian blur to the grayscale image."""
        if self.gray is None:
            self.to_gray()
        self.gray = cv2.GaussianBlur(self.gray, blur_size, 0)
        return self.gray

    def _clickAndMark(self, event, x, y, flags, param):
        """Callback function for mouse events during manual contour selection."""
        if event == cv2.EVENT_LBUTTONDOWN:
            self.manual_contour_points.append((x, y))
            cv2.circle(self.img, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow("Image", self.img)
            if len(self.manual_contour_points) == 4:
                cv2.line(
                    self.img,
                    self.manual_contour_points[0],
                    self.manual_contour_points[1],
                    (0, 255, 0),
                    2,
                )
                cv2.line(
                    self.img,
                    self.manual_contour_points[1],
                    self.manual_contour_points[2],
                    (0, 255, 0),
                    2,
                )
                cv2.line(
                    self.img,
                    self.manual_contour_points[2],
                    self.manual_contour_points[3],
                    (0, 255, 0),
                    2,
                )
                cv2.line(
                    self.img,
                    self.manual_contour_points[3],
                    self.manual_contour_points[0],
                    (0, 255, 0),
                    2,
                )
                cv2.imshow("Image", self.img)
                return

    def manualContourSelection(self):
        """Open a window for the user to manually select the contour of the receipt."""
        cv2.namedWindow("Image")
        cv2.setMouseCallback("Image", self._clickAndMark)
        self.img = self.resizeImage()
        cv2.imshow("Image", self.img)
        cv2.waitKey(0)
        cv2.destroyWindow("Image")
        if len(self.manual_contour_points) == 4:
            self.contour = np.array(self.manual_contour_points, dtype=np.float32)
        else:
            print("Please select exactly four points.")
            self.contour = None
        return self.contour

    def detectEdges(self, threshold1=50, threshold2=150, debug=False):
        """Detect edges in the image using Canny edge detection."""
        if self.gray is None:
            self.to_gray()
        self.edged = cv2.Canny(self.gray, threshold1, threshold2)
        if debug:
            cv2.imwrite("debug_edges.jpg", self.edged)
        return self.edged

    def findContours(self, debug=False):
        """Find contours in the image."""
        if debug and self.contour is not None:
            print("Using cached contour")
            debug_img = self.img.copy()
            cv2.drawContours(debug_img, [self.contour], -1, (0, 255, 0), 3)
            cv2.imwrite("debug_contours.jpg", debug_img)
            return self.contour
        if self.edged is None:
            self.detect_edges()
        contours, _ = cv2.findContours(
            self.edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
        )
        if contours:
            largest = max(contours, key=cv2.contourArea)
            self.contour = self._approximateContour(largest)
        else:
            self.contour = None
        return self.contour

    def _approximateContour(self, contour):
        """Approximate contour shape to a polygon."""
        peri = cv2.arcLength(contour, True)
        return cv2.approxPolyDP(contour, 0.02 * peri, True)

    def correctPerspective(self):
        """Correct the perspective of the image based on the largest contour."""
        if self.contour is None or len(self.contour) != 4:
            raise InterruptedError(
                "Contour not found or invalid for perspective correction"
            )
        self.img = cv2.cvtColor(self.imgorg.copy(), cv2.COLOR_BGR2RGB)
        rect = self._contourToRect()
        self.scanned = self._wrapPerspective(self.img, rect)
        return self.scanned

    def _contourToRect(self):
        """Convert contour to rectangle coordinates considering both width and height ratios."""
        if self.contour is None:
            raise ValueError("No contour available to convert to rectangle.")
        if len(self.contour) != 4:
            raise ValueError(
                "Contour does not have 4 points and cannot be converted to a rectangle."
            )
        pts = self.contour.reshape(4, 2).astype(np.float32)
        scaled_pts = np.zeros((4, 2), dtype="float32")
        for i in range(4):
            scaled_pts[i][0] = pts[i][0] / self.width_ratio
            scaled_pts[i][1] = pts[i][1] / self.height_ratio
        rect = np.zeros((4, 2), dtype="float32")
        sum_pts = scaled_pts.sum(axis=1)
        rect[0] = scaled_pts[np.argmin(sum_pts)]
        rect[2] = scaled_pts[np.argmax(sum_pts)]
        diff_pts = np.diff(scaled_pts, axis=1)
        rect[1] = scaled_pts[np.argmin(diff_pts)]
        rect[3] = scaled_pts[np.argmax(diff_pts)]
        return rect

    def _wrapPerspective(self, image, rect):
        """Apply a perspective transformation to the image."""
        (tl, tr, br, bl) = rect
        widthA = np.linalg.norm(br - bl)
        widthB = np.linalg.norm(tr - tl)
        heightA = np.linalg.norm(tr - br)
        heightB = np.linalg.norm(tl - bl)
        maxWidth = max(int(widthA), int(widthB))
        maxHeight = max(int(heightA), int(heightB))
        dst = np.array(
            [
                [0, 0],
                [maxWidth - 1, 0],
                [maxWidth - 1, maxHeight - 1],
                [0, maxHeight - 1],
            ],
            dtype="float32",
        )
        M = cv2.getPerspectiveTransform(rect, dst)
        return cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    def toBlackAndWhite(self, block_size=21, offset=10):
        """Convert the scanned image to black and white."""
        if self.scanned is None:
            raise ValueError(
                "Scanned image not available for black and white conversion"
            )
        gray_scanned = cv2.cvtColor(self.scanned, cv2.COLOR_BGR2GRAY)
        T = threshold_local(gray_scanned, block_size, offset=offset, method="gaussian")
        self.bw_scanned = (gray_scanned > T).astype("uint8") * 255
        return self.bw_scanned

    def saveImage(self, file_path):
        """Save the final processed image to a file."""
        if not os.path.exists(file_path):
            os.makedirs('scanned')
        if self.bw_scanned is None:
            raise ValueError("No black and white scanned image to save")
        cv2.imwrite(file_path, self.bw_scanned)
        return file_path
