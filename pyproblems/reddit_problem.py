str1="This is string1"

str2="This is string2"

list1 = str1.split(' ')
list2 = str2.split(' ')
common = []

for i in list1:
    for j in list2:
        if i == j:
            common.append(i)

print(common)

