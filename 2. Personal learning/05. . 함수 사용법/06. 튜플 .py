# 괄호 안 넣어도 "튜플"로 인식한다 
a = 10,20,"betty","of","the","best"
print(type(a))

b = (123,435,565,"grgre")
print(type(b))


# 리스트 처럼 이렇게도 사용 가능  (선언)
(arg1,arg2) = 10, 20
print(arg1,arg2)

    # 역시 ( ) 없이 사용 가능
arg1,arg2 = 10, 20
print(arg1,arg2)


#######  값 교환하기 #################
arg1,arg2 = arg2,arg1
print(arg1,arg2)


# 여러개의 값 리턴하기  (튜플사용)

def test() :
    return (10 , 20)

a , b = test( )

print("a :",a)
print("b :",b)