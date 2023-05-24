list1 = [1,2,4]
list2 = [1,3,4]
newl =[]

for i in range(len(list1)):
    newl.append(list1[i])
for j in range(len(list2)):
    newl.append(list2[j])

newl.sort()
print(newl)