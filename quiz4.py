import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint


file = open('result.csv', 'w', encoding='utf-8_sig', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['სათაური', 'ავტორი', 'ფასი'])

for ind in range(1, 7):
    url = "https://daraba.art/ge/artworks?categories=4&priceFrom=0&minPeriod=1910&maxPeriod=2020&minWidth=1&maxWidth=" \
          "200&minHeight=1&maxHeight=200&priceTo=8480&material=&medium=&color=&subject=&sort=&discover=&page=" +\
          str(ind)
    r = requests.get(url)
    # print(r.headers)
    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    all_painting = soup.find('div', id='product-list')
    # print(all_painting)
    paintings = all_painting.find_all('div', class_='article-item')
    # print(paintings)

    for painting in paintings:
        p_features = painting.find('div', class_='title-container')
        p_price = painting.find('span', class_='new-price')
        p_title = p_features.h4.a.text.strip()
        p_author = p_features.h6.a.text.strip()
        print(p_title)
        print(p_author)
        print(p_price.text)
        file_obj.writerow([p_title, p_author, p_price.text])

    sleep(randint(1, 5))

file.close()
