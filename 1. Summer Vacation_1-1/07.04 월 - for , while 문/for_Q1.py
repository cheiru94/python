# 07.04 월
# 입력 받을 변수 작성
row = int(input("양의 정수를 입력 하세요 : "))
# 층 반복할 for 반복문 작성
for rowvalue in range(row):
    # 각층에 1,2,3,4,5 순으로 입력 값 반복적으로 입력
    # rowvalue 값에 따라 반복적으로 숫자 나열하기
    for value in range(rowvalue+1):
        # 반복적으로 가로로 숫자 나열
        print(value+1, end=" ")
    # 한 행이 끝 나고 나면 줄 띄워쓰기
    print()