def solution(a, b):
    answer = 0

    # 1. for
    for Index in range(len(a)) :
        answer += a[Index]*b[Index]

    return answer

print(solution([-1,0,1]	,[1,0,-1]))