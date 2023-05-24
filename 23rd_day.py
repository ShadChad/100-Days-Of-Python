l = [3,45,64,45,64,23,456,1]

print(l)
l.append(7) #append adds the value from the end in lists
print(l)

l.sort() #sorts the items from asc
print(l)

l.sort(reverse=True) #sorts in desc order
print(l)

l.reverse() #reverse all the items from orginal list
print(l)

print(l.index(45)) #this method returns the index of the first occurance of the first index
print(l)

print(l.count(45)) #counts the number of time the value is stored in the list

m = l.copy() #it makes the copy of the lists, hence there will be no any change or modifactions in the orginal list doing so
m[0] = 0
print(l)
print(m)

m = l
m[0] = 0 #overwrites the value on given index
print(l)


l.insert(0,899) #it inserts the value on given index without affecting the any value on the lists
print(l)

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)


m = [900,1000,1100]
l.extend(m) #it extends the list m and add the value in orginal list at the end
print(l)

colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)


m = [700,556,767]
k = l + m #it merges
print(k)

