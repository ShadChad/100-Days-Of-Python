import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


#normal code
# time1 = time.perf_counter()

# func(4)
# func(2)
# func(1)

# time2 = time.perf_counter()
# print(time2-time1)


# same code using threads

t1 = threading.Thread(target=func,args=[4])
t2 = threading.Thread(target=func,args=[2])
t3 = threading.Thread(target=func,args=[1])
# all gets excecuted at once

t1.start()#start in background,and throw that in side
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # future1 = executor.submit(func,3)
        # future2 = executor.submit(func,2)
        # future3 = executor.submit(func,6)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        l = [3,4,1,5,2]
        results = executor.map(func,l)
        for result in results:
            print(result)




poolingDemo()
