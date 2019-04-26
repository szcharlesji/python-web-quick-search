import requests, sys, webbrowser, bs4

res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
linkelements = soup.select('.r a')
linktoopen = min(5,len(linkelements))

for i in range(linktoopen):
    webbrowser.open('https://google.com'+linkelements[i].get('href'))