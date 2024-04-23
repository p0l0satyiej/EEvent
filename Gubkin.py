from peewee import *
from db import *
import requests
from bs4 import BeautifulSoup

def Gubkin_parser():
    url = "https://www.gubkin.ru/events/"
    response = requests.get(url)

    EEvents = []
    EEvents.append(["Название", "Дата (+ время)", "Ссылка", "Описание", "Тип"])
    hrefs = []
    titles = []
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        headers = soup.find("div", class_ ="b-news-items")
        headers2 = headers.find_all("div", class_ ="b-news-items")
        for header in headers2:
            hrefs.append(header.get("href"))
            titles.append(header.text)
        #print(titles)
    else:
        print("Ошибка при получении страницы:", response.status_code)

    for i in range(len(hrefs)):
        EEvents.append([titles[i], "", hrefs[i], "", "Олимпиада"])


    for i in range(1, len(EEvents)):
        add_event(EEvents[i])
    print('done Olimp')
Gubkin_parser()