from bs4 import BeautifulSoup
import requests
import re

key    = input('Keyword : ')

url    = f"https://www.joox.com/id/search/{key}"
url    = url.replace(" ", "%20")
page   = requests.get(url)
s      = BeautifulSoup(page.content, 'html.parser')

title  = s.find('b', class_='jsx-2493651356 SongName').text
artis  = s.find('span', class_='jsx-3317143431 SongDescItem').text
url    = s.find('b', class_='jsx-2493651356 SongName').a['href']

url    = f"https://www.joox.com{url}"
page   = requests.get(url)
s      = BeautifulSoup(page.content, 'html.parser')

lyrics = s.find('div', class_='jsx-804686892 renderLyrics')

if lyrics is None:
    print('Lirik Tidak Tersedia')
    exit()
    pass

print(f"\n{title} - {artis}\n")
for lyric in lyrics:
    lyric = str(lyric).replace("<p>", "").replace("</p>", "")
    print(lyric)
