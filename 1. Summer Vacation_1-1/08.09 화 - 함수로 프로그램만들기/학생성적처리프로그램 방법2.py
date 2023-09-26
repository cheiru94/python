# 학생 성적  처리 프로그램 : 학생들의 성적을 키보드로부터 입력 받아 리스트에 저장하고 입력 값을 출력하는 프로그램을 함수를 이용하여 작성
student_num_list = []          # 학번 리스트 and 반복 횟수 리스트(len)
name_list        = []          # 이름 리스트
kor_list         = []          # 국어 리스트
eng_list         = []          # 영어 리스트
math_list        = []          # 수학 리스트
sum_list         = []          # 합계 리스트
avg_list         = []          # 평균 리스트
date_count       = 0           # 입력데이터 갯수를 나타내는 변수
all_sum          = 0           # 전체 합계
all_avg          = 0           # 전체 반복
# (1) 각 입력 값 생성 -> 입력 값 각 리스트에 저장
def input_value():
    student_num = input("학번을 입력하세요")
    student_num_list.append(int(student_num))
    name        = input("이름을 입력하세요")
    name_list.append(name)
    kor         = input("국어 성적을 입력하세요")
    kor_list.append(int(kor))
    eng         = input("영어 성적을 입력하세요")
    eng_list.append(int(eng))
    math        = input("수학 성적을 입력하세요")
    math_list.append(int(math))
# (2) 메뉴 선택란 생성 및 현 입력 데이터 갯수 및 전체 학생 평균 값 생성
def menu():
    print("=============================")
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력 순)")
    print("3. 프로그램 종료")
    print()  
    print("현 입력데이터 갯수:",date_count)
    print("전체 학생 평균 값 :",all_avg)
    print("=============================")
# (3) 메뉴 선택 
while True:
    menu() 
    num = int(input())
    date_count += 1
    # 1번 메뉴 선택 -> 학생 정보 입력
    if  num == 1:       
        input_value()
        # 합계 생성 
        for sum_index in range(len(student_num_list)):
            sum = kor_list[sum_index] + eng_list[sum_index] + math_list[sum_index]
            if sum not in sum_list:
                sum_list.append(sum)
        # 평균 생성
        for avg_index in range(len(student_num_list)):
            avg = sum / 3
            if avg not in avg_list:
                avg_list.append(avg)
        # 전체 학생 평균 
        for all_index in range(1):
            all_sum += sum
            all_avg = all_sum / 3 / len(student_num_list)
            print(all_avg)
    # 2번 메뉴 선택 -> 학생 목록 출력
    elif num == 2:       
        for index in range(len(student_num_list)):
            print("[id:",student_num_list[index],"name:",name_list[index],"kor:",kor_list[index],"eng:",eng_list[index],"math",math_list[index],"sum:",sum_list[index],"avg:",avg_list[index])
    # 3번 메뉴 선택 -> 프로그램 종료
    elif num == 3:   
        print("프로그램 종료")    
        break