
#파일 쓰는 법
파일 = open('a.txt', 'w')
파일.write('hello')
파일.close()

#파일 읽는 법
파일 = open('a.txt', 'r')
print(파일.read())
파일.close()

#파일에 내용 추가
파일 = open('a.txt', 'a')
파일.write('hello')
파일.close()