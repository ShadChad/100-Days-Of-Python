import requests
from bs4 import BeautifulSoup
import json
# query = input("what kinda news are you intrested in?")
# url = f"https://newsapi.org/v2/everything?q={query}&from=2023-03-01&to=2023-03-01&sortBy=popularity&apiKey=6c602f9c857347e2920abb75cd0b44ca"



# response = requests.get(url)
# # print(response.text)


# news= json.loads(response.text)
# # print(news,type(news))

# for article in news["articles"]:
#     print(article["title"])
#     print(article["description"])
#     print("-------------------------------")


# # soup = BeautifulSoup(response.text,"html.parser")

# # print(soup.prettify())


# # for title in soup.find_all('h2'):
# #     print(title.text)


query = "Apple"
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-03-01&to=2023-03-03&sortBy=popularity&apiKey=6c602f9c857347e2920abb75cd0b44ca"


r = requests.get(url)
# print(r) #response[200],[300] is used for redirecting

# print(r.content) #unreadable

data = json.loads(r.content)
# print(data['articles'][0])
key = input("Keys:\n1.Title\n2.Description\n3.Author\n")
if key=="1":
    for i in range(1,10):
        print(f"{i}.{data['articles'][i]['title']}\n")


titlenum = int(input("Press the specific key(1-10) for description\n"))
print("\n\n\n",data['articles'][titlenum]["description"]) 

content = input("press c for full content")
if content == "c":
    print(data['articles'][titlenum]['content'])

        










