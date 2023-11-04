from bs4 import BeautifulSoup
import requests

url = 'https://www.aramco.com/en/news-media/news/2023/aramco-announces-full-year-2022-results'
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')  # You can use 'html.parser' as well
sentence = []
#paragraphs = soup.select_one('container sublayout sublayout__body-content').text
paragraphs = soup.find_all('li')
for para in paragraphs:
    if ("$" or "%") in para.text:
        sentence.append(para.text)
file = open("article.txt", "w")
for x in sentence:
   file.write(x)
   file.write('\n')