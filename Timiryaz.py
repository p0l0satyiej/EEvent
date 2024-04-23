from peewee import *
from db import *
import requests
from bs4 import BeautifulSoup

def Timiryaz_parser():
    url = "https://www.timacad.ru/"
    response = requests.get(url)

    EEvents = []
    EEvents.append(["Название", "Дата (+ время)", "Ссылка", "Описание", "Тип"])
    hrefs = []
    titles = []
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        #headers = soup.find_all("a", class_ ="tabs-type-1__item announce-main__itemtabs-type-1__blocks-container announce-main row")
        headers = soup.find("div", class_ ="tabs-type-1__blocks-container announce-main row")
        #headers2 = headers.find_all("div", class_ ="col-6")
        '''for header in headers:
            hrefs.append(header.get("href"))
            titles.append(header.text)'''
        print(headers)
    else:
        print("Ошибка при получении страницы:", response.status_code)

    for i in range(len(hrefs)):
        EEvents.append([titles[i], "", hrefs[i], "", "Олимпиада"])


    for i in range(1, len(EEvents)):
        add_event(EEvents[i])
    print('done Olimp')
Timiryaz_parser()