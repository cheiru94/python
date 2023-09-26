#     [3번, 1번, 2번, 3번]

def solution(nums):
    answer = 0
    HALF = len(nums) //2
    Select_List = [ ]
    for Index in range(len(nums)) :
        Element = nums[Index]
    # 조건식 : if ★ in nums          while len(Select_List) < HALF :
        if nums[Index] not in Select_List and len(Select_List) < HALF: 
            Select_List.append(Element)
    answer = len(Select_List)
    return answer

print(solution([3,3,3,2,2,2]))