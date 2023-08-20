종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']

import requests
from bs4 import BeautifulSoup

for x in 종목들 :
    data = requests.get('https://finance.naver.com/item/sise.naver?code=' + x)
    soup = BeautifulSoup(data.content, 'html.parser') 

    file = open('a.txt', 'a')
    file.write(soup.find_all('strong', id="_nowVal")[0].text + '\n')
    file.close()  
    

