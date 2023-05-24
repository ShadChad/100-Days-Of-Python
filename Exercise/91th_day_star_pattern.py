# for i in range(5):
#     for j in range():
#         print('*',end=' ')
#     print()
# n = 10
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=" ")
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()


# def hillpattern(n):
#     n=int(input('enter the number of pattern to draw'))
#     for i in range(n):
#         for j in range(i,n):
#             print(' ',end=" ")
#         for j in range(i+1):
#             print("*",end=" ")
#         for j in range(i):
#             print('*',end=" ")
#         print()
#     for i in range(n):
#         for j in range(i):
#             print(' ',end=' ')
#         for j in range(n-i):
#             print('*',end=' ')
#         for j in range(i,n):
#             print('*',end=" ")
#         print()

# hillpattern(n)
num = 9
for i in range(num):
    for j in range(i,num):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(num):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,num):
        print('*',end=" ")
    for j in range(i+1,num):
        print('*',end=' ')
    print()




