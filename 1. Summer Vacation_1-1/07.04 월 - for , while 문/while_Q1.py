InputValue = int(input("양의 정수를 입력 하세요 : "))
# 1씩 늘리게 만들 value 변수 선언
value = 0
# 문자로 입력 받아 저장 할 변수 공간 선언
litteral = ""
# 바뀐 문자 열을 다시 담아 저장할 변수 공간 선언
new_litteal = ""
# 반복 8미만
while value < InputValue:
    # 1씩 증가시켜 8까지 출력하도록 value에 +=1 설정 
    value += 1
    # 입력 받은 value 값을 문자열로 바꿔주기
    litteral = str(value)
    # 바꿔준 문자 열을 더하기
    new_litteal += litteral+" "
    # 출력
    print(new_litteal)