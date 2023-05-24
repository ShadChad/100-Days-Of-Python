#sometimes we need error to terminate the program, it is really useful sometimes
try:
    a = int(input("enter any value between 5 and 9 "))
    if(a<5 or a>9):
        raise ValueError("value should be between 5 and 9")
    if(a=="quit"):
        print('quit')
except:
    print("quited")





  


