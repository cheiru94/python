# while 문을 이용한 삼각형 만들기
#   *
#   **
#   ***     기준으로 잡고 나누기 
#   **
#   *

# 층만들 변수   /  int(input("몇층 : "))
floor =  5
# 층을 반으로 나누기 , 층의 반 값 
divided = floor//2 + 1   # 3
# while문을 조종할 변수 작성   1 , 2
# 1. 가로
row = 1 
# 2. 세로
col = 1

# 세로 줄 만들 while 문 작성 ( 해당 범위 설정)
while row <= floor :    # floor = 층 = 5
    # 조건식 작성 :  if - else
    if row <= divided :  # 가로<=divided  
        while col <= row :
            print("*" , end ="")
            # col 1 씩 증가시켜 원하는 범위까지 증가
            col += 1
        print()
        # 가로 while 문이 끝나면 띄워쓰기 , print()
        
        col = 1
        # 반복문을 증감시킬 장치 만들기 , += 1
        row += 1
    # 가로<=divided 가 아닐때      
    else :  # 가로 줄 만들 while 문 작성 ( 해당 범위 설정)
        while floor >= row  :
            print("*" , end ="")
            row+= 1
        print()
        # if row == 6 :
        #     print("*") 