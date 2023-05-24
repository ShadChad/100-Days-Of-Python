for i in range(12):
    if(i==10):
        break
    print("5 X",(i+1),"=",5 * (i+1))
    
print("Loop lai break hanyo ra nikliyo")

for i in range(1,101,1):
    print(i,end=" ")
    if(i==50):
        break
    else:
        print("missisippi")
print("thankyou")


for i in range(12):
    if(i==10):
        print("skips the iteration")       
        continue
    print("5 X",i,"=",5 * (i))
    
for i in[2,3,4,6,8,0]:
    if(i%2!=0):
        continue
    print(i)
 
    