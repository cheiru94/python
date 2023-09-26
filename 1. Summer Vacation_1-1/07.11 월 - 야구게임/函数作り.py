# 정의 할 함수 만들기 (이름)

        # 횟수,랜덤범위, 
def betty (entire,kara,made,name) :
    name = []
    import random
    while len(name) <entire :
        element = random.randint(kara,made)   
        if element not in name :
            name.append(element)
       
    return name
print(betty(3,1,9,"myList"))