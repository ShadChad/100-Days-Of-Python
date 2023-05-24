# shutil module provides a higher level interface for working with file and directories.

import shutil

import os


# functions of shutil--->

# --> shutil.copy(src,dst) -- copies the file located at the src
# --> shutil.copy(src,dst) -- also adds the metadata,like timestamp

# --> shutil.copytree(src,dst) -- copies the directory located at src

# --> shutil.move(src,dst) -- moves the file located at src to a new location

# --> shutil.rmtree(path) --> this function deletes the directory


# # Copying a file
# shutil.copy("src.txt", "dst.txt")

# # Copying a directory
# shutil.copytree("src_dir", "dst_dir")

# # Moving a file
# shutil.move("src.txt", "dst.txt")

# # Deleting a directory
# shutil.rmtree("dir")





shutil.copy("70th_day.py","70_th_copy.py")

shutil.copytree(".tutorial","mytutorial")

shutil.move(".tutorial/file.file","file.file")

shutil.rmtree("mytutorial")

os.remove("file.file")




