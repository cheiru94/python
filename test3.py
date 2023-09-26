  

from tkinter import N


Switch = True

while Switch :
    print("--------------------------------")
    print("1. 구구단출력")
    print("2. 프로그램 종료")
    print("--------------------------------")

    InputNum = int(input(""))

    if  not 1<=InputNum<=2  : 
        print("잘못 입력 하셨습니다. 다시 입력하세요")  
        continue

    if  InputNum == 2 :
            break
    
    while True :
        dan = int(input("출력할 구구단을 입력 하세요. 구구단은 2~9 사이 입력"))

        if 1 < dan < 10 :
            
            for num in range (1,9+1):
                print(dan,"X",num,"=",dan*num)
        else:
            print("2~9 사이 정수를 입력해주세요")
            continue
        break
print("이용해 주셔서 감사합니다.")