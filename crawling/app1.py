import requests
from bs4 import BeautifulSoup

# proxies = {
#     'http' : '43.76.42.83:8080',
#     'https' : '43.76.42.83:8080'
# }

# 데이터 = requests.get('https://finance.naver.com/item/main.naver?code=011070', proxies=proxies)


# 크롤러 만드는 법
# 1. 파이썬으로 원하는 페이지 접속해서 HTML 가져옴
# 2. 원하는 글자만 추림


데이터 = requests.get('https://finance.naver.com/item/main.naver?code=011070')

soup = BeautifulSoup(데이터.content, 'html.parser')

print(soup.find_all('strong', id="_nowVal")[0].text)
print(soup.find_all('span', class_="tah")[5].text)

soup.select('strong#_nowVal') # css 셀렉터
soup.select('.gray .f_down em')[0].text # 오른쪽 클릭 copy selector 쓰면 꿀팁

이미지 = soup.select('#img_chart_area')[0]
print(이미지['src'])


# 방법1 return
def nowPrice(param) :
    data = requests.get(f'https://finance.naver.com/item/main.naver?code={param}')
    soup = BeautifulSoup(data.content, 'html.parser')
    print(soup.find_all('strong', id="_nowVal")[0].text)
    print(soup.find_all('span', class_="tah")[5].text)
    return print(soup.find_all('strong', id="_nowVal")[0].text)

f = open('a.txt', 'w')
f.write(nowPrice('005930'))
f.close()


# 방법 2 list
리스트 = []
def nowPrice2(param) :
    data = requests.get(f'https://finance.naver.com/item/main.naver?code={param}')
    soup = BeautifulSoup(data.content, 'html.parser')
    print(soup.find_all('strong', id="_nowVal")[0].text)
    print(soup.find_all('span', class_="tah")[5].text)
    리스트.append(print(soup.find_all('strong', id="_nowVal")[0].text))

f = open('a2.txt', 'w')
f.write(리스트[0])
f.close()


# 숙제 : 다음 종목들의 현재가격을 전부 txt 파일로 저장하려면?

종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']

def stockPrice(param) :
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={param}')
    soup = BeautifulSoup(data.content, 'html.parser')
    return print(soup.find_all('strong', id="_nowVal")[0].text)

f = open('a3.txt', 'w')
for i in 종목들:
    f.write( '\n' + stockPrice(i))
f.close()
