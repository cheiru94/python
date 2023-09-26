# #프로그램명: 야구 게임 만들기
#------------------------------------------------------------------------------------------------------------------
# 0~9사이의 3개 정수를 random.randint() API를 이용하여 난수로 생성.
# -정수의 범위는 0~9사이
# -중복 값 없이 생성. 예) 2, 2, 6 X → 2중복
#------------------------------------------------------------------------------------------------------------------
#  게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
#  • 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력 (예외처리 X)
#  • 아래 경우 게임 Lose
#   – 시도 횟수 >= 5
#   – Strike out == 2
#  • 아래 경우 게임 Win
#   – 컴퓨터에서 생성 한 난수 값을 자리 순서대로 맞출 경우

import random

# 시도 횟수 카운트 ,입력문
count = 1

###################################################################################################################
#시도 횟수 알림 

#0~9 사이 정수 입력 받기

# 3개의 정수(난수)를 담을 리스트 작성
ransu = []

# 반복문으로 3개의 정수 뽑기 : 총 3개의 난수 생성 (범위는 3까지)
while len(ransu) < 3 :
    value = random.randint(0,9)
    if value not in ransu :
        ransu.append(value)
# Game 의 정수가 안 겹치게    


###################################################################################################################

# 변수  Strike
Strike = 0
# 변수  Ball
Ball = 0
# 변수  Out
Out = 0

#while 전체 반복문 스위치 
switch = True

# 1. 전체를 반복으로 흐름을 제어할 반복문 작성
while switch :
    # count 알려주는 횟수 출력기
    print("시도횟수 :",count)
    print("정수 3개를 입력하세용~ ")
    
    # # n 번 변수 공간 작성
    # Number = int(input("몇개 입력 할래? : "))
    # # 반복문 으로 계속해서 myList 에 입력할 원소 뽑기 
    # for value in range (1,Number+1) :
    #     kazu = input(str(value)+"번째 정수 :")
    #     myList.append(kazu)

    # 입력 요소 리스트 공간 작성
    myList = []

    # 반복문 으로 계속해서 myList 에 입력할 원소 뽑기 
    for value in range (3) :
        kazu = int(input(str(value+1)+"번째 정수 :"))
        myList.append(kazu)

    # 위의 입력 받은 값들을 리스트로 정렬
    print(myList)
   
# [난수 값] 과 [입력 값] 비교
# 2. [난수 값] 을 for 반복문으로 하나씩 추출
        # 1. [입력 값] 을 for 반복문으로 하나씩 추출
    for index in range (len(myList)) :
        element = myList[index]
        # strike,ball  /조건문으로 판정 값 선택
        if element in ransu : 
            # strike
            if element == ransu[index] :
                Strike += 1
            #ball 
            elif element != ransu[index] : 
                Ball += 1
    # Out
    if Strike == 0 and  Ball == 0 :
        Out += 1
        # count     
    count += 1

    # Out
    if Out>=1 :
        print("Out : 아웃",Out,"번")
    # Strike , Ball 일 때 
    if Strike >= 1 or Ball>= 1 : 
        if Strike >= 1 :
            print(Strike,"Strike")
        elif Ball >= 1 :
            print(Ball,"Ball")
    elif Strike >= 1 and Ball>= 1 :
        print(Strike,"Strike"," ",Ball,"Ball")
        
# 시도 횟수 초과일경우  ->  count >=5  "or" Out == 2
    if  count >=5 or Out ==2 :
        print()
        print("게임횟수 초과")
        print("아까비~~~졌네용..")
        print("정답은 : " ,ransu[0],ransu[1],ransu[2], "입니다." )
        print("계속 하려면 Ctr + F5 를 눌러주세요")
        switch = False 
    #조건에 따른 출력문
    print()
    print()
    Strike = 0 
    Ball = 0 