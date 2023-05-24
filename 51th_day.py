class MyClass:
    def __init__(self,value) -> None:
        self._value = value

    def show(self):
        print(f"value is {self._value}")

    @property
    def ten_value(self):
        return 10* self._value

    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10
        # return 10* self._value
    
    


obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)

obj.show()


class Employee:

    def __init__(self,first,last) -> None:
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@gmail.com'
    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('delete name!')
        self.first = None
        self.last = None






emp_1 = Employee('john','smith')

emp_1.first = 'jim' #changing name, hence all the data should be changed, including email

emp_1.fullname = 'corey schafer'

print(emp_1.first)
# print(emp_1.email()) 
# while using the emial func


#using property decorators
print(emp_1.email) 

# print(emp_1.fullname())
print(emp_1.fullname)

del emp_1.fullname