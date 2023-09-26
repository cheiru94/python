# 홀수인 정수를 입력 받으시오 / int(input("몇 층 입력할래? :  "))
InputValue =  5
# 입력 받은 정수 반으로 나누기 
divided = InputValue//2 + 1
# 층만들 반복문 작성

for row in range (1,InputValue+1) :
    # 조건 : 
    # 上 처음 부터 반까지는 순차적으로 1씩증가
    if row <= divided :
        for star in range (row) :
            print ("*" , end="")
        print()                
    # 下 2 -> 1  순으로 1개씩 감소
    else :
        for star1 in range (InputValue-row+1) :
            print ("*" , end="")
        print() 