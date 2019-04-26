from bs4 import BeautifulSoup
import requests
website = requests.get(https://baidu.com)
soup = BeautifulSoup(website.content, 'html.parser')
print(soup)