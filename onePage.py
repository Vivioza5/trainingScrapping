from bs4 import BeautifulSoup
import requests
website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
box = soup.find('article', class_='main-article')
title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script')
transcript = transcript.get_text(strip=True, separator=' ')
print(soup.prettify())
with open(f'examples/{title}.html', 'w') as file:
    file.write(transcript)