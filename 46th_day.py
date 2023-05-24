a = 4
b = '4'


print(a is b) # exact location of objects in memory
print(a == b) # checks value

z = [1,2,4,43]
x = [1,2,4,43]
print(z is x) #will return false because of differnt memory location ,since list are mutable, python assign them on diff mem
print(z==x) #value is same, hence will return true



c = 3
d = 3
print(c is d) #since the value is constant, python assigns all the values to the same memory location, or hence points to the mem location
print(c==d) #value is same, true


v=None
f=None
print(v is f) #returns True 
print(v==f) #true