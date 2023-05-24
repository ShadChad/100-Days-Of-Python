import functools
import time

#lru also takes a certain memory according to the program

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return(n*5)


print(fx(20))
print("done for 20")

print(fx(2))
print("done for 2")

print(fx(6))
print("done for 6")


#will print instantly cause it fetches the data the cache, it memoizes the values

print(fx(20))
print("done for 20")

print(fx(2))
print("done for 2")

print(fx(6))
print("done for 6")

#takes 5 secs again here
print(fx(61))
print("done for 61")

@functools.lru_cache(maxsize=None)
def identity(name):
    id = name
    time.sleep(4)
    full_name = id + "sharma"

print(identity("hari"))
print("done for hari")

print(identity("shyam"))
print("done for shyam")

print(identity('hari'))#will perform it instantly, it fetches the data from the lru cache
print("done for hari again")





