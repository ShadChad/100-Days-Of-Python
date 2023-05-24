a = input('Enter a numeber') #will produce an error if i enter a string rather then a integer
print("Multiplication table of", a ,"is : ")

try:
    for i in range(1,11):
        print(int(a),'x',(i) ,'=', (int(a)*i))
# except Exception as e: #will give e, the reason
#     print('the error is',e)

except:
    print('sorry some error occured invalid inout')


print('Some important lines of code')
print('end of program')

try:
    num = int(input("ente a number"))
    a = [6,4,5]
    print(a[num])
except ValueError:
    print('number entered is not an integer') #if input other than interger this will trigger out
except IndexError:
    print('Index error') #if the python founds we entered a index greater than the list this will trigger out

try:
    l = [1,5,6,7]
    i = int(input("enter the index: "))
    print(l[i])

except:
    print('some error occured')

finally:
    print('i am alaways executed') #this is always occured no matter what, a error or no error
#print('i am alaways executed') #why not use this?

#because
def func1():
    try:
        l = [1,5,6,7]
        i = int(input("enter the index: "))
        print(l[i])
        return 1

    except:
        print('some error occured')
        return 0

    finally:
        print('i am alaways executed') #this is always occured no matter what, a error or no error
    # print('i am always executed')

x = func1()
print(x)