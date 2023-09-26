import random

# 1 ~ 50 사이의 난수 25개 (N X N), 중복되지 않게
N = 5
NUM_OF_ELEMENTS = N * N
RAND_NUM_FROM = 1
RAND_NUM_TO = 50

# randNumList = []

# while len(randNumList) < NUM_OF_ELEMENTS:
#     num = random.randint(RAND_NUM_FROM, RAND_NUM_TO)    
    
#     if num not in randNumList:
#         randNumList.append(num)

randNumList = [21, 14, 11, 3, 16, 48, 31, 41, 47, 30, 5, 28, 17, 22, 8, 38, 34, 23, 20, 49, 32, 25, 37, 2, 43]

# 5 X 5 매트릭스 출력
for index in range(NUM_OF_ELEMENTS):
    print(randNumList[index], "\t", end="")
    
    if (index + 1) % 5 == 0:
        print()

# 열에 대한 최소, 최대, 중간 값 출력
for col in range(N):
    tempList = []
    for row in range(N):
        tempList.append(randNumList[row*N + col])
        
    tempList.sort()
    
    print(tempList[0], tempList[-1], tempList[N//2])

print()

# 행에 대한 최소, 최대, 중간 값 출력
for row in range(N):
    tempList = []
    for col in range(N):
        tempList.append(randNumList[row*N + col])
            
    tempList.sort()
        
    print(tempList[0], tempList[-1], tempList[N//2])

# 매트릭스 전체 원소에 최소, 최대, 중간 값 출력

randNumList.sort()
print(randNumList[0], randNumList[-1], randNumList[NUM_OF_ELEMENTS//2])