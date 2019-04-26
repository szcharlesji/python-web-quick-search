from bs4 import BeautifulSoup
import requests

website = requests.get('https://www.google.com/search?q=python') # enable users to input own keywords (refer to 10 line youtube video for string stitching)

soup = BeautifulSoup(website.content, 'html.parser')

titles = soup.select('.r a')

for title in titles:
    href = link.get_attribute("href")
    print("href")

