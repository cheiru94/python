# n 개의 정수를 입력 받아 오름 차순으로 정렬

# < 1 >
#  입력 정수 갯수
InpitNum = int(input("정수 갯수를 입력 하세요 : "))
# 입력 값 리스트
Container = []
# 키보드로 부터 N개의 정수를 입력 받아 리스트에 저장
for value in range (InpitNum) :
    Element = input(f"{value+1}번째 정수를 입력 하세요 : ")
    Container.append(Element)

##########################################################

# < 2 >
# 리스트에 저장된 정수 값을 오름 차순으로 정렬

# 전체적으로는 두개를 비교
# 1. 반복문 : 처음 값 지정     InpitNum = 4
for Front_Num in range ( InpitNum-1 ) :   # 4 ->  0 1 2 3
#   2. 반복문 : 
    for Back_Num in range ( InpitNum - Front_Num -1 ) :
        #  조건문 : 만약 Front_Num > Back_Num 라면 
        if Container[Front_Num] > Container[Back_Num] :
            Cup = Container[Front_Num]
            Container[Front_Num] = Container[Back_Num]
            Container[Back_Num] = Cup
print(Container)

# 리스트 값 출력




# 전체적으로는 두개를 비교
# 1. 반복문 : 처음 값 지정
for Front_Num in range ( len(Container)-1 ) :   # 4 ->  0 1 2 3
#   2. 반복문 : 
    for Back_Num in range (Front_Num+1 , len(Container) ) :
        #  조건문 : 만약 Front_Num > Back_Num 라면 
        if Container[Front_Num] > Container[Back_Num] :
            Cup = Container[Front_Num]
            Container[Front_Num] = Container[Back_Num]
            Container[Back_Num] = Cup
print(Container)

# 리스트 값 출력