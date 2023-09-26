def solution(seoul):
    answer = ''
    KIM = 'Kim'
    for  Index in range(len(seoul)) :
        if  seoul[Index] == 'Kim' :
            answer = f'김서방은 {Index}에 있다'

    return answer

print(solution(["Jane", "Kim"]))