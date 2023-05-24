n = int(121)
l = int(n)
count = 0

while(l>0):
    print(l)
    rev = l % 10
    # print(rev)
    print(rev)
    sum = (n % rev)
    print(sum)
    if sum == 0:
        count += 1
        # print(count)
    l/= 10
    # print(l)
print(count)
        

    
