# import sys
import os
from os import listdir
def clutter(file):
    # cwd = os.getcwd()
    # print(cwd)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    dir_name = (r"\Users\subed\Desktop\python 100 days of code\clutter_files")
    test = os.listdir(dir_name)


    for item in test:
        if item.endswith(file):
            # dir_hii = (os.path.join(dir_name,item))
            # print(dir_hii)
            os.remove(os.path.join(dir_name,item)) #to concatanate the png file location
            print("Item removed")   


clutter('.txt')


