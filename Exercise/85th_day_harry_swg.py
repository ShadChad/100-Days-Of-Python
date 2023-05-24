import random


def gamecheck(comp,user):
    if comp == user:
        return 0
    elif comp == 0 and user== 1:
        return 1
    elif comp == 1 and user == 2:
        return 1
    elif comp == 2 and user == 0:
        return 1
    
    return -1

    



comp = random.randint(0,2)
# print(comp)
user = int(input("enter 0 for snake 1 for water and  2 for gun: "))
print("comp:",comp)
print("user:",user)

score = gamecheck(comp,user)

if score == 0:
    print("game draw")
elif score == 1:
    print("comp wins")
else:
    print("you won")



