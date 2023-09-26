# 07.04 월
#
# 층작성에 사용할 변수 작성
row = 5
# 전체로 적으로 총 3번 돌릴 반복문 작성
for fullcount in range(3):
# 층 돌릴 반복문 작성
    for rowvalue in range(row):
        # 층내에서 별 1개씩 찍을 반복문 작성
        for star in range(row):
            print("*", end="")
        # 한라인 끝나면 띄워쓰기 
        print()
    # 5 x 5 한번 끝나면 다음과 구분하기 위한 띄워쓰기 
    print()