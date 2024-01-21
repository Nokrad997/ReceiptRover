from pydantic import BaseModel, root_validator
from image import Image
import pytesseract
import re

class Ocr(BaseModel):
    """
    Class for performing OCR (Optical Character Recognition) on an image.
    """

    class Config():
        arbitrary_types_allowed = True
        
    file : str 
    text: str = ''
    shop: str = ''
    products: list[str] = []
    ammount: float = 0.0
    img: Image = None
    

    @root_validator(pre=True)
    def create_image(cls, values):
        """
        Root validator to create an Image object from the provided file path.
        """
        file_path = values.get('file')
        if file_path:
            values['img'] = Image(file_path)
        return values
        
    def getText(self):
        """
        Extracts text from the image using pytesseract library.
        """
        try:
            self.text = pytesseract.image_to_string(self.img.getImage(), lang='pol')
            self.text = self.text.replace(',', '.')
            self.text = self.text.replace(' I ', '1')
        except Exception as e:
            self.text = f'Error occurred while extracting text: {e}'
       
    def extractProducts(self):
        """
        Extracts products from the extracted text using regular expressions.
        """
        try:
            product_pattern = re.compile(r"(?P<item>.*\w+.)(?P<ilosc> \d.*x|X)(?P<cena>\d+\.\d+)")
            products = product_pattern.findall(self.text)

            for element, i in zip(products, range(len(products))):
                products[i] = list(element)
                products[i][1] = products[i][1].replace('x', '')
                products[i][1] = products[i][1].replace('X', '')
                products[i][1] = products[i][1].replace(' ', '')
                products[i][1] = products[i][1].replace(' x', '')
                products[i][1] = products[i][1].replace('0-', '')
                products[i][2] = products[i][2].replace(' ', '')
                item_pattern = r"\d+$"
                products[i][0] = re.sub(item_pattern, '', products[i][0])
            self.products = products
        except Exception as e:
            print(f"Error occurred while extracting products: {e}")
            self.products = []
            
     
    def getProducts(self):
        """
        Returns the extracted products.
        """
        return self.products
    
    def extractShop(self):
        """
        Extracts the shop name from the extracted text using regular expressions.
        """
        try:
            shop_pattern = self.text.splitlines()[2]
            self.shop = str(shop_pattern)
        except Exception as e:
            self.shop = f'Error occurred while extracting shop: {e}'

    def getShop(self):
        """
        Returns the extracted shop name.
        """
        return self.shop

    def getAmmount(self):
        """
        Calculates the total amount based on the extracted products.
        """
        for product in self.products:
            self.ammount += float(product[1]) * float(product[2])
        return self.ammount
    
