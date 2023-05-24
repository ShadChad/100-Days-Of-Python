#single inheritence 

# syntax

# class ChildClass(ParentClass):
#     pass


class Animal: 
    def __init__(self,name,species) -> None:
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="Dog") 

        self.breed = breed

    def make_sound(self):
        print("Bark!")


d = Dog("dog","dogerman")

d.make_sound()

a = Animal("dog","Dog")
a.make_sound()

class Cat(Animal):
    def __init__(self, name, color,food) -> None:
        super().__init__(name, species = "Cat")

        self.color = color
        self.food = food

    def make_sound(self):
        print("meow meow")

    def feed_food(self):
        print("you feeded the cat",self.food)

c = Cat("jenny",'white',"milk")
(c.make_sound())
c.feed_food()


class Employee:
    no_of_leaves = 0

    def __init__(self,aname,asalary,arole) -> None:
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"the name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    
    @staticmethod
    def printgood(string):
        print("this is good" + string)


class Programmer(Employee):
    def __init__(self, aname, asalary, arole,lang) -> None:
        # super().__init__(aname, asalary, arole)
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.lang = lang


    def printProg(self):
        return f"the programmer name is {self.name}. salary is {self.salary} and role is {self.role},the languages are {self.lang}"

harry = Employee("harry",255,"instructor")
rohan = Employee("rohan",455,"student")


shubham = Programmer("shubham", 555, "programmer",["python","cpp"])
karan = Programmer("karan",777, "programmer",["python","java"])


print(karan.printdetails())
print(karan.printProg())






