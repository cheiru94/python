# for value in range (5):
#     print("/", value / 2)
#     print("//", value // 2)
#     print("%", value % 2)  # 모둘러 == %


# 1. break 로 탈출!  (무조건 반복문만 탈출)
while True :
    num = int(input("정수를 입력 하세요"))

    if num == 1:
        #탈출
        break


# 2. 변수에 True Flase 넣어 활용

flag = True

while flag:
    num = int(input("정수를 입력 하세요"))
    if num == 1:
        flag = False