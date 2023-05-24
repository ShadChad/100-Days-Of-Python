#sets are unordered collection of items,and it is enclosed by curly brackets, sets are unchangable
#sets donot contain double data


s = {2,4,2,6} #2 will be only printed once
print(s)

info = {'carla',19,False,5,9,19} 
print(info)

# items cannot be accesed through indexing

harry = {} #empty curly brackets are always dictionary
print(type(harry))

hari = set() #is set
print(type(hari))

for value in info:
    print(value)