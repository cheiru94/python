def solution(n):
    answer = ""
    for index in range(n):
        if index %2==0:
            answer += "수"
        else:
            answer += "박"
    return answer
print(solution(3))