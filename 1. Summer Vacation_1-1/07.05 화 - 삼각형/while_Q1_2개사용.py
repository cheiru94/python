#양의 정수를 입력 받기
#양의 정수를 입력 하세요

# while 문을 범위에 맞게 조종할 변수 설정
row = 1
col = 1

# row 작동시킬 while 문 작성
while row <= 5 :
    # col 작동시킬 while 문 작성
    while col <= row :
        print(col , end=" ")
        # col 값 1씩 증가시켜 계속 반복시키기   
        col += 1
    # 하나의 while 이 종료 되면 띄워쓰기    
    print()
    # 리셋 -> 처음부터col 값 갱신
    col = 1
    # row 높이를 바꾼다 
    row += 1