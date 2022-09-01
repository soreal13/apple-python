from urllib import request
import requests
from bs4 import BeautifulSoup


# 무한 스크롤 데이터 수집
# 웹페이지에 원하는 데이터가 나중에 뜬다면, 갑자기 페이지에 추가되는 데이터들은 Network 탭가면 나옴.

# html에서 백슬래시가 들어가는 경우 제거하면 됨.

data = requests.get('https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=1&query=%ED%80%B8%EB%A1%9C%EC%A0%9C&nso=&nqx_theme=&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_nmr&ssc=tab.view.view&ngn_country=KR&lgl_rcode=09560110&fgn_region=&fgn_city=&lgl_lat=37.528317&lgl_long=126.929425&abt=&_callback=viewMoreContents')

soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser') # data.content는 object형 자료이므로 replace를 사용하기 위해 text를 써준다.

txtList = soup.select('a.api_txt_lines')
print(txtList[0].text)
print(txtList[1].text)
print(txtList[2]['href'])


data = requests.get('https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=31&query=%ED%80%B8%EB%A1%9C%EC%A0%9C&nso=&nqx_theme=&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=31&sm=tab_nmr&ssc=tab.view.view&ngn_country=KR&lgl_rcode=09560110&fgn_region=&fgn_city=&lgl_lat=37.528317&lgl_long=126.929425&abt=&_callback=viewMoreContents')


# 혼자 할 수 있는 프로젝트
# 1. 네이버 블로그 검색시 100개 검색물 수집
# def 네이버블로그순위('사과') 하면 1등부터 5등까지 남는 함수.


def naverBlogRank(keyword) :
    data = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=43&where=view&api_type=11&start=1&query={keyword}')
    soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')
    subjects = soup.select('a.api_txt_lines')
    subList = []
    for i in range(5):
        subList.append(subjects[i].text)
    return subList

print(naverBlogRank('퀸로제'))
