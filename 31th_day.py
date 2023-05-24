ep1 = {122:45,123:89,567:69,670:69}

ep2 = {222:67,566:90}
ep1.update(ep2)
# ep1.clear() #clears the values
empt = {}
# print(empt)
ep1.pop(122) #removes the given key
ep1.popitem() #removes the last item
del ep1[123] #removes the item
# del ep1 deletes the dict 
print(ep1)

