import matplotlib.pyplot as plt
from datetime import datetime
import os
class DataAnalysisService:
    
    def __init__(self):
        self.path="img/charts/"
        
    
    def getMounthlyStatement(self,receipt):
        # troche nie wiem jak to brać skoro klucz sie generuje na podstawie daty kiedy wczytujemy dane
        # pózniej to sie ogarnie
        pass
    
    def getShopStatement(self,receipts) ->str:
            data = {}
            for receipt in receipts:
                shop_name = receipt.shop
                total_cost = sum(product.price * product.quantity for product in receipt.products)
                if shop_name not in data:
                    data[shop_name] = total_cost
                else:
                    data[shop_name] += total_cost

            fig, ax = plt.subplots(facecolor='lightgray')
            
            shops = list(data.keys())
            costs = list(data.values())

            plt.bar(shops, costs, color='darkblue',width=0.5, edgecolor='black', linewidth=3, alpha=0.5)
            
            plt.title('Suma wydatków w poszczególnych sklepach',fontdict={'fontsize': 14, 'fontweight': 'bold'})
            plt.xlabel('Sklepy',fontdict={'fontsize': 10})
            plt.ylabel('Suma wydatków(PLN)',fontdict={'fontsize': 10})
            
            now = datetime.now()
            date_time = now.strftime("%m%d%Y%H%M%S%f")
            path=self.path+date_time+'.jpg'
            
            plt.savefig(path)
            plt.show()
            
            return path
        
        
    def clearCharts(self) -> None:
        for file in os.listdir(self.path):
            os.remove(self.path+file)