from bs4 import BeautifulSoup


page = open("index.html", "r+")
soup = BeautifulSoup(page, "html.parser")

result = soup.find_all('dd',itemprop="foundingDate")

print(result[0].get_text())
