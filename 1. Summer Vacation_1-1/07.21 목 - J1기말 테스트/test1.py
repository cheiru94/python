# 5번 회전시킬 상수
COUNT = 5

# 합계 변수
SUM = 0


# 1.  for 반복문 -> 5번반복
for value in range (COUNT) : # 0 1 2 3 4
    # 2. 입력값 받기
    Inputvalue = int(input(str(value+1)+"번째 값 입력 : "))
    # 합계
    SUM += Inputvalue
    
# 출력부
print("합계 :" , SUM)
print("평균 :" , SUM/COUNT)