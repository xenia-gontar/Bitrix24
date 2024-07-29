from bs4 import BeautifulSoup


page = open("index.html", "r+")
soup = BeautifulSoup(page, "html.parser")

print(soup.find_all('dd',itemprop="foundingDate"))
