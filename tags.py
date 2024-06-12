import requests
from bs4 import BeautifulSoup


with open("sample.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.div)     
# print(soup.find_all("div"))
# print((soup.find_all("div")[1]))

# #find links in web page
# for link in soup.find_all("a"): #a for anchor tags
#     print(link.get("href")) #href for links
#     print(link.get_text())

# cont = soup. find(class_="container")
# print (cont. has_attr("contenteditable"))

def has_class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

results = soup.find_all(has_class_but_not_id)
print(results)

print("----------------------------------------------")

def has_content (tag):
    return tag.has_attr("content")

results = soup.find_all(has_content)
for result in results:
    print(result, "\n\n")