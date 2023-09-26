########## 게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성

# random 호출
import random
# 필요한 변수들 선언
answer   =   []         # 답을 담아줄 변수

# 리스트에 3가지 값이 중복이 되지 않도록 출력
while len(answer) < 3 :
    answerValue = random.randint(1,9)
    # 정답 리스트 안에 값이 없는 경우만 넣어 주기
    if answerValue not in answer:
        answer.append(answerValue)

########## 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력

# 필요한 변수 선언
try_count       =   1   # 횟수 카운트 변수
out_count       =   0   # 아웃 카운트 변수

while True:
    # 시도횟수 출력
    print("시도횟수 :", try_count)
    # 정수 3개 입력받기
    inputValue      =   [int(input("정수를 입력하세요 \n")) for value in range(3)]

    # 필요한 변수들 만들기
    strike_count    =   0   # 스트라이크 카운트
    ball_count      =   0   # 볼 카운트

    ##### 아웃 또는 볼 값 찾기
    for index in range(3):
        if inputValue[index] == answer[index]:
            # 스트라이크 카운트
            strike_count += 1
        elif inputValue[index] in answer:
            # 볼 카운트
            ball_count   += 1

    # 아웃 또는 볼, 스트라이크 카운트 출력
    if strike_count == 0 and ball_count == 0:
        out_count += 1
        print(out_count,"Out")
    else:
        print("Strike : ", strike_count, " Ball : ", ball_count)

    # 한 번 반복이 끝나면 시도횟수 카운트
    try_count += 1

    ##### 종료하는 경우
    # 종료 안내문 출력
    # – 시도 횟수 >= 5
    if try_count     >=  5 : 
        print("시도횟수 초과")
        print("아까비 졌네용")
        print("정답은", answer[0], answer[1], answer[2], "이에요")
        break
    # – Strike out == 2
    if out_count     >=  2 :
        print("아웃횟수 초과")
        print("아까비 졌네용")
        print("정답은", answer[0], answer[1], answer[2], "이에요")
        break
    # - 3 Strike
    if strike_count  ==  3 :
        print("이겼어요 축하해요")
        break