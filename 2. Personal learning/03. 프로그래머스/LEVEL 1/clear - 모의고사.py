def solution(answers):

    # 정답
    answer = []

    # 유저 정답 리스트 
    L_USER_1 = [ 1, 2, 3, 4, 5 ]
    L_USER_2 = [ 2, 1, 2, 3, 2, 4, 2, 5 ] 
    L_USER_3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 ]

    # 유저들 정답 수 
    User_1 = 0 
    User_2 = 0
    User_3 = 0
    Compare = [ ]   # 리스트에 담기

    # 정답 수만 큼 반복
    for Index in range (len(answers)) :

    # asnswer 길이에 따른 유저들 정답 수 증가
        if len(L_USER_1) < len(answers) or len(L_USER_2) < len(answers) or len(L_USER_3) < len(answers) : 
            L_USER_1 = L_USER_1 * len(answers) 
            L_USER_2 = L_USER_2 * len(answers) 
            L_USER_3 = L_USER_3 * len(answers)  

    # 유저들 정답수 체크
        # L_USER_1
        if answers[Index] == L_USER_1[Index] :
            User_1 += 1
        # L_USER_2 
        if answers[Index] == L_USER_2[Index] :
            User_2 += 1
        # L_USER_3 
        if answers[Index] == L_USER_3[Index] :
            User_3 += 1

# Compare에 User들 정답수 추가
    Compare.append(User_1) , Compare.append(User_2) , Compare.append(User_3)
    
    # 딕셔너리 만들기 => 유저들의 key , value 값 같이 저장 
    Compare_dic = { }

    # 딕셔너리에 추가
    for key,value in enumerate(Compare) :
        Compare_dic[key] = value

# ★ 정답 체크 ★  
    # 1. 3개의 값이 같을 때 
    if Compare[0] == Compare[1] == Compare[2] :
        Compare[0] = 1
        Compare[1] = 2
        Compare[2] = 3
        #  1 ,2 ,3 순으로 "answer에 저장"
        for Index in Compare :
            answer.append(Index)
            
    # 2. 1이상이 선택 될 때
    else : 
         # for 반복문으로 딕셔너리 안의 내용 하나씩 추출
        for Index in range(len(Compare_dic)) :
            # 조건 : value 값이 최대 값이면 새로운 
            if Compare_dic[Index] == max(Compare) and  Index+1 not in answer :
                answer.append(Index+1)
    return answer

print(solution([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
                



# def solution(participant, completion):
#     #딕셔너리안에 참가자들을 키로 만들어 넣어 준다
#     who={}
    
#     for value in participant:
#         if value not in who:
#             who[value]=1

#         else:
#             who[value]+=1

#     for value in completion:
#         who[value]-=1

#     loser=[key for key, value in who.items() if value > 0]
    
#     #교집합
#     answer = loser[0]
#     return answer