# 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거

def solution(arr):

    answer = []

    for Index in range (len(arr)) :
        
        # arr 요소들 뽑아 내기 
        Element = arr[Index]

    # 다른리스트에 없으면 넣기
    
    # 1. 앞 뒤 같을 때 추가  (2개이상 거르기 )
        if Element == arr[Index-1] : 
            # 겹치는 리스트 안에 요소가 없으면 더해라
            if Element not in answer :
                answer.append(Element)
            # elif Element in answer and  :

    # 2. 1개만 있을 경우 
        # if Element not in answer :
        else :
            answer.append(Element)
    return answer


print(solution([5,5,5,5,3,3,3,3,5,5,3])) 