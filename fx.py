# 함수 *위에서 미리 만들고 사용*
# 1. 긴 코드를 짧은 단어로 축약할 때
def 인사하기() :
    print('안녕하세요 중고차 신뢰딜러 차은우입니다')
    print('안녕하세요 중고차 신뢰딜러 차은우입니다')
인사하기()

# 2. 무언가를 집어넣으면 다른게 나오는 변환기
def 모자(구멍, 구멍2) :
    print(구멍 + 구멍2)

모자(1, 2)
# 3. 함수 실행하고 나서 가죽을 남기고 싶을 때

def 함수() :
    return 10

함수 ()
# 4. 함수에 구멍(파라미터) 잘뚫기
# 글자 중간에 변수넣기 >> f'글자{변수}글자'
def  현재가(구멍) :
    데이터 = requests.get(f'https://finance.naver.com/item/sise.naver?code={구멍}')

현재가('005930')
현재가('066575')