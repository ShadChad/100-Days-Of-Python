class Shape:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
        super().__init__(radius,radius)


    
    def area(self):
        return 'the area of a circle is',3.14 * super().area()
    


rec = Shape(3,6)
print(rec.area())

c = Circle(5)
print(c.area())

# class instances-->inherited instances-->class variable --> inherited class variable

class A:
    classvar1 = 'I am in class variable in class A' #goes here, if there is no any instance and
    #class variable in class B

    def __init__(self) -> None:
        self.var1 = "i am inside class A's construction"
        self.classvar1 = "Instance var in class A"
        self.special = 'Special' #i want to run this method anyhow, hence here it comes super() method


class B(A):
    classvar1 = 'I am in class B'
    def __init__(self) -> None: #overrides the method, hence the init method above wont run

        super().__init__() #it goes one step above and prints out the details, here, it goes up and sets the value of specail and came back
        self.var1 = "I am inside class b's constructor"
        self.classvar1 = 'instance var in class B'
        # super().__init__() #here, it goes after the self.var1 instance, and overrides the instances by class A, tho prints out the details from class A
        # print(super().classvar1) #gpes one step above and prints out the instance

a = A()
b = B()
print(b.special,b.var1,b.classvar1)
print(b.special)