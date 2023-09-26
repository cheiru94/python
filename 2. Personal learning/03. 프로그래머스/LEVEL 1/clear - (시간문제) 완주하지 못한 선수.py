def solution(participant, completion):
    answer = ''

    # participant - completion = 완주 x 사람 
    for Index in range (len(completion)) :
       
        Element = completion[Index]

        participant.remove(Element) if completion[Index] in participant  else True    

    answer = ",".join(participant)    
    return answer

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])