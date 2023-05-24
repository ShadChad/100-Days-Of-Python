# class varible
class MyClass:
    class_variable = 0

    def __init__(self) -> None:
        MyClass.class_variable += 1

    def print_class_variable(self):
        print(MyClass.class_variable)
obj1 = MyClass()
obj2 = MyClass()

obj1.print_class_variable()  #the value get incremented
obj2.print_class_variable()


# instance varible
class MyClass:
    def __init__(self,name) -> None:
        self.name = name

    def print_name(self):
        print(self.name)

obj1 = MyClass("john")
obj2 = MyClass('jane')


obj1.print_name()
obj2.print_name()





class Employee:
    def __init__(self,name) -> None:
        self.name = name 

    def showdetails(self):
        print(f"the name of the Employee is {self.name}")



emp1 = Employee("Harry")
emp1.showdetails()



class Employee:
    def __init__(self,name) -> None:
        self.name = name


    def showdetails(self):
        print(f"the name of the employee is {self.name}")




emp2 = Employee('Aasish')

# emp2.showdetails() #here goes emp2 as self
Employee.showdetails(emp2)  #here goes emp2 as a argument,self which is both the exact thing




class Employee:
    companyName = 'Apple'
    noOfEmployees = 0
    def __init__(self,name) -> None:
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1


    def showDetails(self):
        print(f"the name of the employee is {self.name} and the raise amount in {self.companyName} of sized {self.noOfEmployees} is {self.raise_amount}")




emp3 = Employee("Riti")
emp3.raise_amount = 0.3
emp3.companyName = "Apple India" #the company name will only change for Riti, not for the whole class
#if there is intance variable,it will first search for the instance variable, and then to class varible

emp3.showDetails()


emp4 = Employee("rohan")
Employee.companyName = "Google" #changes the class variable
print(Employee.companyName) #will print company name, class variable
emp4.showDetails()



class Math:
    pi = 3.14
    calculation = 0


    def __init__(self,value) -> None:
        self.value = value
        Math.calculation += 1



    def cal(self):
        return self.pi*(self.value*self.value) 

    def calcu(self):
        return self.calculation


algo = Math(4)
print(algo.cal())
algo1 = Math(6)
print(algo1.cal())

print('the number of calculation you did is:',algo.calcu())



         
