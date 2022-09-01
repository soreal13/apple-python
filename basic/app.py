

# 리스트 = ['삼성전자', '카카오', '네이버', '신풍제약']

# f = open('a.txt', 'w')
# for i in 리스트:
#     f.write(i)
#     f.write('\n')
# f.close()

구구단 = '' 

for i in range(2,10):
    for j in range(1,10):
        print(str(i)+ 'x' + str(j)+ '=' + str(i*j))