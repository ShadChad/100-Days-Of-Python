s1 = {1,2,5,6}
s2 = {3,7,6}
print(s1.union(s2)) #returns the union of sets, all the values
s1.update(s2)
print(s1,s2)

cities = {'tokyo','madrid','berlin','delhi'}
cities2 = {'tokyo','seoul','kabul','madrid'}
# cities3 = cities.intersection(cities2) #returns the intersection, same value fromboth sets
# cities3 = cities.intersection_update(cities2)
cities4 = cities.symmetric_difference(cities2)
print(cities)
# print(cities3)
print(cities4)


cities5 = {'tokyo','madrid','berlin','delhi'}
cities6 = {'tokyo','seoul','kabul','madrid'}
cities7 = cities5.difference(cities2)
print(cities7)

cities8 = {'tokyo','madrid','berlin','delhi','seoul','kabul'}
cities9 = {'tokyo','seoul','kabul','madrid'}
print(cities8.issuperset(cities9))
print(cities9.issubset(cities9))

town = {'helsinki','madrid','brazil','china'}
town.add('nepal') #add one item
town2 = {'ktm','pkr','chitwan'} #ad multiple item
town.update(town2)
town.remove('ktm')
#town.remove('tokyo2') #throws an error
town.discard('tokyo2') #doesnt throws an error
town.pop() #pops the random item
#del town #deletes the whole sets
town.clear() #only clears the item inside the sets, not the whole set
print(town)



info = {'carl',19,False,5.9}
if 'carl' in info:
    print('yes')
else:
    print('no')














