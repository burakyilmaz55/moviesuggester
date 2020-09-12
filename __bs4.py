import requests
from bs4 import BeautifulSoup
import random

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

list = soup.find('tbody', {"class":"lister-list"}).find_all('tr')
sayi = random.randint(1,250)
movies = []

for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td",{"class":"ratingColumn"}).find("strong").text
    movies.append([title,year,rating])

randoMovie = movies[sayi]
print(f"Film Adı: {randoMovie[0]}\n Vizyon Yılı: {randoMovie[1]}\nIMDB Puanı: {randoMovie[2]}")