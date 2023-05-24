import multiprocessing
# import requests
import time
# # import os

# def downloadFile(url,name):
#     print(f"started downloading {name}")
#     response = requests.get(url)
#     open(f"{name}.jpg","wb").write(response.content)
#     print(f"finshed downloading {name}")



# url = "https://picsum.photos/200/300"

# pros = []
# for i in range(5):
#     # downloadFile(url,i)
#     p = multiprocessing.Process(target=downloadFile,args=[url,i])

#     p.start()

#     pros.append(p)

# for p in pros:
#     p.join()

square_result=[]


def calc_square(numbers):
    global square_result
    for n in numbers:
        # time.sleep(5)
        print("square"+ str(n*n))
        square_result.append(n*n)
    print('within a process : result' + str(square_result)) #due to multiprocessing, the result gets shown here

def calc_cube(numbers):
    for n in numbers:
        # time.sleep(5)
        print('cube'+str(n*n*n))








if __name__ == "__main__":
    arr = [2,3,4,5]
    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube,args=(arr,))

    p1.start()
    p2.start()


    p1.join()
    p2.join()

    # print('result',str(square_result)) if it was multithreading the result would have shown here
    print("done!")

     

