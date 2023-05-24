class Vector:
    def __init__(self, i,j,k) -> None:
        self.i = i
        self.j = j
        self.k = k

    # def vector_Show(self):
    #     return f"{self.i}i + {self.j}j + {self.k}k"
    

    def __str__(self):  #__str__ gets executed while printing the object
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,other):
        return f"{self.i + other.i}i + {self.j + other.j}j + {self.k + other.k}k"
    
    def __mul__(self,other):
        return f"{self.i * other.i}i + {self.j * other.j}j + {self.k * other.k}k"
    

vec = Vector(2,3,4)
vec1 = Vector(6,7,8)
print(vec)
print(vec1)
# print(vec.vector_Show())
print(vec+vec1) #i defined a method to do so
print(vec*vec1) #defined a method above 


class Employee: 

    no_of_leaves = 0

    def __init__(self, name, salary, arole) -> None:
        self.name = name
        self.salary = salary
        self.arole = arole


    def printDetails(self):
        return f"the name is {self.name} and salary is {self.salary},and role is {self.role}"
    

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self,other):
        return self.salary + other.salary
    
    def __truediv__(self,other):
        return self.salary / other.salary
    
    def __repr__(self):
        return f"{self.name}:{self.salary}:{self.arole}" #gets ignored after __str__ method
    
    def __str__(self):
        return f"the name is {self.name} and salary is {self.salary},and role is {self.arole}"
    

emp1 = Employee('harry',345, "programmer")
print(emp1) #print(str(emp1))
print(repr(emp1))

emp2 = Employee("Rohan",5,"Cleaner")
print(emp2)
print(repr(emp2))

print(emp1+emp2) #adds 345+5

print(emp1/emp2)

    





