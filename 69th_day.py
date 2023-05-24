# walrus operator :=

# new to python 3.8
# assignment expression aka walrus operator
# assigns values to varibles as part of a larger expression



a = True 
# print(a=False) will return an error
print(a:=False)


numbers = [1,2,3,4,5]
while(n:= len(numbers) > 0):
    print(numbers.pop())


happy = False
print(happy)

print(happy:=True)


# foods = list()
# while True:
#     food = input("what food do you like?")
#     if food == "quit":
#         break
#     foods.append(food)


# foods = list()
# while(food:= input("what food do you like?: ")) != "quit":
#     foods.append(food)


my_len = [1,3,3]

if(l:= len(my_len)>1):
    print("assigned")

