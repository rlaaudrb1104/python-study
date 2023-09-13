#네이버 로그인 뚫기
#1. 복사 붙여넣기 이용
#2. 실제 브라우저처럼 꾸미기

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyperclip




driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/')


time.sleep(5)
pyperclip.copy('아이디')
e = driver.find_element(By.XPATH, '//*[@id="id"]')
e.send_keys(Keys.CONTROL,'v')

time.sleep(1)

pyperclip.copy('비밀번호')
e = driver.find_element(By.XPATH, '//*[@id="pw"]')
e.send_keys(Keys.CONTROL,'v')
time.sleep(1)
e.send_keys(Keys.ENTER)

time.sleep(4)
driver.get('https://m.blog.naver.com/FeedList.naver')
time.sleep(7)
driver.get('https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FGoWriteForm.naver')
time.sleep(3)
e = driver.find_element(By.XPATH, '//*[@id="se_component_wrapper"]/div[1]/div/div[3]/div/div/div/div/textarea')
e.send_keys('블로그 제목입니다.')

e = driver.find_element(By.XPATH, '//*[@id="se_component_wrapper"]/div[2]/div/div/div/div[2]/div/div/div/div')
e.send_keys('블로그 내용입니다.')
e.send_keys(Keys.ENTER)


time.sleep(20)