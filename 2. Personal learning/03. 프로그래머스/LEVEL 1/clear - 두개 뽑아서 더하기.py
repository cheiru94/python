#   numbers       	result
# [2,1,3,4,1]	[2,3,4,5,6,7]

def solution(numbers):

    # 합계 담을 리스트
    answer = []
   

    # 기준점으로 삼을 for 반복문
    for Std_Index in range (len(numbers)) :
        Axis = numbers[Std_Index]
    # 하나씩 확인할 for 반복문 
        for compare in range (len(numbers)) :
            Element = numbers[compare]
            if Std_Index != compare :
                Sum_Value = Axis + Element
                if Sum_Value not in answer :
                    answer.append(Sum_Value)
    answer.sort()

    return answer
print(solution([5,0,2,7]))