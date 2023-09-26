import requests
from bs4 import BeautifulSoup
import pyautogui 

keyword = pyautogui.prompt("♥ 검색어를 입력하세요 ♥") 

responses = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")

# 해당 url 의 전체 html 소스코드 가져오기 - 문자형태로만 가져온것
html = responses.text # .text 를 붙여 텍스트만 가져오기// html 소스코드 = 웹사이트 전체의 정보 

# html 소스(문자형태) 를 html 형식으로 틀 잡기(parsing 하기 위함) - ( select 를 사용하여 원하는 부분을 추출하기 위해 )
soup = BeautifulSoup(html,"html.parser") # html 중에서 원하는 정보만 추출 
links = soup.select(".news_tit")  # 결과는 리스트로 나온다 
 

for link in links : 
    title = link.text           # 태그안에 텍스트요소를 가져온다.
    url = link.attrs['href']    # href의 속성값을 가져온다 
    print(title)
    print(url)
    print()


# for value in range(len(links)) : 
#     print(links[value])
# print(len(links))
     