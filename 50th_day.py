  
# class Dec:
#     def __init__(self,name) -> None:
#         self.name = name

#     def hello(self):
#         print("Hello world",self.name)

#     def add(a,b):
#         print(a+b)


# obj = Dec('kushal')

# obj.hello()


# decorators modifies the orginal function


def greet(fx):
    def mfx(*args, **kwargs):
        print("Goodmorning")
        fx(*args, **kwargs)
        print("Thanks for using the function")
    return mfx

@greet
def hello():
    print("hello world")


def add(a,b):
    print(a+b)






# greet(hello())
hello()
greet(add)(1,3)


# def greety(fxi):
#     def mfxx(*args, **kwargs):
#         print("good morning")
#         fxi(*args, **kwargs)
#         print("Thanks for using the function")
#     return mfxx

# # @greet
# def add(a,b):
#     print(a+b)

# greet(add)(1,3)

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b


my_function(1,3)



