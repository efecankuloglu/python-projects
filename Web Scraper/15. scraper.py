import string
import requests
from bs4 import BeautifulSoup
import os


pages = int(input("Please enter page number to look from 1 to:"))
subject = input("Please enter subject: ")

for page in range(1, pages + 1):
    os.mkdir(os.path.join(os.getcwd(), f"Page_{page}"))
    os.chdir(os.path.join(os.getcwd(), f"Page_{page}"))
    r = requests.get(f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={page}")
    soup = BeautifulSoup(r.content, "html.parser")
    for i in soup.find_all("article"):
        for j in i.find_all("span", {"data-test": "article.type"}):
            if j.find("span").text == subject:
                art = i.find_all("a", {"data-track-action": "view article"})
                for x in art:
                    title = ""
                    for a in x.text:
                        if a not in list(string.punctuation):
                            title += a
                    n_title = title.replace(" ", "_")
                    with open(os.path.join(os.getcwd(), f"{n_title}.txt"), "w", encoding="utf-8") as f:
                        link = "https://www.nature.com" + x.get("href")
                        content_r = requests.get(link)
                        soup2 = BeautifulSoup(content_r.content, "html.parser")
                        if soup2.find("div", {"class": "article__body"}) is not None:
                            txt = soup2.find("div", {"class": "article__body"}).text.strip()
                            f.write(f'{txt}')
                        elif soup2.find("div", {"class": "article-item__body"}) is not None:
                            txt = soup2.find("div", {"class": "article-item__body"}).text.strip()
                            f.write(f'{txt}')
                        elif soup2.find("div", {"class": "c-article-body"}) is not None:
                            txt = soup2.find("div", {"class": "c-article-body"}).text.strip()
                            f.write(f'{txt}')
    os.chdir("../")
print("Saved all articles")
