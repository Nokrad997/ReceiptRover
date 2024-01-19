import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

from src.exceptions.Exceptions import ErrorReadingXmlException, ErrorSavingXmlException,ErrorValueParsingException
from src.repositories.ProductOfflineRepository import ProductOfflineRepository
from src.repositories.ReceiptOfflineRepository  import ReceiptOfflineRepository

class DataController():
    
    def __init__(self,path):
        self.path = path
        self.ProductR = ProductOfflineRepository()
        self.ReceiptR = ReceiptOfflineRepository()
        try:
            if os.path.exists(path):
                try:
                    tree = ET.parse(path)
                    self.root = tree.getroot()
                except ET.ParseError as e:
                    raise ErrorReadingXmlException(f"Problem z odczytaniem(parsowaniem) danych: \n{e}")
            else:
                self.root = ET.Element("root")
                tree = ET.ElementTree(self.root)
                
                self._save_tree(tree)
                
        except ErrorReadingXmlException as e:
            raise e
        except ErrorSavingXmlException as e:
            raise e
        except Exception as e:
            raise e

    def _save_tree(self, tree):
        try:
            tree.write(self.path)
        except Exception as e:
            raise ErrorSavingXmlException(f"Nie można zapisać danych do pliku: \n{e}")


    def save_receipe(self, receipe_element):
        try:
            if os.path.exists(self.path):
                try:
                    tree = ET.parse(self.path)
                    self.root = tree.getroot()
                except ET.ParseError as e:
                    raise ErrorReadingXmlException(f"Problem z odczytaniem(parsowaniem) danych: \n{e}")

                receipes_element = self.root.find("Receipes")
                if receipes_element is None:
                    receipes_element = ET.Element("Receipes")
                    self.root.append(receipes_element)
                
                receipes_element.append(receipe_element)
                
                self._save_tree(tree)

            else:
                self.root = ET.Element("root")
                receipes_element = ET.Element("Receipes")
                self.root.append(receipes_element)
                self.root.append(receipe_element)

                tree = ET.ElementTree(self.root)
                
                self._save_tree(tree)
                
        except ErrorSavingXmlException as e:
            raise e
        except ErrorReadingXmlException as e:
            raise e
        except Exception as e:
            raise e
        
    def downland(self):
        receipts=[]
        try:
            for receipt in self.root.findall(".//Receipes/Receipe"):
                
                try:
                    key = receipt.find("key").text
                    shop = receipt.find("shop").text
                except ValueError as e:
                    raise ErrorValueParsingException(f"Blad podczas parsowania danych i zapisywania do modeli paragonu \n{e}")
                
                products = []
                for product_element in receipt.findall("Product"):
                    product = self.product_parser(product_element)
                    products.append(product)
                
                instance = self.ReceiptR.createReceipt(key, shop, products)
                
                receipts.append(instance)
                
        except ErrorValueParsingException as e:
            raise e
        except Exception as e:
            raise e
        
        return receipts
            
        
    def product_parser(self, product):
        try:
            name = product.find("name").text
            price = float(product.find("price").text)
            quantity = float(product.find("quantity").text)
            return self.ProductR.createProduct(name, price, quantity)
        except ValueError as e:
            raise ErrorValueParsingException(f"Blad podczas parsowania danych i zapisywania do modeli produktu \n{e}")
        

    def save(self,receipts):
        for receipt in receipts:
            receipt_element = ET.Element("Receipe")
            ET.SubElement(receipt_element, "key").text = str(receipt.key)
            ET.SubElement(receipt_element, "shop").text = str(receipt.shop)
            
            products=receipt.products
            if products is not None:
                for product in products:
                    product_element = self.save_products(product)
                    receipt_element.append(product_element)
                    
            

            self.save_receipe(receipt_element)
        
        
    def save_products(self, product):
        product_element = ET.Element("Product")
        ET.SubElement(product_element, "name").text = str(product.name)
        ET.SubElement(product_element, "price").text = str(product.price)
        ET.SubElement(product_element, "quantity").text = str(product.quantity)
        return product_element


