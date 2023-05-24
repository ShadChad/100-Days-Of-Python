# generators are the special type of functions that allow you to create an iterable sequence of values.
# returns a genrator object, shich can be used to generate the values one by one as you iterate over it.
# retunrns of values on the fly, rather than having to create and store the the entire sequence in memory


def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
# print((gen)) #reuturns the object
# print(next(gen))#returns the object value
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for j in gen: 
    # print(j)


names = []
def my_generator1():
    # global names
    for i in range(5):
        name = input("enter your name")
        names.append(name)
        # print(names)
        yield name

gen1 = my_generator1()

print(next(gen1))
print(next(gen1))
# print(next(gen1))
#runs the program only for three time

# for name in names():
#     print(f"1.{name}")




# def my_generator2():
#     for i in range(20):
#         num = i*i
#         yield num
    
# gen2 = my_generator2()


# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))







