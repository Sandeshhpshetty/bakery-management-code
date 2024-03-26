import pandas as pd
class Bet:
    def __init__(self,name,custid,order):
        self.name=name
        self.custid=custid
        self.order=order
    
    def place(self):
        print("welcome to python database")

while True:
    name=[input("enter the name")]
    custid=[int(input("enter the custid in number"))]
    order=[input("Enter the order they required")]
    a=int(input("enter 1 to continue"))
    break
    
if a==1:
    df=pd.DataFrame()
    df["names"]=name
    df["custid"]=custid
    df["order"]=order
    df
    df.to_csv("C:\\Users\\sande\\OneDrive\\Desktop\\applebox project\\bakery management code.csv")
    
else:
    print("ok")
    d=int(input("enter 1 to custdata using custid"))

if d==1:
    c=int(input("enter the custid"))
    if c in custid:
        print("custid=",name,order)
    else:
        print("no data found")
else:
    print("Thank you")

