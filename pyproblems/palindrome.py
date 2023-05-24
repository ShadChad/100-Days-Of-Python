# num = int((input("enter the number")))
# n = num
# sum = 0
# while(num>0):
#     temp = num % 10
#     sum = (sum*10) + temp
#     num = int(num / 10)
# if n == sum:
#     print("number is palindrome",n)
# else:
#     print('it isn"t')

def palindrome(x):
    x = int
    sum = 0
    temp = x
    while(temp>0):
        last = temp % 10
        rev = (sum*0) + last
        num = x/10
    if x == rev:
        return True
    else:
        return False

palindrome(121)


