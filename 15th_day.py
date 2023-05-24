import time


currentTime = time.strftime('%H:%M:%S')
#hour = time.strftime('%H')
hour= int(input("enter the time"))

if(hour>=4 and hour<12):
    print("Good Morning")
elif(hour>=12 and hour<=18):
    print("GoodAfternoon")
elif(hour>18 and hour<22):
    print("GoodEvening")
else:
    print("GoodNight")

