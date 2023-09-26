#  라인
for line in range (3) :  # 0 1 2 
    # 공백
    for blank in range (3-(line+1)) : # 2 1 0
        print(" ", end=" ")
    # 별
    for star in range (2*(line)+1) :
        print("*", end=" ")
    print()