# 라이브러리 에서 추출하기 
import requests                    # 1. 원하는 사이트이 url을 html 형식으로 파이썬에 가져오기 위한 라이브러리
from bs4 import BeautifulSoup      # 2. html 소스에서 해당 부분만 추출하기 위해 파씽하는 라이브러리 
import pyautogui                   # 3. 검색 입력 창 나타는 라이브러리   gui형식으로 input 나타내기  =>  py  auto  "gui" 


keyword = pyautogui.prompt("♥ 검색어를 입력하세요 ♥")                     # 1. 검색어 입력 받기
lastpage = pyautogui.prompt("♥ 마지막 페이지 번호룰 입력 하세요 ♥")   # 2. 페이지 입력 받기 -  입력받은 문자열을 int 형으로 형 변환 
page_num = 1      # 페이지 알려줄 입력창 나타내기 



# 여러 페이지를 반복적으로 증가시킬 반복문 작성
for page in range ( 1 , int(lastpage) * 10 , 10 ) :      #  lastpage = 1-1p , 11-2p,  21-3p
    # 페이지 나타내기
    print(f"------------------------------------------------{page_num}페이지 입니다 ------------------------------------------------")
    print()  # 줄 변경
    # 원하는 페이지(링크) 요청
    responses = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&star={page}")
    html = responses.text                        # .text 를 붙여 텍스트만 가져오기// html 소스코드 = 웹사이트 전체의 정보   //  텍스트 , 선택자 구분 못하고 전부 텍스트로 인식
    soup = BeautifulSoup(html,"html.parser")     # html 중에서 원하는 정보만 추출   // 텍스트와 선택자를 구분 가능하게 만듬
    links = soup.select(".news_tit")             # 결과는 리스트로 나온다 

    for link in links : 
        title = link.text           # 태그안에 텍스트요소를 가져온다.
        url = link.attrs['href']    # href의 속성값을 가져온다 
        print(title)
        print(url)
        print()
    page_num += 1

# for value in range(len(links)) : 
#     print(links[value])
# print(len(links))
     