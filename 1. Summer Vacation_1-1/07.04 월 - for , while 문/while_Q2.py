#전체 적으로 반복 시킬 변수 공간 선언 
TotalMatrix = 0
# 가로 줄 반복시킬 변수 공간 선언 
RowMatrix = 1
# 세로 줄 반복시킬 변수 공간 선언 
ColMatrix = 1

# 총 3개의 5x5 Matrix를 만들기 위해 
while TotalMatrix < 3 :
    #가로 줄 반복시킬 while 반복문 작성 
    while RowMatrix < 6 :
        #세로 줄 반복시킬 while 반복문 작성
        while ColMatrix < 6 : 
        # * 출력
            print("*" , end="")
        # ColMatrix += 1 로 1씩 증가
            ColMatrix += 1 
        # 세로 줄 다 찍고 나면 띄워쓰기 print()
        print()
    # ColMatrix 다시 1로 초기화
        ColMatrix = 1
    # RowMatrix += 1 로 1씩 증가
        RowMatrix += 1
    # 마지막 5x5 를 제외한 나머지는 반복문이 한번 종료 되면 띄워쓰기 사용    
    if TotalMatrix < 2 :
        print()
    # RowMatrix  다시 초기화 
    RowMatrix = 1
    # 전체적으로 반복될 TotalMatrix를 1씩 증가 
    TotalMatrix += 1 





# while 문 1개
# # while 문을 해당 범위까지 실행 시킬 변수 설정
# Matrix = 1

# # while 반복문 작성
# while Matrix < 76 :
#     print("*", end="")
# # 조건문으로  % 5 == 0 이면 띄워쓰기
#     if Matrix % 5 == 0 :
#         print()
# #  조건문으로 5 x 5 단이 끝나면 띄워쓰기        
#     if Matrix   == 25 or Matrix   == 50 :
#         print()
# # 지속적으로 Matrix 값을 26에 근접하게 +=1 씩 증가 
#     Matrix += 1