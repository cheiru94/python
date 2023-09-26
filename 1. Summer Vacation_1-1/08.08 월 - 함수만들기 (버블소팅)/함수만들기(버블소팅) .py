# < 1 >
# 키보드로 부터 N개의 정수를 입력 받아 리스트에 저장

def InputValueCreater (InputNum) :
#  입력 정수 갯수
    InputNum = int(input("정수 갯수를 입력 하세요 : "))
    # 입력 값 리스트
    ContainerOfList = []
    # 키보드로 부터 N개의 정수를 입력 받아 리스트에 저장
    for value in range (InputNum) :
        Element = input(f"{value+1}번째 정수를 입력 하세요 : ")
        ContainerOfList.append(Element)
    
    return ContainerOfList


# < 2 >
# 리스트에 저장된 정수 값을 오름 차순으로 정렬
def BubbleSorting (ArgValue,ascend = True) :
    # 전체적으로는 두개를 비교
    # 1. 반복문 : 처음 값 지정
    for Front_Num in range ( len(ArgValue)-1 ) :   # 4 ->  0 1 2 3
    #   2. 반복문 :   
        for Back_Num in range (Front_Num+1 , len(ArgValue) ) :
            #  조건문 : 만약 Front_Num > Back_Num 라면 
            if ArgValue[Front_Num] > ArgValue[Back_Num] :
                Cup = ArgValue[Front_Num]
                ArgValue[Front_Num] = ArgValue[Back_Num]
                ArgValue[Back_Num] = Cup
    return ArgValue



mylist = InputValueCreater(4)

BubbleSorting(mylist)

print(mylist)