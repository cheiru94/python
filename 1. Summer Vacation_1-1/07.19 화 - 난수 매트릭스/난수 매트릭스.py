import random

MyList = []         # 무작위로 받는 리스트
SortingList = []    # 정렬 리스트

# 2차원 리스트
row_List = [[],[],[],[],[]]   # [ [0] , [1] , [2] , [3] , [4] ]   -> 5개


# 1. while 로 같은거 안들어 오게 계속 무한 반복 
while len(MyList)< 25 :    # 0 ~24 개
    # 1,50 사이 수를 무작위로 돌리기
    Element_1 = random.randint(1,50) 
    # 리스트안에 요소가 안들어 있으면 넣기     
    if not Element_1 in MyList :
        MyList.append(Element_1)
#################################################

# 2. 1,50사이 순서대로 크기 잡아가면서 정렬
# == MyList.sort()
for index in range (1,50+1) :
    if index in MyList :
        SortingList.append(index)
#################################################

# 3. 화면 출력용   5 X 5
for value in range (len(SortingList)) :
    # 원소 추출
    Element_2 = SortingList[value]

    print(Element_2, "\t", end= "" )
    # 띄워쓰기
    if (value+1) %5 == 0 :
        print()
#################################################

# 4. 2차원 리스트 
Count = 0  # 전체 카운트
Sorting_count = 0 # 솔팅 카운트

# 리스트 안에 리스트가 5개 까지 반복
while Count < len(SortingList) :
    # 요소 뽑기
    row_List[Sorting_count].append(SortingList[Count])
    if len(row_List[Sorting_count]) == 5 :
        Sorting_count += 1
    Count += 1


# 5. 출력부

# 5.1 열 
print()
print("열")

# 최소 값
print("최소값","\t",end="" )
for index in range (len(row_List[0])) :
    print(row_List[0][index],"\t" , end="")
print()

#최대 값
print("최대값","\t",end="" )
for index in range (len(row_List[4])) :
    print(row_List[4][index],"\t" , end="")
print()  

#  중간 값
print("중간값","\t",end="" )
for index in range (len(row_List[4])) :
    print(row_List[len(row_List)//2][index],"\t" , end="")
print()

# 5.2 행
print()
print("행")
print("최소값", "\t\t","최대값", "\t","중간값")


# 2차원 리스트  ( 5 X 5 를 행,열 로 활용 ) 
for row in range (len(row_List)) :       # 0 1 2 3 4
    for col in range (len(row_List)) :   # 0 1 2 3 4
        # 최소값
        if col == 0 :
            print (row_List[row][col],"\t\t",end="   ") 
        # 최대 값
        elif col  == 2 :  
            # 숫자 조절 
            col = 4  
            print (row_List[row][col],"\t\t",end="   ")                                                        
        # 중간 값
        elif col == len(row_List)-1 :
            # 숫자 조절
            col = 2
            print (row_List[row][col],"\t\t",end="   ") 
    print()

# 5.3 전체
print()    
print("最小値 : ",SortingList[0])
print("中間値 : ",SortingList[12])
print("最大値 : ",SortingList[len(SortingList)-1])