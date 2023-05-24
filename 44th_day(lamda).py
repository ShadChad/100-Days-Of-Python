# def double(x):
#     return x * 2
#lamda can be useful for short and one liner statments
#a mini function

def appl(fx,value):
    return 6 + fx(value) #a function having an fucntions args

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y: (x+y)/2
avg1 = lambda x,y,z: (x+y+z)/2





print(double(5))
print(cube(5))
print(avg(3,5))
print(avg1(1,2,3))
print(appl(cube,2))
#better soln
print(appl(lambda x: x*x*x,2))