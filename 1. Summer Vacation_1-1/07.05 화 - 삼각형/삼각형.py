# 반복문 사용해서 뽑기

# 홀수의 정수 값 입력 받기
# 층수 변수 만들기
num = int(input("홀수의 정수 값 입력 : "))
# 반으로 쪼갤 것
median = num // 2 + 1 

# 반을 기준으로 
# 층수 만들 for 반복문 작성 
for row in range (1,num+1) :
# 반 이하까지는 점점 늘이기
    if row <= median :
        # range 범위를 row 와 동일하게 적용 = 층과 같이 별 출력
        for star in range (row) :  # 1, 2, 3,     
                print("*", end="")
        print() 
# 반 이상으로는 점점 줄이기        
    else :
        # range 범위 num+1-row 으로 적용 = 별 하나씩 감소
        for star in range (num+1-row) :  # 1, 2, 3,     
            print("*", end="")
        print()
        
