from src.repositories.ProductOfflineRepository import ProductOfflineRepository
from src.repositories.ReceiptOfflineRepository import ReceiptOfflineRepository 
from src.controllers.DataAnalysisController import DataAnalysisController


ProductR = ProductOfflineRepository()
ReceiptR = ReceiptOfflineRepository()

p1=ProductR.createProduct("p1",23.00,1)
p2=ProductR.createProduct("p2",2.00,2)
p3=ProductR.createProduct("p3",3.00,3)
p4=ProductR.createProduct("p4",8.00,4)

r1=ReceiptR.createReceipt("s1", [p1,p2])
r2=ReceiptR.createReceipt( "s2", [p3,p4])
r3=ReceiptR.createReceipt( "s3", [p3,p4,p1])
r4=ReceiptR.createReceipt( "s4", [p2,p2,p1])


print(type(r1))
print(r1.key)
print(r2.key)
d=DataAnalysisController()
d.clearCharts()
print(d.getShopStatement([r1,r2,r3,r4]))

