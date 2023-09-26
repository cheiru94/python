# 리스트에서 가장 작은 수 찾기 

#index 0  1   2    3   4    5   6    7
alt = [6, 3 , 12 , 7 , 25 , 2 , 9 , 11]

min = 0    # 최솟값 변수

# Index 는 뒤에 있는 값  / ★가작 작은 값을 갖고있는 인덱스를 보관★
for Index in range (1,8) :  #  1    2   3   4   5   6   7
    if alt[min] > alt[Index] :
        min = Index

# (~ 번째 인덱스, 최솟값)
print(min, alt[min])

######################################################

# 가장 작은 수 반복 하기 
alt = [6, 3 , 12 , 7 , 25 , 2 , 9 , 11]

# 리스트 수 만큼 반복
for front in range (8) :
    min = front
    for back in range(front+1,8) :
        if alt[min] > alt[back] :
            min = back
