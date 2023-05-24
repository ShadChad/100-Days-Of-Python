'''
dir() fucntions returns a  list of all attributes and methods(including dunder methods) availabe for an object
'''


x = [1,2,3]
print(dir(x)) #gives of the list of all the methods that can be applied
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__',
#  '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#  'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(x.__add__)

y = (1,2,3)

print(dir(y))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__',
#   '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__',
#     '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', 
#     '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

class Person:
    def __init__(self,name,age) -> None:
        self.name = name 
        self.age = age
        self.version = 1


p = Person('john',30)
'''
the __dict__ attribute returns a dictionary representaion of an object attributes
'''
print(p.__dict__)
# ['__add__', '__class__', '__class_getitem__',
#  '__contains__', '__delattr__', '__dir__', '_
# _doc__', '__eq__', '__format__', '__ge__', '
# __getattribute__', '__getitem__', '__getnewargs__',
#  '__getstate__', '__gt__', '__hash__', '__init__', 
# '__init_subclass__', '__iter__', '__le__', '__len__'
# , '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', 
# '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
# {'name': 'john', 'age': 30, 'version': 1}
print(help(Person))
'''
the help() function is used to get help documentation for an object, includiing a desc of its attributes and methods

'''
# class Person(builtins.object)
#  |  Person(name, age) -> None
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name, age) -> None
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
# -- More  --

#in conclusion dir(),dict and help() are useful built in fucntions in python that can be useed to get information about objects.