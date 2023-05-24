#a constructor is a special method in a class used to create and initialize an object of a calss.

#default constructors----->
class Details:
    def __init__(self) -> None:
        print("animal crab belongs to crustacenas group")

obj1 = Details() #prints the value


#parameterized constructor in python


class Person:
    def __init__(self,n,o):
      print('Hey im a person')
      self.name = n
      self.occ = o
    

    def info(self):
        print(f"{self.name} is a {self.occ}")
#self passes as objectt which is 'a and 'b' here
a = Person('harry','developer') #passes the vale as argument n and o
b = Person('divya','hr')
# print(a.name) #pprints harry


# a.name = 'dviya' #overwrites
# a.occ = 'hr'
# print(a.name) #pints divya



a.info()
b.info()


class Home:
    animal = 'crab'
    group = 'seaFood'

    def ani(self):
        print(f"{self.animal} belongs to {self.group}")

f = Home()
print(f.animal)
print(f.group)
f.ani()

f.animal = "goat"
f.group = "land"
f.ani()


class HomeGuy:
    def __init__(self,nt,st) -> None:
        print("Program started")
        self.n = nt
        self.s = st


    def itti(self):
        print(f"{self.n} is a {self.s}")


h = HomeGuy('aasish','developer')
h.itti() #prints aasish is a developer



class Deeti:
    def __init__(self,a,s) -> None:
        self.name = a
        self.group = s



m = Deeti("crab",'crustaceans')
print(m.name,"belongs to",m.animal,'group')

