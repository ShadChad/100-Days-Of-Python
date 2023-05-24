class GparentClass:
    def gparent_method(self):
        print("This is the gparent method")
    

class gChildClass(GparentClass):
    def gchild_method(self):
        print("this is the gchild method")
        super().gparent_method() #calls the function from the upper class



gchild = gChildClass()
gchild.gchild_method()





class ParentClass:
    def parent_method(slef):
        print("this is the parent method")


class ChildClass(ParentClass):
    def parent_method(self):
        print("Harry")
        super().parent_method()

    
    def child_method(self):
        print("this is the child method")
        super().parent_method()


child_object= ChildClass()
child_object.child_method()
child_object.parent_method()


class Employee:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id



class Programmer(Employee):
    def __init__(self,name,id,lang) -> None:
        super().__init__(name,id)
        self.lang = lang

rohan = Employee("Rohan Das",'420')
harry = Programmer("harry",'2345','python')
print(rohan.name)
print(harry.name)
print(harry.id)
print(harry.lang)


class ParentClass1:
    def parent_method(self):
        print("this is the parent method od parentclass1")
    


class ParentClass2:
    def parent_method(self):
        print('this is the parent method of parentclass2')


class ChildClass1(ParentClass1,ParentClass2):
    def parent_method(self):
        print("this is child parent method")

    def child_method(self):
        print("this is the child method.")
        super().parent_method()


child__object = ChildClass1()
child__object.child_method() 
child__object.parent_method()  

