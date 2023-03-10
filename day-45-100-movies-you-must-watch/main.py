import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in reversed(titles):
        file.write(f"{movie}\n")

