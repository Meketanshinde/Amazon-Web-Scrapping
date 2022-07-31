# from bs4 import BeautifulSoup
# import requests


# url = 'https://www.amazon.in/First-Coffee-Then-Data-Dishwasher/dp/B095HXJQG3/ref=sr_1_2?crid=39M5ULGV8G7GO&keywords=data+analyst+cup&qid=1659025232&sprefix=data+analyst+cup%2Caps%2C318&sr=8-2'

# headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71"}

# page = requests.get(url,headers= headers)

# soup = BeautifulSoup(page.content,"lxml")

# soup1 = BeautifulSoup(soup.prettify(), "lxml")

# title = soup1.find(id = "productTitle").get_text()

# Brand = soup1.find(id="bylineInfo").get_text()

# price = soup1.find("a-price-whole")

# Brand=Brand.strip()
# title=title.strip()

# print(title)
# print(Brand)

# import datetime

# today=datetime.date.today()
# print(today)

# import csv

# header= ['Title', 'Brand', 'Date']
# data = [title, Brand, today]

# with open('AmazonDataSet.csv','w',newline='',encoding='UTF8') as f:
#     writer=csv.writer(f)
#     writer.writerow(header)
#     writer.writerow(data)

# import pandas 
# pd = pandas.read_csv(r'C:\Users\29ske\Desktop\Web Scrapping\AmazonDataSet.csv')
# print(pd)

