import matplotlib.pyplot as plt
from datetime import datetime
import os
from collections import defaultdict


class DataAnalysisService:
    def __init__(self):
        self.path = "img/charts/"

    def getSelecteReceipts(self, receipts, year, month):
        selected_receipts = []
        for receipt in receipts:
            receipt_year_month = receipt.key[:6]
            if receipt_year_month == f"{year:04d}{month:02d}":
                selected_receipts.append(receipt)

        return selected_receipts

    def getMounthlyStatement(self, receipts, year, month):
        selectedReceipts = self.getSelecteReceipts(receipts, year, month)

        for receipt in selectedReceipts:
            print(receipt.key)
        # jescze nie wiem co tu dać

        return self.path

    def getShopStatement(self, receipts, year, month) -> str:
        selectedReceipts = self.getSelecteReceipts(receipts, year, month)
        data = {}
        for receipt in selectedReceipts:
            shopName = receipt.shop
            total_cost = sum(
                product.price * product.quantity for product in receipt.products
            )
            if shopName not in data:
                data[shopName] = total_cost
            else:
                data[shopName] += total_cost

        # fig, ax = plt.subplots(facecolor="lightgray")

        # od danej ceny
        data = {key: value for key, value in data.items() if value > 10}

        # top 5
        # sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        # data = dict(list(sorted_data.items())[:5])

        shops = list(data.keys())
        costs = list(data.values())

        plt.figure(figsize=(4, 4))

        plt.bar(
            shops,
            costs,
            color="darkblue",
            width=0.5,
            edgecolor="black",
            linewidth=3,
            alpha=0.5,
        )

        plt.title(
            "Suma wydatków w poszczególnych sklepach",
            fontdict={"fontsize": 9, "fontweight": "bold"},
        )
        plt.xlabel("Sklepy", fontdict={"fontsize": 7})
        plt.ylabel("Suma wydatków(PLN)", fontdict={"fontsize": 7})

        now = datetime.now()
        date_time = now.strftime("%m%d%Y%H%M%S%f")
        path = self.path + date_time + ".jpg"  

        plt.savefig(path, dpi=75)
        # plt.show()
        plt.close()

        return path

    def clearCharts(self) -> None:
        for file in os.listdir(self.path):
            os.remove(self.path + file)
