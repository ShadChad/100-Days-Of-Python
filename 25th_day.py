#<---------Tuple is immutable------
#as we already know tuples are immutable hence we cannot modify or change the items in tuple but what we can do is---
#-we can change the tuple into lists and hence do all the modifications
#- and we can always change get back to tuple using a tuple keywords




countries = ('Spain','italy','India',"england",'germany')
temp = list(countries) #---Changing into lists
temp.append('russia') #-- we already know the methods of lists, hence we are adding(appending) the value at the last of the tuple/lists
temp.pop(3) #-- We are deleting the 3rd index string
temp[2] = 'Finland' #--we're overwriting the string
countries = tuple(temp) #changing back to tuple again after doing all the modifications
print(countries)

#-concatenating the two tuple, we're creating a third or new tuple and printing out
countries1 = ('pakistan','afghanstan','bangladesh','srilanka')
countries2 = ('vietnam','india',"china")
southEastAsia = countries1 + countries2
print(southEastAsia)



#---Methods of Tuples----

tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = tuple1.count(3) #counts the number of occurance of the given value

res1 = tuple1.index(3) #Gives us the first occurance (index) of the given value
#--will raise a value error if the given value isnt inside the tuple
#res0 = tuple1.index(321)
res2= tuple1.index(3,4,8) #the first paramater will be the value we want to index, and the second and the third are the indexed meaning, the python should only search for  the value inside those index
print('count of 3 in tuple is:',res)
print('the occurance of 3 is in index:',res1)
print('the occurance of 3 inside the index ranging from 4 to 8 is:',res2)



print("the total number of values inside the tuple is",len(tuple1))




