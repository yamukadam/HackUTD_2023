from article_scraper import scraper
import random as rand
def prompter():
    companies = ["Exxon", "Saudi Aramco", "Shell"]
    urls = ['https://www.reuters.com/business/energy/sarabia-other-opec-producers-announce-voluntary-oil-output-cuts-2023-04-02/','https://www.cnbc.com/2022/02/24/russian-forces-invade-ukraine.html','https://www.cnbc.com/2021/06/09/tc-energy-terminates-keystone-xl-pipeline-project.html']
    for company in companies:
        scraper(rand.choice(urls), company)
    for company in companies:
        prompt = None
        try:
            prompt = open(f"{company}prompt.txt", "x")
        except:
            prompt = open(f"{company}prompt.txt", "a")
        article = open(f'{company}.txt','r')
        artiline = ''
        for line in article:
            artiline += line
        prompt.write(f'Read the following article : "{artiline}", how do you think this will affect the {company} company?')
        prompt.close()
prompter()