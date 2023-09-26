# ★★★★★★stateIndex 사용하는 방법★★★★★★

# 검색어 : hello
# dhello dhellod hellod
# hello

# 입력 값
num = int(input("줄 수를 입력 하세요"))

textList = []

# 문장 입력
for index in range(num):
    textList.append(input(str(index + 1) + "번째 문장을 입력 하세요"))
    
# 검색어 입력
findWord = input("검색 단어를 입력 하세요")

for row in range(num):  # 0 1 2 
    stateIndex = 0    # 맞는지 기준으로 잡는 Index
    previousChar = ""
    nextChar = ""

    for col in range(len(textList[row])):
        # 다음 알파벳 설정    (3항 연산자)
        nextChar = "" if col == (len(textList[row]) - 1) else textList[row][col+1]
        print("prev : ", previousChar, " cur : ", textList[row][col], " next : ", nextChar)
     	
#     3항 연산자로 바꾸기 전 
	### 다음 알파벳 설정  ###
# 	if col == (len(textList[row]) - 1) :
# 		nextChar = "" 
# 	else :
# 		nextChar = textList[row][col+1]
# 	 print("prev : ", previousChar, " cur : ", textList[row][col], " next : ", nextChar)
                
        # 매칭 시작
        if textList[row][col] == findWord[stateIndex] and stateIndex == 0:
             stateIndex += 1
        # 매칭 중
        elif textList[row][col] == findWord[stateIndex]:
             # 값 검색 완료
             if stateIndex == (len(findWord) - 1):
                 print("검색, row, col : ", row, col)
                 stateIndex = 0
             # 매칭 계속
             else:
                 stateIndex += 1        
        # 매칭 실패
        else:
             stateIndex = 0
        # 이전 알파벳 설정    
        previousChar = textList[row][col]
print(textList)