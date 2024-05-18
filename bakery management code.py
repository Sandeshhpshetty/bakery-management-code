import pandas as pd
class Bet:
    def __init__(self):
        self.order=[]
        self.quantity=[]

        print("welcome to python baker database")
        self.custid=input("enter the cust id: ")
        
    
    def place(self):
        
        self.od=input("enter the order required: ")
        self.quant=input("enter the order quantity required: ")

        
        self.order.append(self.od)
        self.quantity.append(self.quant)
    

data=Bet()
n=int(input("enter the total orders: "))
for i in range(n):
    data.place()

df=pd.DataFrame({
    "order" : data.order ,
    "quantity" : data.quantity
})
print(df)

c=input("enter the custid: ")
if c in data.custid:
    print(data.order,data.quantity)
