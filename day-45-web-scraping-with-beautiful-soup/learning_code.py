from bs4 import BeautifulSoup


with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)

company_url = soup.select_one(selector="p a")
print(company_url)

headings = soup.select(selector=".heading")
print(headings)