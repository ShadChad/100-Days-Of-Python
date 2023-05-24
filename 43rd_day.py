with open('file.txt','r') as f:
    print(type(f))

    f.seek(10) #skips the specific elements
    print(f.tell()) #seeking to the specific position 
    data = f.read(5)
    print(data)

with open('sample.txt','w')as f:
    f.write('hello world')
    f.truncate(5) #only write or reads till the specific elememts

with open('sample.txt','r') as f:
    print(f.read())

