import requests
from bs4 import BeautifulSoup
import json
import os
import time
import re
import lxml

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
url = 'https://mm.enterdesk.com/dongmanmeinv/'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('img')
folder_path = './photos/'
if os.path.exists(folder_path) == False:
    os.makedirs(folder_path)

for index,item in enumerate(items):
    if item:
        html = requests.get(item.get('src'))
        img_name = folder_path +str(index + 1) + '.jpg'
        with open(img_name,'wb') as file:
            file.write(html.content)
            file.flush()
        file.close()
        print('第%d张图片下载完成'%(index + 1))
        time.sleep(1)

print('抓取完成')










