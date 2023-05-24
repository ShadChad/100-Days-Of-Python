from functools import reduce
#map
def cube(x):
    return x * x * x


print(cube(2))
# newl = []
l = [1,2,4,6,4,3]
# for item in l:
#     newl.append(cube(item))
# newl = list(map(cube,l))
newl = list(map(lambda x:x*x*x,l))
print(newl)


#filter
def filter_function(a):
    return a>2

newnewl = list(filter(filter_function,l))
print(newnewl)

# reduce

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y: x+y,numbers)
print(sum)