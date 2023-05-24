import requests

# response = requests.get("https://www.codewithharry.com")
# print(response.text)


url = "https://jsonplaceholder.typicode.com/posts"

data =  {
    "title":"harry",
    "body" : "bhai",
    "userid" : 12,


}

headers = {
    'Content-type' : 'application/json;charset=UTF-8',

}


response = requests.post(url,headers=headers,json=data)

print(response.text)
# returns
# {
#   "title": "harry",
#   "body": "bhai",
#   "userid": 12,
#   "id": 101
# }
# 


 
from bs4 import BeautifulSoup
url1 = ("https://www.codewithharry.com/blogpost/django-cheatsheet/")

r1= requests.get(url1)


soup1 = BeautifulSoup(r1.text,"html.parser")

# print(soup1.prettify())
 
for heading in soup1.find_all("h2"):
    print(heading.text)
    # retunrs all h2 tags 

