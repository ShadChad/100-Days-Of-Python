nums = [2,7,1,11,15]
target = 9
sum = 0
for num in nums:
    i = 0
    newnum = num + sum
    sum = newnum
    i+=1
    if sum==target:
        print("your indices is this", i-1,i)