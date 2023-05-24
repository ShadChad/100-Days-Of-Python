# Multi level inheritance in python


# syntax
class BaseClass:
    # code
    pass

class DerivedClass1(BaseClass):
    pass

class DerivedClass2(DerivedClass1):
    pass


class Animal:
    def __init__(self,name,species) -> None:
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
    
class Dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name, species="Dog")
        self.breed = breed

    def show_details(self):
        super().show_details(self)
        # print(f"breed : {self.breed}")
    

class GoldenRetriever(Dog):
    def __init__(self, name, color) -> None:
        Dog.__init__(self,name, breed="Golden Retriever")

        self.color = color

    def show_details(self):
        Dog.show_details(self)
        # print(f"color:{self.color}")



o = GoldenRetriever("tommy","gold")
o.show_details()



    



