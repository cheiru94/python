
list_1 = [4, 5, 6]
list_2 = [8, 9, 10]

#merged_list = list_1 + list_2
# for value in merged_list:
#     print(value)

list_1.extend(list_2)

for value in list_1:
    print(value)