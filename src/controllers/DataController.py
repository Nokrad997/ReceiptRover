import xml.etree.ElementTree as ET
from xml.dom import minidom
from src.modelsOnline.Product import Product
from src.modelsOnline.Receipt import Receipt
from src.modelsOnline.Transaction import Transaction


# rozdzielić na kilka plików, nie może być 3 klas w jednym pliku


class DownloadData:
    def __init__(self):
        pass

    def download(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        return root


class Parser:
    def __init__(self, root):
        self.root = root
        pass

    def parse(self):
        transactions = []

        for transaction_element in self.root.findall(".//Transaction"):
            transactions_id = int(transaction_element.find("transactions_id").text)
            user_id = int(transaction_element.find("user_id").text)
            date = transaction_element.find("date").text
            scan_id = int(transaction_element.find("scan_id").text)
            key = transaction_element.find("key").text

            transaction = Transaction(transactions_id, user_id, date, scan_id, key)
            print("cc")
            receipt_element = transaction_element.find("Receipt")
            if receipt_element is not None:
                transaction.receipt = self.receipt_parser(receipt_element)

            transactions.append(transaction)

        return transactions

    def receipt_parser(self, receipt):
        receipt_id = int(receipt.find("receipt_id").text)
        key = receipt.find("key").text
        receipt_data = receipt.find("receipt").text.encode("utf-8")

        products = []
        for product_element in receipt.findall("Product"):
            product = self.product_parser(product_element)
            products.append(product)

        instance = Receipt(receipt_id, key, receipt_data)
        instance.products = products
        return instance

    def product_parser(self, product):
        product_id = int(product.find("product_id").text)
        name = product.find("name").text
        price = float(product.find("price").text)
        quantity = int(product.find("quantity").text)
        return Product(product_id, name, price, quantity)


class SaveData:
    def __init__(self):
        pass

    def save(self, path, transactions):
        transactions_element = ET.Element("Transactions")
        for transaction in transactions:
            transaction_element = ET.Element("Transaction")
            ET.SubElement(transaction_element, "transactions_id").text = str(
                transaction.transactions_id
            )
            ET.SubElement(transaction_element, "user_id").text = str(
                transaction.user_id
            )
            ET.SubElement(transaction_element, "date").text = str(transaction.date)
            ET.SubElement(transaction_element, "scan_id").text = str(
                transaction.scan_id
            )
            ET.SubElement(transaction_element, "key").text = str(transaction.key)

            if transaction.receipt is not None:
                receipt = transaction.receipt
                receipt_element = self.save_receipt(receipt)
                transaction_element.append(receipt_element)

            transactions_element.append(transaction_element)

        xml_str = ET.tostring(
            transactions_element, encoding="utf-8", method="xml"
        ).decode()
        xml_str = minidom.parseString(xml_str).toprettyxml(indent="    ")

        with open(path, "w", encoding="utf-8") as xml_file:
            xml_file.write(xml_str)

    def save_receipt(self, receipt):
        receipt_element = ET.Element("Receipt")
        ET.SubElement(receipt_element, "receipt_id").text = str(receipt.receipt_id)
        ET.SubElement(receipt_element, "key").text = str(receipt.key)
        ET.SubElement(receipt_element, "receipt").text = str(
            receipt.receipt, encoding="utf-8"
        )

        if receipt.products:
            for product in receipt.products:
                product_element = self.save_products(product)
                receipt_element.append(product_element)

        return receipt_element

    def save_products(self, product):
        product_element = ET.Element("Product")
        ET.SubElement(product_element, "product_id").text = str(product.product_id)
        ET.SubElement(product_element, "name").text = str(product.name)
        ET.SubElement(product_element, "price").text = str(product.price)
        ET.SubElement(product_element, "quantity").text = str(product.quantity)
        return product_element


# product1 = Product(1, "Product A", 10.99,1)
# product2 = Product(2, "Product B", 5.99,1)

# receipt1 = Receipt(1, "def456", b"example receipt data")
# receipt1.products = [product1, product2]

# receipt2 = Receipt(2, "ghi789", b"another receipt data")
# receipt2.products = [product2]

# transaction1 = Transaction(1, 123, "2024-01-11", 456, "abc123")
# transaction1.add_receipt(receipt1)

# transaction2 = Transaction(2, 456, "2024-01-12", 789, "xyz789")
# transaction2.add_receipt(receipt2)

# # Zapisywanie do pliku XML z ładnym formatowaniem
# transactions = [transaction1, transaction2]


# save = SaveData()
# save.save("transactions.xml", transactions)

# read=DownloadData()
# root=read.download("transactions.xml")
# parser=Parser(root)
# list=parser.parse()
# for t in list:
#     print(t.transactions_id)
#     for p in t.receipt.products:
#         print(p.product_id)
#         print(p.name)
#         print(p.price)
#         print(p.quantity)
