import requests
from bs4 import BeautifulSoup 

# get webpage
page = requests.get('http://quotes.toscrape.com/')
# get html of page
html = BeautifulSoup(page.content, 'html.parser')

#print status code and info
print("status code: " + str(page))
print("connected to: " + str(page.url))
    
# print important page info
print("Page Title: " + str(html.title.text))

#print quotes
quotes = html.find_all('div', class_='quote')
for quote in quotes:
    print(quote.find('span', class_='text').text)
