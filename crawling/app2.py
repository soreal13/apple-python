import requests
from bs4 import BeautifulSoup

# 함수 잘쓰는 법 1: 긴 코드 축약
def 인사하기() :
    print('안녕하세요~~')
    print('두번째 인사~')

# 함수 잘쓰는 법 2: 마법의 모자 가능. 집어넣으면 다른게 나오는 변환기.
def 모자(hole) :
    print(hole)

모자('hello')

# 함수 잘쓰는 법 3: 함수 실행하고 나서 가죽을 남기고 싶을 때

def 함수() :
    return 10

print(함수())

