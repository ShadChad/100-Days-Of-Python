import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []



for i in range(2,10):
    url = "https://www.flipkart.com/search?q=mobile+phones&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_2_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+phones&requestId=16570dd5-8146-420b-994b-295e52aa9f9c&page=1"

    r = requests.get(url)

    soup = BeautifulSoup(r.text,'lxml')

    box = soup.find('div',class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div",class_='_4rR01T')
    # print(names)

    for i in names:
        name = i.text
        Product_name.append(name)
    # print(Product_name)

    prices = box.find_all('div',class_ = "_30jeq3 _1_WHN1")

    for i in prices:
        price = i.text
        Prices.append(price)
    # print(Prices)

    desc = box.find_all('div',class_ = "fMghEO")

    for i in desc:
        des = i.text
        Description.append(des)

    # print(Description)

    review = box.find_all('div',class_='_3LWZlK')

    for i in review:
        rev = i.text
        Reviews.append(rev)

    # print(len(Product_name))
    # print(len(Description))
    # print(len(Prices))
    # print(len(Reviews))
    # print(Reviews)


df = pd.DataFrame({"Product Name": Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
# print(df)

df.to_csv("flipkart_mobile_scrap.csv")




    # print(soup)
    # while True:
# np = box.find('a',class_='_1LKTO3').get('href')
#         # print(np)

# cnp = "https://www.flipkart.com" + np
# print(cnp)

    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text,'lxml')


