from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)

data = conn.read()
html_content = data

soup = BeautifulSoup(html_content, "html.parser")

section = soup.find('section', 'section chart-grid')

li_list = section.find_all('li')

datas = []

for li in li_list:
    data = {}
    a = li.h3.a
    data["Song name"] = a.string
    b = li.h4.a
    data["Artist"] = b.string
    datas.append(data)

    search_name = a.string + b.string
    options = {
        'default_search': 'ytsearch',
        'max_downloads': 1
    }
    dl = YoutubeDL(options)
    dl.download([search_name])

# pyexcel.save_as(records=datas, dest_file_name="songs.xlsx")    # already saved
