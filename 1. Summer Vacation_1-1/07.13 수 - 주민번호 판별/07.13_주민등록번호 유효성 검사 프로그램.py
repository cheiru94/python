# 주민등록번호 검사 알고리즘

# 주빈번호 13자리[문자열] (총14자리 - 포함) 입력 받기 
Number = (input("주민번호 13자리를 입력하세요 : "))
              #=>   주민번호  : 0 0 0 0 0 0   0 0 0 0 0 0 0   
Checked = 2   #=>   체크수    : 2 3 4 5 6 7 - 8 9 2 3 4 5 (12개)
Sum = 0       #=>   덧셈 계산 -> (주민번호[n] * 체크수) 전부 더하기 

# for 반복문으로 입력받은 문자 하나씩 꺼내기
for Index in range (len(Number)-1) :   
    Element = Number[Index]
# 숫자 인지 아닌지 판별
    if Element.isdigit():
    # 곱셈 계산 => 주민번호[n] * 체크수 
        Multiplication = int(Element) * Checked
        # 곱한것 Sum 에 계속 더하기
        Sum += Multiplication
        # 체크수 1씩 증가
        Checked += 1
# 숫자가 아니면 다시 체크        
    else :
        continue
    # 체크 2로 초기화 
    if Checked >= 10 :
        Checked = 2

# # 합계 중간 점검
# print(Sum) 

# 有効 
if (11-(Sum%11))%10 == int(Number[len(Number)-1]) :
    print("유효한 주민번호 입니다.")
# 不有効
else : 
    print("유효하지 않은 주민번호 입니다.")