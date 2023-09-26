# 리스트    
malist = enumerate(["i", "love", "you","betty"])

for Index, value in malist:
    print(Index, ":", value)
print()



techacademy = ['未経験転職', '初心者でも安心', '短期集中プログラミング']
for i, j in enumerate(techacademy):
  print('{0}:{1}'.format(i, j))




# 문자열 
malist = enumerate("재미있는 파이썬")
for Index, value in malist:
    print(Index, ":", value)
print()

# 튜플
data = enumerate({1, 2, 3})
for i, value in data:
    print(i, ":", value)
print()


# 딕셔너리
dict1 = {'이름': '한사람', '나이': 33}
data = enumerate(dict1)
for i, key in data:
    print(i, ":", key, dict1[key])
print()

######################################################

data = enumerate((1, 2, 3))
print(data, type(data))

for i, value in data:
    print(i, ":", value)
print()



######  딕셔너리에 값 추가 할떄 사용 가능
  

Compare = [ ]

Compare_dic = { }

for key,value in enumerate(Compare) :
    Compare_dic[key] = value