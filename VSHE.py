# парсер вышки олимпиад
import requests
from bs4 import BeautifulSoup
from db import *
from time import time

code = '''EEvents = []
for i in range(500):
    EEvents.append([""] * 5)
EEvents[0][0] = "Название"
EEvents[0][1] = "Дата (+ время)"
EEvents[0][2] = "Ссылка"
EEvents[0][3] = "Описание"
EEvents[0][4] = "Тип"

myJSON={}
myJSON["operationName"]=None
myJSON["variables"]={}
myJSON["variables"]["types"]=[]
myJSON["variables"]["directions"]=[]
myJSON["variables"]["preferences"]=[]
myJSON["variables"]["grades"]=[]
myJSON["variables"]["isInProgress"]=False
myJSON["variables"]["section"]="school_hse"
myJSON["query"]="query ($types: [Int!], $directions: [Int!], $preferences: [Int!], $isInProgress: Boolean, $grades: [Int!], $section: OlympSectionName) {\n  schoolHseCompetitions: olympCompetitions(\n    types: $types\n    directions: $directions\n    preferences: $preferences\n    isInProgress: $isInProgress\n    grades: $grades\n    section: $section\n  ) {\n    id\n    title\n    description\n    image {\n      url\n      __typename\n    }\n    types {\n      title\n      color\n      __typename\n    }\n    startDate\n    endDate\n    url\n    comment\n    callToActionLabel\n    formattedDates\n    __typename\n  }\n}\n"

#олимпида/конкурсы
url = "https://www.hse.ru/n/gql"
dicty = requests.post(url, json = myJSON).json()
for header in dicty:
    newdicty = dicty[header]
actualevents = []
titles = []
hrefs = []
descriptions = []
datesofregister = []
for header in newdicty:
    for i in range(len(newdicty[header])):
        if newdicty[header][i]['comment'] != 'Регистрация в 2023-24 учебном году закрыта':
            actualevents.append(newdicty[header][i])
            

for i in range(len(actualevents)):
    for header in actualevents[i]:
        if header == 'title':
            EEvents[i + 1][0] = actualevents[i][header]
            if actualevents[i][header].count("олимипада") != 0 or actualevents[i][header].count("Олимипада") != 0:
                EEvents[i + 1][4] = "Олимпиада"
        if header == 'description':
            EEvents[i + 1][3] = actualevents[i][header]
        if header == 'url':
            EEvents[i + 1][2] = actualevents[i][header] 
        if header == 'comment':
            EEvents[i + 1][1] = actualevents[i][header]
#состязания
            url = "https://www.hse.ru/n/gql"
dicty = requests.post(url, json = myJSON).json()
for header in dicty:
    newdicty = dicty[header]
actualevents = []
titles = []
hrefs = []
descriptions = []
datesofregister = []
for header in newdicty:
    for i in range(len(newdicty[header])):
        if newdicty[header][i]['comment'] != 'Регистрация в 2023-24 учебном году закрыта':
            actualevents.append(newdicty[header][i])
            

for i in range(len(actualevents)):
    for header in actualevents[i]:
        if header == 'title':
            EEvents[i + 1][0] = actualevents[i][header]
            if actualevents[i][header].count("олимипада") != 0 or actualevents[i][header].count("Олимипада") != 0:
                EEvents[i + 1][4] = "Олимпиада"
        if header == 'description':
            EEvents[i + 1][3] = actualevents[i][header]
        if header == 'url':
            EEvents[i + 1][2] = actualevents[i][header] 
        if header == 'comment':
            EEvents[i + 1][1] = actualevents[i][header]

#отрезаем лишнее
EEvent_new = []
for i in range(len(EEvents)):
    if len(EEvents[i][0]) != 0:
        EEvent_new.append(EEvents[i])

#добавляем в базу
for i in range(1, len(EEvents)):
    add_event(EEvents[i])'''


t = time()
while True:
    currentTime = time()
    if int(currentTime - t) % 15 == 0:
        exec(code)
