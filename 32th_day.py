for i in range(5):
    print(i)

else:
    print('Sorry no i')

for i in []: #will directly go to else, because there is no value inside the given list
    print(i)
   
else:
    print('sorry no i')

for i in range(6):
    print(i)
    if i == 4:
        break #it wont execute the else statement because the loop is completed, but not the loop is broke 
else:
    print('Sorry no i')


i = 0
while i<7:
    print(i)
    i = i+1
    if i == 4:
        break #it wont execute the else statement because the loop is completed, but not the loop is broke 

else:
    print('sorry no i')

i = 0
while i<7:
    print(i)
    i = i+1
    # if i == 4:
    #     break #it wont execute the else statement because the loop is completed, but not the loop is broke 
else:
    print('sorry no i') #it will execute

for x in range(5):
    print("iteration no {} in for loop ".format(x+1))
else:
    print('else block in loop')
print('out of loop')