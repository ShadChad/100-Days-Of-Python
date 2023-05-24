from bs4 import BeautifulSoup
import requests


with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

# print(soup.prettify())

# match = soup.title
match = soup.title.text 
# match1 = soup.div
match1 = soup.div.text #returs first div tag with all of its child tag

# match2 = soup.find('div') #returs same
match2 = soup.find('div',class_='footer') #returs footer div, class is a
# special keyword in python, reason why there is a underscore

article = soup.find('div',class_='article') #does same work

headline = article.h2.a.text #goes inside articl and gets h2 anker tag in text

summary = article.p.text  #kinda does same, but gets the paragragh in text


#----- Note ----- Find methods gets the first tag that matches

for article in soup.find_all('div',class_='article'):
    headline = article.h2.a.text

    print(headline)


    summary = article.p.text
    print(summary)

    print()

#finds all and returns all

# print(match)
# print(match1)
# print(match2)
# print(article)
# print(headline)
# print(summary)

