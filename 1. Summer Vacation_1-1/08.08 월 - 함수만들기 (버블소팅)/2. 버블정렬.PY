# 버블 정렬

alt = [6, 3 , 12 , 7 , 25 , 2 , 9 , 11]

for j in range(8) :
    for k in range(7) :
        if (alt[k] > alt[k+1]) :
            tmp = alt[k]
            alt[k] = alt[k+1]
            alt[k+1] = tmp
    
    print(alt)

# 비교 대상이 alt[k]와 alt[k+1]
# k 값의 범위는 선택정렬과 달리 0에서 6까지
# for k in range (7):
