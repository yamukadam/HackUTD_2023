from bs4 import BeautifulSoup
import requests
def scraper(url, company, arttype = "article"):
  page = requests.get(url)
  article = BeautifulSoup(page.text, 'html.parser')
  if arttype == "article":
    article = article.find_all('p')
  elif arttype == "list":
    article = article.find_all('li')
  text = []
  file = None
  try:
    file = open(f"{company}.txt", "x")
  except:
    file = open(f"{company}.txt", "a")
  for x in article:
      if ('\n') not in x.text and len(x.text) > 100: 
        text.append(x.text)
  for x in text:
    file.write(x)
    file.write('\n')