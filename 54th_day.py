class Math:
    def __init__(self,num) -> None:
        self.num = num


    def addtonum(self,n):
        self.num = self.num + n


    @staticmethod #no need to pass self as a argument, we can just use the staticmethod function
    def add(a,b):
        return a+b


a = Math(5)

print(a.num)
a.addtonum(6)
print(a.num)



print(a.add(5,6))
# print(Math.add(5,6)) #same result, obj or class it doesnt matter



class Home:
    @staticmethod
    def add(a,b):
        return a+b


result = Home.add(1,2)
print(result)


class Date:
    def __init__(self,yest) -> None:
        self.yesterday = yest


    def today(self):
        if self.yesterday < 30:
            return self.yesterday + 1
        else:
            return False

    @staticmethod
    def afteraweek(today):
        if today + 7 <=30:
            return today + 7

        else:
            return False


calender = Date(29)
print(calender.today())
print(calender.afteraweek(23))

        




