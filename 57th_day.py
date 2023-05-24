class Employee:
    def __init__(self,name,salary) -> None:
        self.name = name
        self.salary = salary

    @classmethod
    def FromStr(cls,string):
        return cls(string.split('-')[0],int(string.split('-')[1]))




e1 = Employee('john',12000)
print(e1.name)
print(e1.salary)



string = 'harry-12000'
e2 = Employee.FromStr(string)
print(e2.name)
print(e2.salary)



class Person:
    def __init__(self,name,age,address) -> None:
        self.name = name
        self.age = age
        self.address = address


    @classmethod
    def FromStr(cls,string1):
        return cls(string1.split(',')[0],string1.split(',')[1],string1.split(',')[2])




p = Person('aasish',19,'gaindakot')
print(p.name)
print(p.age)
print(p.address)


string1 = 'Aliza,19,chitwan'
p1 = Person.FromStr(string1)
print(p1.name)
print(p1.age)
print(p1.address)

class Rectangle:
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height


    @classmethod
    def square(cls,size):
        return cls(size,size)
    


rectangle = Rectangle.square(10)
print(rectangle.height)
print(rectangle.width)

