# 전체적으로 감싸는 (2번 반복하게 하는 반복문) 변수 작성
full = 0
# row 으로 사용할 변수 작성
row = 1 
# col 으로 사용할 변수 작성
col = 1 


# 총 번  while 반복문 활성화
while full <2 : 
    
# 1. 첫 번째 반복문
    if full == 0 : 
        # 세로 작성할 반복문 작성 -> 5까지
        while row < 6 :
            # 가로 작성할 반복문 작성 -> 5까지
            while col  < 6 :
                # 조건문 작성
                # row가 2 이고 col 이 2 이면 공백 출력 아니면 *출력 
                if row % 2 == 0 and col % 2 == 0 :  
                    print(" " , end ="")
                else :
                    print("*" , end ="")
                # 반복문이 끝날 때 col 에 +=1 씩 추가    
                col += 1
            #한 층 다 출력 되면 띄워쓰기로 구분    
            print()
            # 다시 새로운 col 에서 col 값 초기화
            col = 1
            # row 에 1씩 증가
            row += 1
        print()    

# 2. 두 번째 반복문       
    else :
        # 세로 작성할 반복문 작성 
        
        while row < 6 :
            # 가로 작성할 반복문 작성 
            while col  < 6 :
                # 조건문 작성 : row == col 이면 공백 출력 아니면 별
                if row == col :
                    print(" ", end = "")
                else : 
                    print("*", end = "")
                col += 1
            # 하나의 반복문 끝나면 띄워쓰기 
            print()
            # row 1씩 증가
            row += 1
            # col 초기화
            col = 1
    # 한번 전체 반복문이 끝나면 한번더 반복하게 1씩 증가
    full += 1
    # row 값 초기화로 다음 반복문에서도 활용 하능
    row = 1