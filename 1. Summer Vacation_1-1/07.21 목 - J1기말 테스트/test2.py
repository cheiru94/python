flag =True # while문 제어기


# 1.  0이 나올 때 까지 반복시킬 반복문 작성
while flag :
    # 2.  정수 입력 받기
    Inputvalue = int(input("정수를 입력 하세요 : "))

    # 3.   조건식
    # 3.1   양수일 때
    if Inputvalue > 0 :
        print("양수 입니다.")
    # 3.2   0 일 때    
    elif Inputvalue == 0 :
        flag =False
    # 3.3  음수일 때    
    else : 
        print("음수 입니다.")