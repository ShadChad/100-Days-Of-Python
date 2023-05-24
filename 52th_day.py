class Employee:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id= id

    def showDetails(self):
        print(f"the name of employee is {self.name} and {self.id}")


class Programmer(Employee):
    def showLangauge(self):
        print("the defualt langauge is Python")



e1 = Employee('harry bhai',420)
e1.showDetails()
e2 = Programmer('aasish rana magar',90)
e2.showDetails()
e2.showLangauge()

class Home:
    def __init__(self,home,add,space) -> None:
        self.home = home
        self.home_add = add
        self.home_space = space

    def HomeDetails(self):
        print(f"{self.home} is located at {self.home_add} and has a total space of {self.home_space}")

class Hotel(Home): #has all the properties that class home has + we can extend the propertis of hotel
    def hotelRoom(self):
        print(f"the hotel name is {self.home}")

        



h1 = Home('villa','us','4 rooms')
h2 = Hotel("Rani",'aus',78)

h1.HomeDetails()
h2.hotelRoom()
