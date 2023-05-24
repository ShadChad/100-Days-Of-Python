import os
def current_path():
    cwd = os.getcwd() #guves the current working directory

    print("current working directory is:", cwd)

# os.chdir('../') #backs one directory, we can also give any directory loction to move to
current_path()
if(not os.path.exists('data')):
    os.mkdir('data')
for i in range(0,100):
    # os.mkdir(f"data/Day{i+1}")
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")
    
    

