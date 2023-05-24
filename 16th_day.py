# x = 4
x = int(input("Enter the value of X: "))
#x is the variable to match
match x:
    #if x is 0
    case 0:
        print('x is xero')
    #case with if-condition
    case 1:
        print("case is 1")
    # case 4 if x % 2 == 0:
    #     print("x % 2 == 0 and case is 4")
    #empty case with if-condition
    #case _ if x < 10:
     #   print("x is <10")
        #default case(will only be matched if the above 
        # cases were not matched
        #so it is basically just an else:
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
        
    case _:
        print(x)
