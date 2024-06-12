from bs4 import BeautifulSoup  
import requests


url= "https://www.flipkart.com/search?q=puma%20shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


r=requests.get(url, headers=head)

soup = BeautifulSoup(r.text, 'html.parser')
#print (soup.prettify())
spans = soup.select(class_.PUMA)
print(spans)
# for span in spans: 
#     print(span.string) 