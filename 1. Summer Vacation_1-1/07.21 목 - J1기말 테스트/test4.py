# 1 ~ 100 까지 양의 정수 중 “3”이 포함된 정수만 출력


Count = 1  # while 문을 세기위한 변수

Letter = "" # 문자열 담기

# 1.  1 ~ 100 까지 반복시킬 반복문
while Count <= 100 :
    # Count 를 문자로 바꾸기 
    Letter += str(Count)

    # 2.  Count 에 요소를 하나씩 꺼내기 위한 for 반복문 작성
    for value in Letter : 

    # 3.  조건문 3이 포함이면
        if value == "3" :
            print(Count)
    # 4.  문자열 초기화
    Letter = ""
    # 5.  카운트 1씩 증가 
    Count += 1