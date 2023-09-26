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
#------------------------------------------------------------------------------------------------------------------




# 1. 0~9 사이 3개의 정수를 만들 랜덤함수 작성
import random
# 랜덤(난수)으로 나와 만든 요소를 담을 (난수)리스트 
ranlist = []

# 1.1. 정수 3개 만들기
while len(ranlist) < 3 :
    # 1.2. 0~9 사이개 만들기
    value = random.randint(0,9)
    # 1.3. 조건 : 중복 X   
    if value not in ranlist : 
        ranlist.append(value)

#################################################
# # 정수 3개 만들기 函数 
# def Integer (entire,kara,made,name) :
#     name = []
#     import random
#     while len(name) <entire :
#         value = random.randint(kara,made)   
#         if value not in name :
#             name.append(value)
#     return name
# # 함수 입력 部分    
# print(Integer(,,,""))
#################################################



# 횟수 체크 할 'count' 변수 생성
count =1
# 전체 흐름 (while 문) 제어할 스위치     
flag = True

# 2. 전체 흐름 제어 할 반복문 작성  (ON / OFF 스위치 만들기)
while flag :
# 2.1. 출력문 - 시도횟수 : N
    print("시도횟수 : ",count)
# 2.2. 출력문 - 정수 3개를 입력하세용~~~^__^
    print("정수 3개를 입력하세용~~~^__^")
# 2.3. 입력 받은 정수 보이게 하기 

    #############################################################################################
    # 3. 사용자로 부터 입력 값 3개 받기 
    mylist = []
    # 3.1. 반복문으로 부터 받은 3개의 입력값 저장할 리스트 공간 만들기 
    for value in range (3) : 
        # 3.2. 총 세 번동안 입력 받을 창 출력  -> 입력값 받기 
        #      입력 받은 값을 바로 리스트에 넣기 
        mylist.append(int(input(str(value+1)+"번째 값을 입력 : ")))
    #############################################################################################


    # Strike・Ball・Out 의 변수 공간 만들기
    Strike = 0
    Ball   = 0
    Out    = 0

# 4. 조건에 따른 반복문  - 입력 값을 기준으로 
    for index in range(len(mylist)) : 
        Element = mylist[index]  
        # 4.1. Strike・Ball
        if Element in ranlist :
            # 4.1.1. Strike
            if Element == ranlist[index] : 
                Strike += 1 
            # 4.1.2. Ball
            elif Element != ranlist[index] :
                Ball += 1
    # 4.1.3. Out
    #  -> Strike == 0 or Ball == 0  
    if Strike == 0 and Ball == 0 :
        Out += 1
    
    # 4.2. 4번 반복문 종료 시 'count'회수 증가 
    count += 1 

    

#############################################################################################
    # 5. 조건에 따른 Strike・Ball・Out 수량 출력
    # 5.1. Out 
    if Out >= 1 :
        print("Out : ",Out,"번")
    # 5.2.  Strike・Ball
    if Strike >=1  or  Ball >= 1 :
        # 5.2.1.  Strike
        if Strike >= 1 :
            print(Strike," Strike")
        # 5.2.2.  Ball
        elif Ball >= 1 :
            print(Ball," Ball")
    elif Strike >=1  and  Ball >= 1 :      
        print(Strike," Strike"," ",Ball," Ball")

#############################################################################################

# 5.3. 4번 반복문 종료 시  Strike・Ball  = 0 으로 초기화
    Strike = 0
    Ball   = 0


# 6.끝. 조건문 - 만약  시도 횟수 >= 5 ,  Out ==2  이면 -> "스위치 OFF" 
    if count >= 5  or  Out == 2 :        
# 6.1 출력문 - 게임횟수 초과 
        print()
        print("게임횟수 초과")
# 6.2 출력문 - 아까비~~~ 졌네용.. 
        print("아까비~~~ 졌네용..")
# 6.3 출력문 - 정답은 ranlist[0] , ranlist[1] , ranlist[2] 입니다.
        print("정답은",ranlist[0] , ranlist[1] , ranlist[2], "입니다.")
# 6.4 출력문 - 계속하려면 'Ctl + F5' 를 누르십시오...
        print("계속하려면 'Ctl + F5' 를 누르십시오...")
# 6.5 스위치 OFF  
        flag = False
    # 미관상 띄우기     
    print()
