import xml.etree.ElementTree as ET
import os
from xml.dom import minidom
from typing import List  
from src.modelsOffline.Product import Product
from src.modelsOffline.Receipt import Receipt

class DataProvider:
    def __init__(self):
        pass
    
    def receiptToXmlElement(self, receipt: Receipt) -> ET.Element:
        receiptElement = ET.Element("Receipt")
        ET.SubElement(receiptElement, "Key").text = receipt.key
        ET.SubElement(receiptElement, "Shop").text = receipt.shop

        productsElement = ET.SubElement(receiptElement, "Products")
        for product in receipt.products:
            productElement = ET.SubElement(productsElement, "Product")
            ET.SubElement(productElement, "Name").text = product.name
            ET.SubElement(productElement, "Price").text = str(product.price)
            ET.SubElement(productElement, "Quantity").text = str(product.quantity)

        return receiptElement

    def xmlElementToReceipt(self, xmlElement: ET.Element) -> Receipt:
        key = xmlElement.find("Key").text
        shop = xmlElement.find("Shop").text

        productsElement = xmlElement.find("Products")
        products = []
        for productElement in productsElement.findall("Product"):
            name = productElement.find("Name").text
            price = float(productElement.find("Price").text)
            quantity = float(productElement.find("Quantity").text)

            products.append(Product(name=name, price=price, quantity=quantity))

        return Receipt(key=key, shop=shop, products=products)

    def addReceiptToXmlFile(self, receipt: Receipt, filePath: str = "src/localData/Receipts.xml"):
        if os.path.exists(filePath):
            tree = ET.parse(filePath)
            root = tree.getroot()
        else:
            root = ET.Element("Receipts")
            tree = ET.ElementTree(root)

        root.append(self.receiptToXmlElement(receipt))

        xmlstr = ET.tostring(root, encoding="utf-8")
        parsed_xml = minidom.parseString(xmlstr)

        xml_lines = [line for line in parsed_xml.toprettyxml(indent="    ").split('\n') if line.strip()]
        formatted_xml = '\n'.join(xml_lines)

        with open(filePath, "w", encoding="utf-8") as xmlfile:
            xmlfile.write(formatted_xml)

    def loadReceiptsFromXmlFile(self, filePath: str) -> List[Receipt]:
        tree = ET.parse(filePath)
        root = tree.getroot()

        return [self.xmlElementToReceipt(receiptElement) for receiptElement in root.findall("Receipt")]
