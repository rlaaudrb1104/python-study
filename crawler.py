#크롤러
import requests #남이 짜놓은 코드 가져오는 법
from bs4 import BeautifulSoup #파이썬으로 HTML 분석

data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930') #웹 페이지 정보

print(data.content) #웹페이지의 HTML 출력
print(data.status_code) #웹페이지 정상접속 유무 200>>정상 400or500>>비정상


soup = BeautifulSoup(data.content, 'html.parser') #가져온 데이터 가공

print(soup)#가공된 데이터 출력
print('현재가:' + soup.find_all('strong',id="_nowVal")[0].text) 
#필요한 정보만 출력 ('태그명',"속성명") // 찾은 결과 리스트로 반환

print('거래량:' + soup.find_all('span', id="_quant")[0].text) 
#거래량 출력// 클래스로 찾고 싶으면 class_= // 띄어쓰기 되어있을 시 하나만 쓴다.
#but 클래스는 유일하지 않으므로 여러개 나올 수 있다
