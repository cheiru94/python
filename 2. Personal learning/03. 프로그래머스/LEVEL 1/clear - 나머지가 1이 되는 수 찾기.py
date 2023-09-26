def solution(n):
    answer = 0
    
    X = 2
    while X < n :
        
        if n % X == 1 :
            answer = X
        
        X += 1

        if answer >= 1 :
            break 
    return answer
print(solution(12))