import requests 
from bs4 import BeautifulSoup 
data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')
soup = BeautifulSoup(data.content, 'html.parser') #가져온 데이터 가공

# 1. 글자가 해체되어있는 경우
# >> 상위 클래스를 찾으면 된다.

# 2. class, id가 하나도 없는 요소
# >> 1) 태그 찾아서 인덱싱
# >> 2) soup.select('css 셀렉터 입력') >> 상위 클래스 찾아서 태그 찾기 
# >> CSS selector >> class는 . id는 # 둘다 만족하려면 붙여쓰기 
soup.select('.class명')
soup.select('#id명')
soup.select('태크명') #HTML 태그명은 아무것도 붙이지 않는다.
soup.select('.class명1 .class명2') # 띄어쓰기는 '~내부의' 라는 뜻

# 3. 이미지 수집
img = soup.select('#img_chart_area')[0] #id가 이미지인 것 찾기
print(img['src']) #이미지 파일로 저장하기 위한 src 추출

# 이미지 URL을 알고있을 때 파일로 저장하는 법
import urllib.request #import 모여있는 맨위에다가 작성
urllib.request.urletrieve(이미지URL, '파일명') # 실행하면 파이썬 파일이 있는 곳에 파일명.jpg 저장
