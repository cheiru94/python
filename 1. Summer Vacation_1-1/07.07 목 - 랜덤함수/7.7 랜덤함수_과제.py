 # 랜덤 함수

# 1.  Clear   0000
#   1 ~ 20 사이의 양의 정수중 
#   난수 값 20 개 생성 후
#   List에 저장 
#----------------------------------------------------------------
# 2.
#   List 내 원소 값에 대한 
#   합계, 평균, 최대 값, 최소 값 출력  
#----------------------------------------------------------------
# 3. 
#   List 내 중복 값과 중복 횟수 정보 출력

# 4. 
#   구간 별 히스토그램 정보 출력


# < 1번 >

# random 함수를 쓰기위해 import 선언! 
import random
# List 공간 만들기
MyList = [ ]
# 1-1. 1~20 사이를 만들 반복문(for) 작성
for Value in range (20) :
# 1-2. 난수 값 무작위로 20개 생성
    ransuu=int(random.random() * 20) +1 
# 1-3.List 공간 만들기 
    MyList.append(ransuu)   # ex) MyList = [16, 15, 9, 9, 9,..... ]

# 출력문 :랜덤 값       
print("랜덤 값 : ")
# 반복해서 랜덤 값을 뽑을 
for RandomValue in range(len(MyList)) :
    result = MyList[RandomValue]
    print("\t ",result, " ", end="")
    if RandomValue == len(MyList)//2-1 :
        print ()

#----------------------------------------------------------------

#2 번 으로 가기전에 띄워 쓰기 
print()
# < 2번 >

# 반복 적으로 list 안에 있는 값들을 추출
# 最小 값 
Max =  MyList[RandomValue-1]
# 最大 값 
Min =  MyList[RandomValue-1]
# 합계 담을 변수 공간 
Sum = 0
for RandomValue in range(len(MyList)) :
    atai = MyList[RandomValue]
    Sum += atai
    # 最小
    if Min < MyList[RandomValue] :
       Min = Min
    else :
       Min = MyList[RandomValue]

    # 最大
    if Max >= MyList[RandomValue] :
       Max = Max 
    else :
       Max = MyList[RandomValue]
# for Value in MyList : 
    
#  2-1. 최소 값
print("최소 값\t:",Min)
#  2-2. 최대 값
print("최대 값\t:",Max)
#  2-3. 합계
print("합계\t:",Sum)
#  2-4. 평균
print("평균\t:",Sum/len(MyList))

#----------------------------------------------------------------

# < 3번 >

# 출력 단어 ->  중복 값   중복 회수
print("중복 값    중복 회수")

# 중복 횟수 측정 할 변수
count = 0
# 1. 리스트의 안의 요소들과 비교할 1~20까지의 고정 숫자 뽑기
for duplicated in range(len(MyList)) : 
    # 2. 1에서 뽑은 수로 리스트 안의 요소와 일치하는지 세기위한 반복문
    for element in MyList :
        # 조건식으로 비교  ->   고정값 , 요소값
        if duplicated == element :
            # 일치시 1씩 카운트 세기
            count += 1
    #  조건식 : 중복될 경우 해당 값과 중복 횟수 출력
    if count>= 2 :       
        print("  ",duplicated,"\t","     ",count)
    #첫번쨰 반복문이 다음으로 넘어갈시 카운트 초기화
    count = 0

#----------------------------------------------------------------

# < 4번 >
# 구간별 히스토그램 문구 출력
print("구간별 히스토그램")

# 해당 범위에 들어오면 카운트할 변수 생성
count1 = 0
count2 = 0
count3 = 0
count4 = 0
# 리스트 안의 원소를 하나씩 뽑을 반복문 작성 
# 조건식 작성 : 히스토그램 범위 설정 
for index in MyList :
    # 1  ~  5
    if 0 < index < 6:
        count1 += 1
    # 6  ~  10
    elif 5< index < 11:
        count2 += 1
    # 11  ~  15
    elif 10< index < 16:
        count3 += 1
    # 16 ~  20
    else :
        count4 += 1
print ("1 ~ 5   : ","*"*count1)
print ("6 ~ 10  : ","*"*count2)
print ("11 ~ 15 : ","*"*count3)
print ("16 ~ 20 : ","*"*count4)