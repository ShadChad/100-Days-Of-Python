#-------Magic Dunder Methods in python

class Employee:
    name = "Harry"
    # lene = len(name)
    def __len__(self):
        i = 0
        for c in self.name:
            i+= 1
        return i




e = Employee()
print(e.name)
# print(e.lene)
print(len(e)) #i created a method with ___(dunder) but called without it,
# well that's known as magic methods

class Employee1:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def __len__(self):
        i = 0
        for a in self.name:
            i+= 1
        return i
    
    def __str__(self):
        print(f"the name of the employee is {self.name} and his age is {self.age}--str")
    
    def __repr__(self) -> str:
        print(f"the name of the employee is {self.name} and his age is {self.age}")
    
    def __call__(self):
        print("hey i am good")

    
e1 = Employee1('Kush',19)
print(len(e1))
# print(str(e1))
# print(repr(e))
e1()


class Worker:
    def __init__(self,fname,lname,salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname +'@gmail.com'

    def fullname(self):
        return 'Employee :{} {}'.format(self.fname,self.lname)
    
    def __add__(self,other):
        return self.salary + other.salary
    
    def __repr__(self) -> str:
        return 'Employee: {} {} {}'.format(self.fname,self.lname,self.salary)
    
    def __str__(self) -> str:
        return '{} {}'.format(self.fullname(), self.email)
    
    def __len__(self):
        return len(self.fullname())
    
    
    
a = Worker('kush','sharma',18000)
b = Worker('aasish','sapkota',20000)
c = Worker('riti','sharma',90000)
print(a.fullname())
print(a.email)
print(int.__add__(1,2)) #everything in python is object
print(a+b) #calls the __add__ method, we created a method up in the class to add the salary
print(a) #takes str always #goes up look for the method, here its repr, returns it, 
#we can also print individualy repr and str

print(repr(a))
print(str(a))

print(a.__repr__()) #this is how the method is called

print(len(a)) #prints of the len of fullname, looks for the methhod and executes it







        
    

    



