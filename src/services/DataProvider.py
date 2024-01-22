import xml.etree.ElementTree as ET
import os
from xml.dom import minidom
from typing import List  
from src.modelsOffline.Product import Product
from src.modelsOffline.Receipt import Receipt

class DataProvider:
    def __init__(self):
        self.filePath: str = "src/localData/Receipts.xml"
    
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

    def addReceiptToXmlFile(self, receipt: Receipt):
        if os.path.exists(self.filePath):
            tree = ET.parse(self.filePath)
            root = tree.getroot()
        else:
            root = ET.Element("Receipts")
            tree = ET.ElementTree(root)

        root.append(self.receiptToXmlElement(receipt))

        xmlstr = ET.tostring(root, encoding="utf-8")
        parsed_xml = minidom.parseString(xmlstr)

        xml_lines = [line for line in parsed_xml.toprettyxml(indent="    ").split('\n') if line.strip()]
        formatted_xml = '\n'.join(xml_lines)

        with open(self.filePath, "w", encoding="utf-8") as xmlfile:
            xmlfile.write(formatted_xml)

    def loadReceiptsFromXmlFile(self) -> List[Receipt]:
        tree = ET.parse(self.filePath)
        root = tree.getroot()

        return [self.xmlElementToReceipt(receiptElement) for receiptElement in root.findall("Receipt")]

    def getkeysFromXML(self) -> List[str]:
        tree = ET.parse(self.filePath)
        root = tree.getroot()

        return [receiptElement.find("Key").text for receiptElement in root.findall("Receipt")]
    
    def getkeyFromXMLByKey(self, key: str) -> str:
        tree = ET.parse(self.file_path)
        root = tree.getroot()

        for reciptElement in root.findall("Receipt"):
            if reciptElement.find("Key").text == key:
                return key

        return None
    
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