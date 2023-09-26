def solution(numbers):

    answer = 0  # sum 변수 

    # 0 ~ 9 모든 숫자  
    FULL_numbers = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]

    for Index in range(len(FULL_numbers)) :
        Num = FULL_numbers[Index]
        if Num not in numbers :
            answer += Num
    return answer

print(solution([5,8,4,0,6,7,9]))