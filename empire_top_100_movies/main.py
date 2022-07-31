from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all("h3", class_="title")
for movie in movies[::-1]:
    # print(movie.getText())
    with open("movies.txt", "a") as f:
        f.write(f"{movie.getText()}\n")