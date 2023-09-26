# !! hello world, it is awesome day

# 특수 문자 =>  !   .   ,

myList = "!! hello world, it is awesome day."

# 단어 하나하나로 따개기 

# 리스트 작성
Reallist = []
word = ""

Blank = 0

# 단어 하나씩 추출
for value in myList :
# 만약에  문자면 저장 
    if value.isalpha() :
        word += value 

    # 문자가 아닌 경우
    else : 
        # 처음에 공백인지 아닌지 판별
        if len(word) >= 1:
            Reallist.append(word)
            word = ""
            Blank += 1
        word = ""

print(Reallist)


###########################################################################

Tokusyuu = 0   # 특수문자 변수
Words = 0      # 단어수
Alpha = 0      # 특수문자 제외 글자수

# myList 안의 요소들을 하나씩 분해
for value in myList :

# 1.  만약에 특수문자 [ !   .   , ] 이면
    if value == "!" or value == "." or value == "," :
        Tokusyuu += 1

# 2.  단어수 == " "  공백 개수
    if value == " " :
        Words+= 1

# 3. 특수문자 제외 글자수
    # 만약 value 가 
    # 3.1  "특수 문자"가 아니거나
    # 3.2  "공백"이  아니거나
    if value != "!" and value != "." and value != "," and value != " " :
        Alpha += 1


# 4. 출력부
print("특수문자 수 : ",Tokusyuu)
print("단어 수 : ",Words)
print("특수문자 제외 글자수 : ",Alpha)
print("찐 공백 : ",Blank)