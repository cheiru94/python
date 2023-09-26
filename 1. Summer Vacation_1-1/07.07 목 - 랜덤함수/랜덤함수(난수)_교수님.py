import random

# 난수 20개, 1~20 -> 리스트 저장
# myList = []

# for value in range(20):
#     myList.append(random.randint(1, 20))
    
# print(myList)

myList = [8, 15, 15, 5, 7, 1, 8, 10, 12, 8, 12, 12, 11, 20, 4, 17, 14, 9, 1, 20]     #<-  1. 이런식으로 변수로 미리 만들어 놓고  

min = 100                                                                            #<-   2. 해당 대는 값들 다 맞는지 확인 해 보기
max = 0
sum = 0
avg = 0.0
    
# 최소, 최대, 합계, 평균
for value in myList:   # [8, 15, 15, 5, 7, 1, 8, 10, 12, 8, 12, 12, 11, 20, 4, 17, 14, 9, 1, 20] 
    # 최소 - value < min :  value <-min
    if value < min:
        min = value
    
    # 최대 - value > max : value <- max
    if value > max :
        max = value
        
    # 합계
    sum += value
    
#평균
avg = sum / len(myList)

print("최소 : ",min,", ","최대 : ", max,",","합계 : ",sum,", ","평균 : ",avg)

############################################################################################

temp = []                            # 중복 값 체크하기 위한 리스트 : 새로운 리스트에 넣어 중복 구별 : 있으면 안 담음
duplicatedNum = [0] * len(myList)    # 중복 값 체크한 것 담는 리스트

# 중복값, 중복 회수
for value in myList:    # [8, 15, 15, 5, 7, 1, 8, 10, 12, 8, 12, 12, 11, 20, 4, 17, 14, 9, 1, 20] 
    # value in temp -> 중복값
    # duplicatedNum[value - 1] 1 증가
    if value in temp:                       # value : myList 안의 엘리먼트
        duplicatedNum[value - 1] += 1
    else:
    # 신규값 
    # temp에 신규 값 추가
        temp.append(value)
                        #    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18  19 
print(duplicatedNum)    #   [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1]     
index = 1 # 1~ 20 까지 증가시켜  1~20 까지 몇개가 중복 되어 있는지 1씩 증가 시키기 위한 증가 변수 
 
for value in duplicatedNum:
    if value >= 1:
        print(index, value + 1)
        
    index += 1

##############################################################################################

# 구간 별 히스토그램
numForInterval = [0]*4
print()
print("구간 별 히스토그램")
for value in myList:
    if 1<= value <= 5:
        numForInterval[0] += 1
    elif 6<= value <= 10:
        numForInterval[1] += 1
    elif 11<= value <= 15:
        numForInterval[2] += 1
    elif 16<= value <= 20:
        numForInterval[3] += 1
        
        
for value in numForInterval:
    print("*"*value)