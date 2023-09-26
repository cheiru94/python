def calculate(input):
    global bias, weight
    value = bias
    for i in range(2):
        value += weight[i] * input[i]

    if value >= 0:
        return 1.0
    else:
        return 0.0


def learning(x, y, l_rate, l_tiralNum):
    global bias, weight
    for l_count in range(l_tiralNum):
        sum_error = 0.0
        for row, target in zip(x, y):
            actualvalue = calculate(row)            # 입력값에 대한 결과 값 계산 : x * w
            error = target - actualvalue            # 오차 계산 : 목표 출력 값 - 신경망 출력 값

            bias = bias + error * l_rate            # 오차 값에 대한 바이어스 값 보정
            sum_error += error ** 2

            # ΔW = ε * (d-y(t))*w
            # w(t+1) = w(t) + ΔW
            for i in range(2):
                weight[i] = weight[i] + l_rate * error * row[i]
            print(row, actualvalue)
        print('트라이얼 횟수 = %d 학습률 = %.3f, 에러율 = %.3f' %
              (l_count+1, l_rate, sum_error))

    return weight


input_set = [[0, 0], [0, 1], [1, 0], [1, 1]]    # 학습 데이터 : 입력
answer_set = [0, 0, 0, 1]                       # 학습 데이터 : 정답

l_rate = 0.1         # 학습률(Learning rate)
epoch = 5            # 에포크(학습 횟수 : Training Data Set의 학습 횟수)

weight = [0.2, 0.1]      # 초기 웨이트 값 0,0 (OR [1,1] , AND [0.2,0.1])
bias = -0.3        # 초기 바이어 값 0.0 (OR [-0.3] , AND[-0.3])

# 학습 실행
print(learning(input_set, answer_set, l_rate, epoch))
