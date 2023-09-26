
# 계정 입력 받기 
account = input("아이디를 입력하세요 : ")
password = input("비밀번호를 입력하세요 : ")



#함수
def Account (ID,PASS) :

    user_account = {"betty":"1234" , "sexy":"0000" }
    account_list =  user_account.keys()
    password_list = user_account.values()
    

    if ID in user_account and  user_account[ID] == PASS :
        return " ♥ "+ ID + "님 로그인 환영합니다 ^^ ♥ "
    else :

        # 문제가 생길 시 
        if not ID in user_account or not PASS in user_account :   # 왜 not을 안 붙이면 안되는가?

            # id , pw 둘다 문제 
            if not ID in account_list and not PASS in password_list :               
                return " id 또는 pass 를 재확인 해주세요."
                
            # id 문제    
            elif not ID in user_account : 
                return "id를 확인해주세요"
            # pw 문제    
            elif not PASS in user_account : 
                return "pass를 확인해주세요"

# 매개변수 입력 부 
Home = Account (account,password)

print(Home)


