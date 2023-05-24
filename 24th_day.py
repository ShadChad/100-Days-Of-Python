#tuples are immutable
#strings are immutable
#list are muttable


# tup = (1) #will print as an int
tup = (1,2,3,4,45,324,3435,'green','red') #if there's a single element inside a tuple, we should always give a comma after that so that the py intrepreter knows its the tuple  
tup[0:]
tup[:]   #__everything is same like list
tup[:5]
# tup[0] = 90 #we cannot add any values inside tuple, its fixed caannot be modified
print(type(tup),tup)
print(len(tup),"len")
print(tup[0])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[-1])


if 324 in tup:
    print("yes 342 is present in this tuple")
if 3434 in tup:
    print("yes it is")
else:
    print('no')
    
tup2 = tup[1:4] #this will create a new tuple holding the given indexed values
print(tup2)

for items in tup:
    print(items,end="-")
    
# colors = ('voilet','indigo','blue')
# rainbow = ('green','yellow','orange','red') -----tuple has no attribute extend
# colors.extend(rainbow)
# print(colors)
