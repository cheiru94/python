# 랜덤(random)함수  : 0과 1 사이의 임의 실수를 반환하는 함수
import random   # 랜덤함수를 사용하기위해 
                # 랜덤함수 모듈 import  <-필수

# <  ramdom 기초 개념  >
for value in range (100) :   # ->    0
 	# random.random()        -> 0 이상 1 미만의  실수값을 난수(임의의 값) 로 출력 
    # 0 이상 1미만의 실수를 반환
    # 0.0 ~ 0.999999999........
		print(random.random())

# 1~10 사이 양의 정수값을 랜덤 값으로 생성.
for value in range (20) :
		num = int(random.random() * 10 ) +1        #  *10 : 정수 값으로 설정 하기 위해      #  +1 : 1에서 10사이로 설정 하기 위해
		print(num)

# 총 20번 반복해서 30~50 까지의 숫자 무작위 추출
for value in range (20) :
        # randint(a, b)로 두 정수 a, b input에 대하여 a, b를 포함하여 a~b 사이에 있는 랜덤 정수 1개를 반환
        # 2개의 숫자 사이의 랜덤 정수를 리턴합니다. (2번째 인자로 넘어온 정수도 범위에 포함시킴)
		num = random.randint(30,50)      # 파이썬 랜덤 정수 추출 함수  / 
		print(num)

# 0 ~ 5 "실수" 랜덤 값
for value in range (10) :
    num = random.random() * 5
    print(num)

print("----------------------------------")

# 0 ~ 5 "정수" 랜덤 값
for value in range (10) :
    num = int(random.random() *5)
    print(num)