list = ['삼성전자', '카카오', '네이버', '신풍제약']

file = open('Homework1.txt', 'w')
for x in list :
    file.write(x)
    file.write('\n')
file.close()