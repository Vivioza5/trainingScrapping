from bs4 import BeautifulSoup
import requests
from splinter import browser, Browser

from .pages.locators import MainLocators

browser = Browser('chrome')
browser.visit(MainLocators.LINK)
browser.fill('q',"снять в аренду футбольное поле")
browser.find_by_name('btnK').click()

result=requests.get(browser.url)
content = result.text
soup = BeautifulSoup(content, 'lxml')
box = soup.find('div', class_='yuRUbf')
links = [link['href'] for link in box.find_all('a', href=True)]
for link in links:
    result = requests.get(f'{link}')
    content = result.text(strip=True, separator=' ')
    soup = BeautifulSoup(content, 'lxml')
    box1 = soup.find('h3', class_='zBAuLc').get_text()
    print()
    # title = box.find('h1')
with open(f'examples/linksRent.txt', 'w') as file:
        file.write(box1)

# class findLinksWriteToFile():
#
#     def open_Goggle(self):



#
# root = 'https://subslikescript.com'
# website = f'{root}/movies'
# result = requests.get(website)
# content = result.text
# soup = BeautifulSoup(content, 'lxml')
# box = soup.find('article', class_='main-article')
# links = [link['href'] for link in box.find_all('a', href=True)]
#
# for link in links:
#     result = requests.get(f'{root}/{link}')
#     content = result.text
#     soup = BeautifulSoup(content, 'lxml')
#
#     box = soup.find('article', class_='main-article')
#     title = box.find('h1').get_text()
#     transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
#
#     with open(f'examples/{title}.txt', 'w') as file:
#         file.write(transcript)