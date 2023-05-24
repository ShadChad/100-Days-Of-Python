import time

start_time = time.time()
for i in range(10000):
    print("Hello world")
end_time = time.time()
print('the time taken is :',end_time - start_time)