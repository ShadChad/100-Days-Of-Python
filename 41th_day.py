
# defualt mode=read (always)
f = open('myfile.txt','r') #gives the file error if the file doesnt exist, this is the default mode as the paramter
print(f)
text = f.read()
print(text)  #returns the content from the file
f.close()

# write mode
f = open('myfile1.txt','w') #will create the file, if it doesnt exist
# print(f)
text = "hi this is me"
f.write(text)
print(text)  #returns the content from the file
f.close()


# append Mode
f = open('myfile1.txt','a') #will create the file, if it doesnt exist
# print(f)
text = "kushal"
f.write(text)
print(text)  #returns the content from the file
f.close()

with open("myfile.txt",'w') as f:
    f.write('I am inside with')




