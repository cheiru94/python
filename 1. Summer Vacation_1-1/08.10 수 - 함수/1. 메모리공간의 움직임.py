
#생명주기
def bar (argA) :
    argA = argA + 1
    foo(argA)
 
def foo (argB) :
    print(argB) 

value = 1   # 프로그램이 종료되면 value 까지 전체 stack 이 다 사라짐 

bar(value)

print(value )