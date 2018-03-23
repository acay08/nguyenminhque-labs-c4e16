from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

data = conn.read()
html_content = data

soup = BeautifulSoup(html_content, "html.parser")

table = soup.find('table', id = 'tableContent', style="border-top: solid 1px #e6e6e6;border-left:solid 1px #cccccc;border-bottom:solid 1px #cccccc")

tr_list = table.find_all('tr', ['r_item', 'r_item_a'])

# print(tr_list)
datas = []
title = ['item', 'Q4-2016', 'Q1-2017', 'Q2-2017', 'Q3-2017']
count = 0

for tr in tr_list:
    data = {}
    td_list = tr.find_all('td')
    i = 0
    for td in td_list[0:5]:
        data[title[i]] = td.string
        i +=1
    datas.append(data)


pyexcel.save_as(records=datas, dest_file_name="vinamilk.xlsx")
