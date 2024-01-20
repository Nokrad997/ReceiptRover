# __init__.py 
from src.repositories.ProductOfflineRepository import ProductOfflineRepository
from src.repositories.ReceiptOfflineRepository import ReceiptOfflineRepository 
from src.controllers.DataController import DataController


ProductR = ProductOfflineRepository()
ReceiptR = ReceiptOfflineRepository()

p1=ProductR.createProduct("n1",1,1)
p2=ProductR.createProduct("n2",2,2)
p3=ProductR.createProduct("n3",3,3)
p4=ProductR.createProduct("n4",4,4)

r1=ReceiptR.createReceipt("k1", "s1", [p1,p2])
r2=ReceiptR.createReceipt("k2", "s2", [p3,p4])


data=DataController("r.xml")
try:
    # data.save([r1,r1])
    list=data.downland()
    for r in list:
        print(r.shop,":")
        for p in r.products:
            print(' ',p.name)
except Exception as e:
    print(e)
