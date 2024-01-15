from flask import Flask, request, jsonify
from ocr import Ocr
import random
import string
import os


app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    """
    Performs Optical Character Recognition (OCR) on an image file.

    Returns:
        A JSON response containing the extracted shop and products information.
    """
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    random_string += '.jpg'
    file.save(random_string)
    ocr = Ocr(file=random_string)
    ocr.getText()
    ocr.extractProducts()
    ocr.extractShop()
    resoult = jsonify({
        'shop': ocr.getShop(),
        'products': ocr.getProducts()
    })
    os.remove(random_string)
    return resoult


if __name__ == '__main__':
    app.run(debug=True)
    