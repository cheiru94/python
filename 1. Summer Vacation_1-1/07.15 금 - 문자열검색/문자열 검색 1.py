lineRange       =  int(input("입력 문자열의 줄(Line) 수를 입력하세요!")) # 문자열 몇 개 입력받을지 횟수 정해주는 변수
inputValueList  =  []                                                  # 입력 받은 문자열에서 단어를 추출해 담아줄 리스트
allWord         =  0                                                   # 전체 단어수를 카운트 해줄 변수 선언

# 입력 받을 횟수만큼 반복 돌리기
for index in range(lineRange):
    inputValueList.append([])
    inputValue = input(str(index + 1) + "번째 라인의 문자열을 입력하세요. ")
    word = ""

# 입력 받은 값을 단어별로 정리하기
    for charIndex in range(len(inputValue)):
        if inputValue[charIndex] == " ":            # 공백인 경우
            if word:                                # word 안에 값이 있다면 단어로 추가
                inputValueList[index].append(word)
                allWord += 1
                word = ""

        else:                                       # 공백이 아닌 경우
            word += inputValue[charIndex]           # 값을 변수에 담아주기
    
        if charIndex == len(inputValue) - 1:        # 마지막 반복인 경우
            if word:                                # word 안에 값이 있다면 단어로 추가
                inputValueList[index].append(word)
                allWord += 1

# 라인, 검색횟수 특정하기
line        =   []            # 검색값이 있는 라인을 담아줄 리스트 선언
searchCount =   0             # 검색값이 얼마나 있는지 카운트할 변수 선언

# 검색값 입력받기
searchValue = input("검색할 문자열을 입력하세요 :")
while not(searchCount):
    # 단어 리스트의 원소 하나씩 확인
    for index in range(len(inputValueList)):
    
        if searchValue in inputValueList[index]:                        # 검색 값이 있다면
            line.append(index + 1)                                      # 해당 인덱스+1 만큼 라인리스트에 넣기

            for charIndex in range(len(inputValueList[index])):                # 단어들을 하나씩 찾는다.
                if inputValueList[index][charIndex] == searchValue:     # 검색값과 같은 값이 있다면 
                    searchCount += 1                                    # 카운트

    if not(searchCount):                                                # 값이 없다면 검색값 다시 받기
        searchValue = input("찾을 수가 없습니다. 검색 할 문자열을 입력하세요.")

# 값 출력하기
print(searchValue + "를 찾았습니다.")
print("검색된 라인 수:", line)
print("검색된 횟수 :", searchCount)
print("총 단어 수 :", allWord)