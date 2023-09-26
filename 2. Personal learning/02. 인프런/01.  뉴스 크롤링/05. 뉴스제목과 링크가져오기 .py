from http.client import responses
from urllib import response
import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup




responses = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = responses.text # .text 를 붙여 텍스트만 가져오기// html 소스코드 = 웹사이트 전체의 정보 
soup = BeautifulSoup(html,"html.parser") # html 중에서 원하는 정보만 추출 
links = soup.select(".news_tit")  # 결과는 리스트로 나온다 
 

for link in links : 
    title = link.text           # 태그안에 텍스트요소를 가져온다.
    url = link.attrs['href']    # href의 속성값을 가져온다 
    print(title)
    print(url)


# for value in range(len(links)) : 
#     print(links[value])
# print(len(links))
     