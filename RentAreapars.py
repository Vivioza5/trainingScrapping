from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re
root = 'https://sportguide.kiev.ua/section/rent/149-futzal'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
result = requests.get(root,headers=HEADERS)
content = result.text
soup = BeautifulSoup(content, 'lxml')
box = soup.find_all('div', class_='zag3')
tops= soup.find_all('div', class_='cont1')
top= soup.find('div', class_='cont1')
root_childs = [e.name for e in top.descendants if e.name is not None]
areaName=[]
count=0
for area in box:
    areaName.append({
         area.find('h3').get_text(strip=True, separator='|')
    })
    count+=1
print(count)
areaRules=[]
areaDescr=[]
for rul in tops:
    distr=rul.get_text(strip=True,separator='|')
    areaRules.append(distr)
    areaRules= '|'.join(areaRules).replace(':|', ': ').split('|')
for item in areaRules:
    if 'Район' in item:

        areaDescr.append({
             item.strip()
        })

areaDescr2=[]
for item1 in areaRules:
    if 'Район' in item:
        areaDescr2.append({
             item1.strip()
        })
# pprint(areaDescr)
areaFull=[]
for q, a  in zip(areaName, areaDescr ):
    areaFull.append({
        '{0},  {1}.'.format(q, a).replace('/\'', ' ')
    })

pprint(areaFull)
# #
# #     with open(f'examples/title.txt', 'w') as file:
# #         file.write(transcript)
# count1=0
# for item2 in tops:
#     if 'Время - цена:' in item2.b:
#         print(item2.findAll('b')[1].nextSibling)
#     else:
#         print(item2.b.nextSibling)
# print (count1)
# print(tops[2].b)

