from peewee import *
from db import *
import requests
from bs4 import BeautifulSoup

def stankin_parser():
    url = "https://msk.postupi.online/vuz/stankin/calendar/"
    response = requests.get(url)

    EEvents = []
    EEvents.append(["Название", "Дата (+ время)", "Ссылка", "Описание", "Тип"])
    titles = []
    dates = []
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        headers = soup.find("ul", class_ ="list-unstyled list-wrap")
        titlesparagraphs = headers.find_all("h3", class_ ="list__h")
        datesparagraphs = headers.find_all("p", class_ = "list-clndr__date")
        for date in datesparagraphs:
            dates.append(date.text)
        for title in titlesparagraphs:
            titles.append(title.text)
    else:
        print("Ошибка при получении страницы:", response.status_code)

    for i in range(len(dates)):
        EEvents.append([titles[i], dates[i], "https://msk.postupi.online/vuz/stankin/calendar/", "", "Встреча"])


    for i in range(1, len(EEvents)):
        add_event(EEvents[i])
    print(EEvents)
    print('done Olimp')
stankin_parser()