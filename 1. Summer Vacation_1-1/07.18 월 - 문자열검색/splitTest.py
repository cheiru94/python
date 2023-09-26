msg = "h   king  car a       ab  fmlkgj  "

list = []
word = ""


count = 0
for value in msg:
    # 단어 일 때
    if value.isalpha():
        word += value
        # 마지막 일 때
        if count == len(msg) - 1:
            list.append(word)
            word = ""
    # 공백일 때
    else:
        if len(word) >= 1:
            list.append(word)
        
        word = ""

    count += 1

print(list)