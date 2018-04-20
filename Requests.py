import requests
from bs4 import BeautifulSoup as bp
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = bp(page.content, "html.parser")
print(page.status_code)
print("\n")

print(soup.prettify())
