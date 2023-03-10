from bs4 import BeautifulSoup
import requests

contents = ""
for page in range(3):
    response = requests.get(f"https://news.ycombinator.com/?p={page}")
    contents += response.text

soup = BeautifulSoup(contents, "html.parser")

articles = soup.select(".titleline > a")
upvote = soup.select("td .subtext")

article_text =[article.get_text() for article in articles]
article_link = [article.get("href") for article in articles]
article_upvote = []


for vote in upvote:
    try:
        article_upvote.append(int(vote.select_one("span .score").getText().split()[0]))
    except AttributeError:
        article_upvote.append(0)

print(article_text, f'\n{len(article_text)}')
print(article_link, f'\n{len(article_link)}')
print(article_upvote, f'\n{len(article_upvote)}')

index_highest_score = article_upvote.index(max(article_upvote))
title_most_voted = {article_text[index_highest_score]: [article_link[index_highest_score], article_upvote[index_highest_score]]}
print(title_most_voted)





















