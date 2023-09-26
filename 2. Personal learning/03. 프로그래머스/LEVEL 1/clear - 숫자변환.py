#       <key>            <value>

#         s	             result
# "one4seveneight"	     1478
# "23four5six7"	         234567
# "2three45sixseven"	     234567
# "123"	                 123


# 0 ~ 9 영어 리스트 만들기 



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
    
    return answer
print(solution('2three45sixseven'))


# 숫자 입력 받기 (s)   / 길이 : 1 ~ 50   / s가  zero 또는 0 은 xxx