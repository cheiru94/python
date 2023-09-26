def solution(absolutes, signs):
    answer_list = [ ]
    answer = 0
    PLUS = 1
    MINUS = -1
        # 1. for 반복문 => Element 추출
    for Index in range (len(absolutes)):
        absolutes_Element = absolutes[Index]
        Bullin_Element    = signs[Index]    

    # 2. 조건식 => 
        # True 
        if Bullin_Element == True :
            result = absolutes_Element * PLUS
            answer_list.append(result)
         # False 
        else : 
            result = absolutes_Element * MINUS
            answer_list.append(result)
            
    answer = sum(answer_list)    
    
    
    return answer