marks = [1,45,23,5,325,89,98] 
index = 0
for i in marks:
    print(i)
    if index == 3:
        print("kush awesome")
    index += 1


for index, mark in enumerate(marks):
    # print(index)
    print(mark)
    if(index==3):
        print('nets')

fruits = ['apple','banana','mango']
for index,fruit in enumerate(fruits):
    print(index,fruit)

fruits = ['apple','banana','pineapple']
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)


fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')

colors = ('red','green','blue')
for index,color in enumerate(colors):
    print(f"{index+1}:{color}")

s = 'hello'
for index, char in enumerate(s,start=3):
    print(index,char)