#global and local variables

x = 4 #global variable
print(x)
 

def hello():
    # global x
    x = 5 #local variables
    print(f"the local variable is {x}")
    print("helo world")

hello()
print(f"the global variable is {x}")
#global and local variables

y = 4 #global variable
print(y)
 

def welcome():
    global y
    y = 5 #local variables
    print(f"the local variable is {y}")
    print("helo world")
    z = 10
  
welcome()
print(f"the global variable is {y}")
# print(z) #returns error because y is an llocal variable, hence cannot return it in global code