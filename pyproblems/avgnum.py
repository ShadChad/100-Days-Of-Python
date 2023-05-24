
n = int(input("how many elements"))
sum = 0
for i in range(n):
    print("enter the number:")
    num = float(input())
    sum += num

avg = sum/n
print("the avg is ", avg)
