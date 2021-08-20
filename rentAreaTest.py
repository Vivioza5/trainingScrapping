# парсинг аренды футбольных полей, потому как находятся в разных местах данные
# пришлось делать через frame in pandas надо будет посмотреть как можно обойтись
# без лишней функции создания фреймов и обьединения их
from bs4 import BeautifulSoup
import requests
import pandas as pd

root = 'https://sportguide.kiev.ua/section/rent/149-futzal'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
FILE = 'areaRent.csv'

def get_html(root):
    result = requests.get(root,headers=HEADERS)
    # content = result.text
    return result

def get_content(content):
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find_all('div', class_='zag3')
    tops= soup.find_all('div', class_='cont1')
    areaName=[]
    areaAdress=[]
    areaDistr=[]
    for item in box:
        areaName.append({
            'title':item.get_text(strip=True,separator='|')
        })
    # pprint(areaName)
    for item2 in tops:
        adress=item2.find('a',class_='fancybox-media').get_text(strip=True,separator='|')
        if 'Время - цена:' in item2.b:
            item2.findAll('b')[1].nextSibling.strip(),
        else:
            areaDistr.append ({
                'district':item2.b.nextSibling.strip()
        })
        areaAdress.append({
             'adress':adress
          })
    # pprint((areaAdress))
    frame1=create_frame(areaName)
    frame2=create_frame(areaAdress)
    frame3=create_frame(areaDistr)
    # print(frame1)
    # print(frame2)
    # print(frame3)
    fullFrame=frame1.join(frame2).join(frame3)
    # print(fullFrame)
    return fullFrame
def create_frame(items):
    frame=pd.DataFrame(data=items)
    return frame


def save_file(items, path):
    with open(path, 'w', newline=''):
        (items.to_csv(path))

def parse():
    html = get_html(root)
    if html.status_code == 200:
        areas=get_content(html.text)
        save_file(areas, FILE)
    else:
        print('Error')


parse()