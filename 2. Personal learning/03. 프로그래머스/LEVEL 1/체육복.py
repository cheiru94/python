# n	  lost	       reserve	   return
# 5	  [2, 4]	  [1, 3, 5]	     5             5	,[2, 4]	,  [1, 3, 5]
# 5	  [2, 4]	  [3]	         4
# 6   [3,4,5]     [ 2,4]
# 5,  [ 2]      [2, 3]          4

def solution(n, lost, reserve):
    answer = 0  # 정답 
    
    Participant  = n - len(lost)  # 참가자
    
    #  reserve   
    for Index_reserve in range (len(reserve))  :
        ELEMENT_reserve = reserve[Index_reserve]
        # lost
        for Index_lost in range (len(lost))  :
            ELEMENT_lost = lost[Index_lost]
            # 조건식 :   ELEMENT_reserve 보다 1 크거나 , 1작으면 
            if ELEMENT_lost ==  ELEMENT_reserve-1 or ELEMENT_lost ==  ELEMENT_reserve+1 :
                # 참가자 증가 
                Participant += 1
                # 선택 된 거 제거 
                lost.remove(ELEMENT_lost)

         
        
    answer = Participant
    return answer


### for 문 2개 사용 해보기 
print(solution( 5	,[2, 4]	,  [1, 3, 5]	))