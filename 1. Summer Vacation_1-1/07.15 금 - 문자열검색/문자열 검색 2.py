lineRange       =  int(input("입력 문자열의 줄(Line) 수를 입력하세요!"))    # 문자열 몇 개 입력받을지 횟수 정해주는 변수
inputValueList  =  []                                                     # 입력 받은 문자열에서 단어를 추출해 담아줄 리스트

for index in range(lineRange):                                            # 입력 받은 횟수만큼 문자열 받기
    inputValueList.append(input(str(index + 1) + "번째 라인의 문자열을 입력하세요. "))

line        = [0] * lineRange                       # 검색값이 있는 라인 담아줄 리스트 선언
searchCount = 0                                     # 검색횟수를 담아줄 변수 선언
searchValue = input("검색할 문자열을 입력하세요 : ")  # 검색할 문자열을 담아줄 변수

while not(searchCount):
    word        =  ""                                                                                       # 문자를 담아줄 변수 선언
    allWord     =  0                                                                                        # 전체 단어수를 카운트 해줄 변수 선언

    for index in range(len(inputValueList)):
        for charIndex in range(len(inputValueList[index]) - 1):
            
            if inputValueList[index][charIndex].isalpha():                                                  # 문자가 나오는 경우
                word += inputValueList[index][charIndex]                                                    # 문자를 변수에 담아주기
            
            # word 에 문자가 있고 다음 인덱스의 원소로 공백이 나오는 경우 or word에 문자가 있고 마지막 인덱스일 경우
            if word and inputValueList[index][charIndex + 1] == " " or word and charIndex == len(inputValueList[index]) - 2:  
                
                allWord += 1                                                                                # 전체 단어 수 카운트
                if inputValueList[index][charIndex + 1].isalpha():                                          # 마지막 원소가 문자라면 word에 더해주기
                    word += inputValueList[index][charIndex + 1]
                
                if word == searchValue:                                                                     # 검색된 단어와 같다면
                    searchCount += 1                                                                        # 검색 횟수 카운트
                    line[index] = index + 1                                                                 # 라인 담아주기
                word = ""                                                                                   # 문자 담는 변수 초기화
            
    if not(searchCount):
        searchValue = input("찾을 수가 없습니다. 검색 할 문자열을 입력하세요. ")

while 0 in line:    # 검색되지 않은 라인 삭제
    line.remove(0) 

print(searchValue + "를 찾았습니다.")
print("검색된 라인 수:", line)
print("검색된 횟수 :", searchCount)
print("총 단어 수 :", allWord)