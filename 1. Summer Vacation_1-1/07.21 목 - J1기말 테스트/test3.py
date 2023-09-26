# 만들 항목  1.층   2.공백   3.별

FLOOR = 5 # 층 상수


# 1.   층
for floor in range (FLOOR) :  # 0 1 2 3 4
# 2.  공백
    for Blank in range(floor) :
        print(" ", end="")
# 3.   별
    for Star in range (FLOOR-floor) :
        print("*", end="")
    # 4.  한 라인 출력 후 줄 바꾸기
    print()