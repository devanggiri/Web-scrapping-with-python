import requests
from bs4 import BeautifulSoup

# baseurl = 'https://www.fabhotels.com/blog'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

r = requests.get('https://www.fabhotels.com/blog/top-12-destinations-to-visit-for-12-months', headers=headers)
soup = BeautifulSoup(r.content, 'lxml')
y = soup.find_all()
print(y)
