from peewee import *
from db import *
import requests
from bs4 import BeautifulSoup

def Olimp_parser():
    url = "https://rsr-olymp.ru/"
    response = requests.get(url)

    EEvents = []
    EEvents.append(["Название", "Дата (+ время)", "Ссылка", "Описание", "Тип"])
    hrefs = []
    titles = []
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        headers = soup.find("div", id="main_table")
        headers2 = headers.find_all("a", target="_blank")
        headers3 = headers.find_all("tbody")
        for header in headers2:
            hrefs.append(header.get("href"))
            titles.append(header.text)

    else:
        print("Ошибка при получении страницы:", response.status_code)

    for i in range(len(hrefs)):
        EEvents.append([titles[i], "", hrefs[i], "", "Олимпиада"])


    for i in range(1, len(EEvents)):
        add_event(EEvents[i])
    print('done Olimp')

