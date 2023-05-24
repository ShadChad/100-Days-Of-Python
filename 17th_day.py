name = 'Ram Baran Acharya'
for i in name: #i can be any variable, and i is every character in string, every element in list, it is differnt for every iterable objects
    print(i)#will print out every characters of the string
    #print(i,end=" ")
    if(i=="B"):
        print("This is B")
        
        
colors = ['Red','green','blue','yellow']
for color in colors:
    print(color) #will print out the element
    for i in color:
        print(i) #willprint out the every character of element
        
        
for k in range(5): #will print out 0-5, which is 0, n-1
    print(k)
    
for k in range(1,15): #will print out 1-15, which is 2 tto n-1
    print(k+1)
    
for k in range(1,20001):
    print(k)
    
for k in range(1,300,2): #the third args is step, which basically add or steps up or just skips everytime according to given value
    print(k)

        