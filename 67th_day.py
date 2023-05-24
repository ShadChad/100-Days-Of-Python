import time


def usingWhile():
    i = 0
    while(i<=50000):
        print(i)
        i+= 1

def usingFor():
    for i in range(50000):
        print(i)

timetaken = time.time()
# usingWhile()
taketaken2= time.time() - timetaken

timetaken = time.time()
# usingFor()
taketaken3= time.time() - timetaken

print(taketaken2)

print(taketaken3)


print(4)
# time.sleep(3)
print("gets printed after 3 secs")



print(time.gmtime(0))

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H: %M :%S",t)
print(formatted_time)


# getting current time by passing
# the number of seconds since epoch
# curr = time.ctime(1627908313.717886)
curr = time.ctime()
print("Current time:", curr)



