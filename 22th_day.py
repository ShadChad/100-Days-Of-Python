marks= [3,5,6,7,8]
print(type(marks))
print(marks)

print(marks[0]) #will return the first value of the list
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[1:3])
print("-")
#------indexing
 #-----[0],[1],[2],[3],--[4]
lists = [3,4,5,'Aasish',True]
print(lists[3])

print(lists[-3])
print(lists[len(lists)-3])#-- will print out 5 from all the statements provided here
print(lists[5-3])
print(lists[2])



if 7 in lists:
    print('yes')
    #will print out no, hence there's no 7 in lists 
else:
    print('no')

if 5 in lists:
    print('yes')
    #will print out yes
else:
    print('no')
    
    
if 'Aasish' in lists:
    print('Aasish is there')
else:
    print('No he isnt')
    
    
if "Har" in 'Harry':
    print('yes yes')
else:
    print('no no')
    
print(marks)
print(marks[:])
print(marks[0:len(marks)])
print(marks[1:-1])
print(marks[1:5:2]) #The third parameter is jump index, what it does is it jumps the number of time which is passed in the third parameter
    
    
#----List Comprehension------
lst = [ i for i in range(10)]
print(lst)
lst0 = [i*i for i in range(10)]
print(lst0)
lst1 = [ i for i in range(10) if i%2==0]
print(lst1)

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])


#Example 1: Accepts items with the small letter “o” in the new list
names = ['milo','sarah','bruno','anastasia','tosa']
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)


#Accepts items which have more than 4 letters
names = ['milo','sarah','bruno','anastasia','tosa']
Len_4 = [item for item in names if len(item)>=5 ]
print(Len_4)





    


