class Employee:
    def __init__(self,name) -> None:
        self.name = name

    def show(self):
        print (f"the name is {self.name}")

class Dancer:
    def __init__(self,dance) -> None:
        self.dance = dance
    
    def show(self):
        print (f"the dance name is {self.name}")


class DancerEmployee(Employee,Dancer):  #o.show will print the method from the class which is passed fist
    #here it is Employee, hence method of employee will run
    def __init__(self,dance,name) -> None:
        self.dance = dance
        self.name = name


o = DancerEmployee("Khathak","Shavani")
print(o.name)
print(o.dance)

o.show()  #prints "the name is Shavani"

print(DancerEmployee.mro())  #returns the list of method, where the method are serched first.

# returns-->
# [<class '__main__.DancerEmployee'>,
#  <class '__main__.Employee'>, 
# <class '__main__.Dancer'>, 
# <class 'object'>]


class Animal:
    def __init__(self,name,species) -> None:
        self.name = name
        self.species = species

    def make_sound(self):
        print("the sound is made by an animal")

class Mammal:
    def __init__(self,name,fur_color) -> None:
        self.name = name
        self.fur_color = fur_color


class Dog(Animal,Mammal):
    def __init__(self, name,breed,fur_color) -> None:
        Animal.__init__(self,name,species="Dog")
        Mammal.__init__(self,name,fur_color)

        self.breed = breed

    # def make_sound(self):
    #     print("bark!")


d= Dog("jean",'german','grey')
print(d.species)
print(d.fur_color)
print(d.name)
print(d.breed)
(d.make_sound()) #___>will look up on its own class-->in herited first args class-->second aargs class-->insatance

AA = Animal('suhya','reptiles')
(AA.make_sound())  

m = Mammal("dolphin","white")
print(m.fur_color)


        

