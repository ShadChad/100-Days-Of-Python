def average(a,b):#required argument
    print("The average is", (a+b)/2)
    
    
average(2,4)
def average(a=9,b=1):#required argument
    print("The average is", (a+b)/2)
    
    
average()
average(7,5)#ignores the value given in args
average(b=3)#overwrites the value of b whil the value of a remain unchanged

def name(fname,mname='john',lname='whatson'):
    print('hello', fname,mname,lname)
    
name('amy')
name('amy','agrawal')#Overwrites
name('amy','agrawal','sharma')

def name1(fname,mname,lname):
    print('hello',fname,mname,lname)
    
name1('hari','prasad','koirala')

# def name2(fname,mname,lname):
#     print('hello',fname,mname,lname)
    
# name2('peter','quill')
#------------------will throw an error we should pass all the value for an args

def average1(*numbers):
    sum = 0
    print(type(numbers))
    for i in numbers:
        sum = sum + i
    print("average is",sum/len(numbers))
        
average1(5,6,7,8,9)

def name4(**name):
    print("hello",name['fname'],name['mname'],name['lname'])
    
name4(mname='buchhan',lname='barnes',fname='james')

def average2(*numbers):
    sum = 0
    print(type(numbers))
    for i in numbers:
        sum = sum + i
    # print("average is",sum/len(numbers))
    #return 7 will return 7 in c
    return sum/len(numbers) #--will only return none if we didnt passed the functions in variable and print the variable

    
c = average2(3,4,5,6,7)
print(c)






