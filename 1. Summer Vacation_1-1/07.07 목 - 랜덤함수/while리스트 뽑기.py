# 1 ~ 10 사이 난수 5개를 List에 저장 후
# 난수 값을 출력하라.
import random

myList = []

for value in range(5):
    myList.append(random.randint(1, 10))
    
for value in myList:
    print(value)
    
print()

index = 0

while index < len(myList):
    print(myList[index])
    index += 1