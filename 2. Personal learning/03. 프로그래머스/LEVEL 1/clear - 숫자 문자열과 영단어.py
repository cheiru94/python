# def solution(s):
#     answer = 0
#     return answer


def solution(s):
    Mydic = {'zero':0,    'one':1 ,   'two':2, 
            'three':3,   'four':4,   'five':5, 
            'six':6,     'seven':7,  'eight':8, 
            'nine':9} 

    Parsing =''     # 하나씩 넣어 판독할 변수
    answer = ''  # 단어로 인식하면 담기 
    
    #for 반복문으로 s 안에 있는 글자들 하나씩 나누기
    for Word in  s :
#   단어를 Parsing 에 하나씩 담기 
        if Word.isalpha() :
            Parsing += Word

        elif Word.isdigit() :
            answer += str(Word)

        if Parsing in Mydic.keys() :
            answer += str(Mydic[Parsing])
            Parsing = ''


    # separate
    
    return int(answer)