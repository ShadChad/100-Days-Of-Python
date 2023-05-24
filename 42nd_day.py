f = open('myfile.txt','r')
while True:
    line = f.readline()
    # print(line)
    if not line:
        # print(line,type(line))
        break
    print(line)

i = 0
f = open('myfilenum.txt','r')
while True:
    i += 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]

    print(f"marks of student {i} in maths is: {m1}")
    print(f"marks of student {i} in sci is: {m2}")
    print(f"marks of student {i} in sct is: {m3}")
    print(line)


f = open('myfile1sty.txt','w')
lines = ['line\n','line1\n','line2\n']

f.writelines(lines)
    
f.close()

f = open('newfile.txt','w')
lines = lines = ['line','line1','line2']
for line in lines:
    f.write(line+'\n')
f.close()