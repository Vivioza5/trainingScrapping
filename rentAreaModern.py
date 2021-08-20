import itertools

from bs4 import BeautifulSoup
import requests
from pprint import pprint
import csv
import pandas as pd
import os

from pandas.core import frame

root = 'https://sportguide.kiev.ua/section/rent/149-futzal'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
FILE = 'area1.csv'

def get_html(root):
    result = requests.get(root,headers=HEADERS)
    # content = result.text
    return result

def get_content(content):
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find_all('div', class_='zag3')
    tops= soup.find_all('div', class_='cont1')
    areaName=[]
    areaDescr=[]
    areaAdress=[]
    for item2 in tops:
        adress=item2.find('a',class_='fancybox-media').get_text(strip=True,separator='|')
        if 'Время - цена:' in item2.b:
            item2.findAll('b')[1].nextSibling.strip(),
        else:
            areaName.append ({
                item2.b.nextSibling.strip()
        })
        areaAdress.append({
             adress
          })
    for item in box:
        areaDescr.append({
            item.get_text(strip=True,separator='|')
        })

    areaFull=[]
    for i in itertools.zip_longest(areaName, areaDescr,areaAdress ):
        areaFull.append(i)
    areaList=list(areaFull)

    pprint(areaFull)







    # i=iter(areaName)
    # areaDict= dict(zip(i, i))
    # print(areaDict)
    # for k, v in areaDict.iteritems():
    #     print (k, v)

    # id, names = list(zip(*areaDescr))[:2]

        # print(areaDescr[0])
    # areaName.extend(areaDescr[0])
    # pprint(id[2])
    # pprint(areaName)
    return areaFull

def save_file(items, path):
    with open(path, 'w', newline=''):
        frame=pd.DataFrame(data=items)
        columns = ["Фирма1",'Фирма2','Фирма']
        (frame.to_csv(path, header=columns))
        print(frame[1])

def parse():
    html = get_html(root)

    if html.status_code == 200:
        areas=[]
        areas=get_content(html.text)
        # save_file(areas, FILE)
        # os.startfile(FILE)
    else:
        print('Error')


parse()
