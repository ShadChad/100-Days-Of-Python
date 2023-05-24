#access Modifiers
#----->Public,private,protected

#in general programming langauge--
#public = can be accessed outside the class
#private = can not be accessed outside
#protected = can be accessed inside the class and and subclass

#but every variable is public in python

#public access modifiers
class Employee:
    def __init__(self) -> None:
        self.name = "harry"


a = Employee()
print(a.name)

#private acceess modifers
# (__) this method wwill create a private variable
class Employee:
    def __init__(self) -> None:
        self.__name = "ram"

a = Employee()
#print(a.__name) #returns an error, we cant access directly
print(a._Employee__name) #can be accessed indirectly, name mangling

print(a.__dir__()) #returns attributes and methods
#name mangling is a technique used to protect class-private and superclass-private attribues from being acidentaly  overwritten by subclasses


#protected acess Modifier
class Student:
    def __init__(self) -> None:
        self._name = "harry"

    
    def _funname(self):  #protceted method
        return "code with harry"

class Subject(Student):  #inherited class
    pass


obj = Student()
obj1 = Subject()

#calling by object of student class

print(obj._name)
print(obj._funname())

#calling by object of subject class

print(obj1._name)
print(obj1._funname())
