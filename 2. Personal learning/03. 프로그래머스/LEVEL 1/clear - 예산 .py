#    d(부서)      budget      result
# [1,3,2,5,4]        9         	3


def solution(d, budget):
    answer = 0  # 더하기 한 횟수 
    Sum = 0     # 합계
   

    d.sort()

    # 부서안의 요소 합이 예산을 초과 하지 않음
    for Index in range(len(d)):
        Element = d[Index]
    # 조건식 element <= budget
        Sum += Element
        if Sum <= budget :
            answer += 1
     
    return answer


print(solution([2,2,3,3],10))