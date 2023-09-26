# 소수점 조정
import math

# 정보담을 리스트 (학생 정보 확인용)
Info_List  = []           # 개인 정보를 2차원 리스트에 저장  

# 각 출력 내용 리스트 (각 성적값 확인용)
IdOfStudent_List = []
Name_List        = [] 
Kor_List         = []
Eng_List         = []
Math_List        = []

# 변수 
Score_Count = 1          # 성적개수
Sum        = 0           # 총합

#------------------------------------------------------------------------------------------------------------------------------------

# 출력문
def Guidance () :
    Avg =  Sum / Score_Count  # 평균 
    print("===========================")
    print(" 1. 학생 성적 입력")
    print(" 2. 학생 목록 출력 (입력순)")
    print(" 3. 프로그램 종료")
    print()
    print("현 입력데이터 갯수 : " ,len(Info_List))
    print("전체 학생 평균 값 : ", round(Avg,2))
    print("===========================")

# 
def OutputWord (Word) :
    input(f'{Word}을 입력하세요 : ')
                                                               

# 전체 반복문                                                                 
while True :                                                                 
    # 안내문 호출                                                                 
    Guidance ()                                                                 
                                                                 
    if len(Info_List) <= 0:                                                                 
        Score_Count = 0                                                                 
                                                                 
    # 선택문 출력                                                                  
    Input_Num = int(input("1 ~ 3 번중 하나를 선택하시오 : "))                                                                 
                                                                     
    ##### 1. 인 경우 ####                                                                 
    if Input_Num == 1 :                                                                 
                                                                 
        Info_List.append([])                                                                 

        for Index in range (Input_Num) :
            # 입력 받을 내용   1)학번 2)이름 3)국어 성적 4)영어 성적 5)수학 성적 
            # 인풋 값 각각의 리스트에 저장 
            IdOfStudent = OutputWord ("학번")
            Info_List[len(Info_List)-1].append(IdOfStudent)
            IdOfStudent_List.append(IdOfStudent)

            Name = OutputWord ("이름 성적")
            Info_List[len(Info_List)-1].append(Name)
            Name_List.append(Name)

            Kor = int(OutputWord ("국어 성적"))         
            Info_List[len(Info_List)-1].append(Kor)
            Kor_List.append(Kor)

            Eng = int(OutputWord ("영어 성적"))
            Info_List[len(Info_List)-1].append(Eng)
            Eng_List.append(Eng)

            Math = int(OutputWord ("수학 성적"))
            Info_List[len(Info_List)-1].append(Math)
            Math_List.append(Math)

        # 입력 받은 성적값 변수에 저장 
        for Index_Score in range( 2 , 4+1 ) :
            # 국어
            if Index_Score == 2 :
                Kor = Info_List[len(Info_List)-1][Index_Score]
                Score_Count += 1

            # 영어
            elif Index_Score == 3 :
                Eng = Info_List[len(Info_List)-1][Index_Score]
                Score_Count += 1

            # 수학    
            else :
                Math = Info_List[len(Info_List)-1][Index_Score]
                Score_Count += 1

        # 합계에 넣기            
        Score_Subject = Kor + Eng + Math
        Sum += Score_Subject
        continue

    ##### 2. 인 경우 ####
    elif Input_Num == 2 :

        for Index in range (len(Info_List)) : 
            print(["id : " ,IdOfStudent_List[Index], "name : ",Name_List[Index] , 
                  "Kor : ",Kor_List[Index] , "Eng : ", Eng_List[Index] , "Math : ",Math_List[Index] ,
                  "Sum : ", (Kor_List[Index] + Eng_List[Index] + Math_List[Index]), "Avg : ", round(((Kor_List[Index] + Eng_List[Index] + Math_List[Index])/3),2)])
 
    ##### 3. 인 경우 ####
    else :
        print('시스템 종료')
        break
