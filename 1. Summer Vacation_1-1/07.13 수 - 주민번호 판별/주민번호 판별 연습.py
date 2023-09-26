#  주민등록번호 검사 알고리즘 

# 주민번호 13 자리 입력 받기 000000-0000000    
Number = input("주민번호 13 자리 입력 하세요 : ") # - 포함 14개


Sum = 0 # 곱하기 한 결과  더하는 변수
Checkcount = 2 # 체크수 변수


# 입력 받은 주민 번호를 하나찍 뽑기  
for Value in range (len(Number)-1):  # 문자인 "-" 때문에 범위에 -1 
    Element = Number[Value]
    # 유효한 번호 인지 판별  isdigit()
    if Element.isdigit():
        #   곱하기   =  Element * Checkcount 
        Kakezan =  int(Element) * Checkcount
    # 유효하지 않으면 다시 반복문으로     
    else :
        continue
# 주민번호       0 0 0 0 0 0 - 0 0 0 0 0 0 0
# 체크 수        2 3 4 5 6 7 - 8 9 2 3 4 5  
  
    # Sum 에다 지속해서 더하기 
    Sum += Kakezan

    # 체크수 9 넘어가면 다시 2로 맞추기
    if Checkcount >= 9 :
        Checkcount = 1
    # 반복문 한번 완료 하기 전 체크수 1씩 증가 
    if Element.isdigit():
        Checkcount += 1


# 유효한 주민번호
if (11-(Sum%11))%10 == int(Number[len(Number)-1]) :
    print("유효한 주민번호 입니다.")
# 유효하지 않은 주민번호  
else : 
    print("유효하지 않은 주민번호 입니다.")