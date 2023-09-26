def betty (argA,argB):
    Sum = argA+argB
    Mul = argA*argB
    return Sum , Mul

# 함수 출력
print(betty(2,3))  # 튜플로 반환  -> (5, 6)

print("---------")

a,b  = betty (2,3)
print(a,b)          # 일반적으로 반환 ->5 6