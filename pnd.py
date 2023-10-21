import pandas as pd 
data=pd.read_csv("D:\Sales_Data\cmd.csv")

print(data.head(100))
print(data.dropna(inplace=True))
data["Month"]=data['Order Date'].str[0:2]

print(data.head())
data["Quantity Ordered"]=pd.to_numeric(data["Quantity Ordered"])
data['Price Each']=pd.to_numeric(data['Price Each'])
data["sales"]=(data["Quantity Ordered"].int)*(data['Price Each'])
print(data.head())


