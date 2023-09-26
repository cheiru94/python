# 랜덤 함수
# - >난수 발생기

import random

# # 0이상 1미만의 실수를 반환
# # 0.0 ~ 0.999999999.......
for value in range(10):
    print( random.randint(1, 10) )


# List: 자료 구조(Data Structure)
# Composite Datat Type : -> Array와 Linked List 
# Abstract Data Type : -> List
# 학생 100 명의 성적을 입력 받아 평균을 계산하시오.



# CRUD
#  - Create
#  - Read
#  - Update
#  - Delete


# Create
# 초기 값
# myList = [3, 4, 5, 2.0, True, "Test"]

# append : 제일 마지막 원소 뒤에 추가
# myList.append(20)

# insert : 지정된 위치에 추가
# myList.insert(1, 80)

# Read
myList = [3, 4, 5, 2.0, True, "Test"]

# 변수의 동작 모드는 두 가지
# GET, SET
# test = 2
# print(test) <- Get Mode
# test = 3 <- Set Mode

# [ ] 연산자를 이용합니다.
print( myList[1] )

myList[1] = 1000

for value in myList:
    print(value)
    
print("-"*10)

# while 문으로 리스트 원소를 하나씩 출력 
index = 0

while index < len(myList):
    print(myList[index])
    index += 1

print(myList[100])