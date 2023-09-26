import random
# List 공간 만들기
MyList = [ ]
# 1-1. 1~20 사이를 만들 반복문(for) 작성
for Value in range (20) :
# 1-2. 난수 값 무작위로 20개 생성
    ransuu=int(random.random() * 20) +1 
# 1-3.List 공간 만들기 
    MyList.append(ransuu)   # ex) MyList = [16, 15, 9, 9, 9,..... ]



print(MyList)