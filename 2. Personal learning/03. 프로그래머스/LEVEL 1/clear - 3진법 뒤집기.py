def solution(n):
    answer = 0
     
    THREE = 3  # 3 진수 변수

    Mylist = [ ]  # 나머지 담을 리스트 

    if n > 3 :
        for value in range (n//THREE) :

            # 3보다 작아 나눌수 없으면 종료
            if n < THREE :
                Mylist.append(n)
                break

            Rrest = n % THREE   # 나머지
            n = n // THREE      # 몫

            Mylist.append(Rrest)
    else : 
        Mylist.append(n)
    # 역 솔팅
    Mylist.reverse()
    

    # 3진수 로 계산
    for Index in range(len(Mylist)) :
        result = (3**Index) * Mylist[Index]
        answer+= result
    
    return answer

    

print(solution(4))    	