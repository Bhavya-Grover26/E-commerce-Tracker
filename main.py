import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name=[]
Prices=[]
Description=[]
Reviews=[]

for i in range(2,12):
    url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r=requests.get(url)
    #print(r)

    soup = BeautifulSoup(r.text, "lxml")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    #print(soup.encode("utf-8"))

    names=box.find_all("div",class_="_4rR01T")

    for i in names:
        name= i.text
        Product_name.append(name)

    prices=box.find_all("div",class_="_30jeq3 _1_WHN1")

    for i in prices:
        price = i.text
        Prices.append(price)

    descriptions=box.find_all("ul",class_="_1xgFaf")

    for i in descriptions:
        description = i.text
        Description.append(description)



df= pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Description":Description})
print(df)





'''
np = soup.find("a", class_="_1LKTO3").get("href")
cnp = "https://www.flipkart.com"+np
print(cnp)
'''



