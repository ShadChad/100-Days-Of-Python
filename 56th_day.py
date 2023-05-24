class Employee:
    company = 'Apple'
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod   #this method is capable of chamging the class variable
    def changeCompany(cls,newCompany):
        cls.company = newCompany



e1 = Employee()
e1.name = 'Harry'
e1.show()

e1.changeCompany('tesla')
e1.show()
print(Employee.company)



class Home:
    home = 'villa'
    def homeName(self):
        print(f'this home {self.home} belongs to {self.name}')


    def changeHome(cls,newHome): #cls can be passed as anything, as it is self rn
        cls.home = newHome



h1 = Home()

h1.name = 'kush'
h1.homeName()
h1.changeHome('hilla') #changes home name to only this oobjects
h1.homeName()
print(Home.home) #prints Villa

#class Methods

class Hoome:
    Home_name = "Silla"

    def showHome(self):
        print(f"the {self.Home_name} belongs to {self.name}")

    @classmethod
    def changeName(tinde,NewHome): #tinde refers to class 
        tinde.Home_name = NewHome



h3 = Hoome()
h3.name = 'sahil'
h3.showHome()
h3.changeName('nilla')
h3.showHome()
print(Hoome.Home_name) #the home name has been changed

