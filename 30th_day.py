dict = {
    "Harry": "human being",
    "spoon" : "object"
}
print(dict) #will return the value and key
print(dict['Harry']) #will return the key value

dict1 = {
    344 : 'Harry',
    345 : 'Shubhum',
    346 : 'neha',
    347 : 'Hari',
}
print(dict1[345])

info = {'name' : 'karan','age':19,'eligible':True}
print(info)
#print(info['name2']) #will throw an error
print(info.get('name2')) #wont throw an error, rather will give none value
print(info.keys()) #will give keys
print(info.values()) #will give values



for key in info.keys():
    print(f"the value corresponding to the key {key} is {info[key]}")

print(info.items()) #will give values and keys

for key, value in info.items():
    print(f"the value corresponding to the key {key} is {value}")


