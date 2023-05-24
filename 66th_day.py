#--->hybrid anad hierarchaial inheritance

#--->example of hybrid inheritence

class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1,Derived2):
    pass


#--> Hierarchical Inheritence

        #         CEO
        #          |
        #     -----------
        #     |    |     |
        #    m1   m2    m3    


class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass

class D3(D1):
    pass

#-->Hybrid Inheritance

class Employee:
    company_name = "techgram academy"

class SystemAnalyst(Employee):
    salary = 45000

class Tutor(Employee):
    salary = 35000

class PythonTutot(Tutor):
    salary = 80000

inderjit = PythonTutot()

print("inderjit = " + inderjit.company_name)
print("inderjit = " , inderjit.salary)

#--> Hierarchical inheritance

class Ceo:
    company = 'abc'

class manager(Ceo):
    department = "sales"
    salary = 56000

class staff(manager):
    specialist = "seller"

class Guard(staff):
    shift = "9 t0 5"
    name = "aasish"


g = Guard()
print(f"name = {g.name},company = {g.company},department = {g.department}")
    




