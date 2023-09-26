# 키보드로 부터 정수 값 입력 받기 
# 1이상의 값만 입력 , 0 이하의 값 입력시   "1이상 양수를 입력해주세요"
# 현재 입력 횟수 출력 후 키보드 입력 값 화면 출력
# 3의 배수("3의 배수 입니다") 또는 7의 배수("7의 배수 입니다")로 출력
# ‘20,000’ 입력 시 "이용해주셔서 감사합니다"

# (n) 씩 증감 시키는 변수 만들기 
Count = 1

# 스위치 만들기 : True 이면 On /  False 이면 Off  
flag = True
# while 반복 문으로 전체 감싸기
while flag : 
    # 키보드로 정수 값 입력 받기
    InputValue = int(input(str(Count)+"번째 입력 값은 = " ))

    # 조건식 만들기 

    # 종료 (플로우 컨트롤 순서 : 위에서 아래로 -> 짝수 판별 보다 위에 작성)
    # 20,000
    if InputValue == 20000 :
        print("이용해주셔서 감사합니다.")
        # 스위치 Off 
        flag = False
    # 짝수 -> InputValue % 2 == 0   
    elif InputValue % 2 == 0 :
        print("\t\t","짝수 입니다.")

    # 음수 -> InputValue < 0 
    elif InputValue < 0:
        print("1이상 양수를 입력해주세요")   
      
    # 홀수 -> else
    else : 
        print("\t\t"+"홀수 입니다.")
        if InputValue % 3 == 0 or InputValue %7 == 0 :
            print("\t\t"+str(InputValue)+"의 배수입니다")    
    # (n) 씩 증감 시키기
    Count += 1 
