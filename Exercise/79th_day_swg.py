# import random

# def lookup(choose, comp):
#     if choose == -1 and comp == 1:
#         return True
#     elif choose == 0 and comp == 1:
#         return True
#     elif choose == 1 and comp == 0:
#         return True
#     elif(choose == comp):
#         return None
#     else:
#         return False

# user = input('Choose s,w,g: ')
# dict = {'s':-1,'w':0,'g':1}
# choose = dict[user]
# print(choose)
# comp = random.randint(-1,1)
# print(comp)
# computer = ['w','g','s']
# win = lookup(choose,comp)
# if win is None:
#     print("matched Draw")
# elif win:
#     print("You lost, you choose",(user),"and comp choose,"+computer[comp])
# else:
#     print("You won, you choose",user,"and comp choose,"+computer[comp])


import random

def lookup(choose,comp):
    if choose == 's' and comp == 'w':
        return True
    elif choose == 'w' and comp == 'g':
        return True
    elif choose == 'g' and comp == 's':
        return True
    elif(choose == comp):
        return None
    else:
        return False
choosen = ('s','w','g')
choose = input("choose s,w,g: ")
computer = random.randint(-1,1)
print(computer)
comp = choosen[computer]
print(comp)
win = lookup(choose,comp)
if win is None:
    print("draw")
elif win is True:
    print("You won")
else:
    print("you lost")




