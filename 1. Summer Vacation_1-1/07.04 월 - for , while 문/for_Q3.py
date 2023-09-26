# 07.04 월
#
# 전체 층으로 사용할 변수 작성
floor = 5

# 1번 or 2번 택하게 조건문
for full in range(2):
    # 1번
    if full == 0:
        # 층을 반복적으로 작성할 for문 작성
        for row in range(floor):
            # 층에 맞는 별 들 입력 하는 반복문 작성
            for star in range(1, floor+1):
                # 조건 짝 수 층에는 2,4 번째에 별 입력 안함
                if (row+1) % 2 == 0 and star % 2 == 0:
                    print(" ", end="")
                else:
                    print("*", end="")
            print()
        # 1 번 다 끝나고 나면 띄어쓰기로 구분
        print()

    # 2번
    else:
        # 5층 반복할 반복문 작성
        for row in range(floor):
            # 층안에서 입력 할 값들 작성
            for star in range(floor):
                # 조건식 :  #해당 층 = 해당 별의 변수  ==> 빈공간 작성
                if row == star:
                    print(" ", end="")
                else:
                    print("*", end="")
            print()






row = 5 # 층 변수 

for value in range (2): 
# 층
    for floor in range (1,row+1) :
        # 별 원소
        for star in range(1,row+1) :
            # 별 뽑을 때 
            if value == 0 :
                if floor %2 != 0  or star %2 !=0 :
                    print("*",end="")
                # 아닐 때 
                else : 
                    print(" ",end="")
         
            else :       
                if floor!=star :
                    print("*",end="")
                else : 
                    print(" ",end="")
        print()  
    print()  