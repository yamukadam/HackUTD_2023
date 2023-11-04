from bs4 import BeautifulSoup
import requests
url = input('Enter an url: ')
page = requests.get(url)
article = BeautifulSoup(page.text, 'html.parser')
article = article.find_all('p')
text = []
file = open("article.txt", "w")
for x in article:
    if ('\n') not in x.text: 
      text.append(x.text)
for x in text:
   file.write(x)
   file.write('\n')