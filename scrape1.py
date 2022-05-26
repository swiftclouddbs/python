import requests
from bs4 import BeautifulSoup

url = "https://www.tutorialspoint.com/index.htm"

#page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")

req= requests.get(url)

soup = BeautifulSoup(req.text, "html.parser")

#with open("example.htm") as fp:
#   soup = BeautifulSoup(fp)
#soup = BeautifulSoup("<html>data</html>")

for link in soup.find_all('a'):
	print(link.get('href'))


#print(page.status_code)
print(soup)

#print(soup.prettify())
