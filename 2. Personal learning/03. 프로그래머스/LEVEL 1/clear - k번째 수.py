def solution(array, commands):
    answer = []
#   1. commands "개수" 만큼 반복                      
#   =>   1차 반복                   
    for Index in range(len(commands)) :   #x3         
#       2.commands "요소의 개수" 만큼 반복             
#       =>   2차 반복                       
        Container = array[commands[Index][0]-1:commands[Index][1]]
        Container.sort() 
        answer.append(Container[commands[Index][2]-1])
    return answer

#                      기준 값                 지정 범위로 자를 값
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))



# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer

# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
