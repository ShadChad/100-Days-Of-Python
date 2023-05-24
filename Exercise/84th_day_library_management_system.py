class Library:
    
    def __init__(self) -> None:
        self.count = -1
        self.list = []



    def addbook(self):
        while True:
             self.book = input('Enter the books, press + to break: ')
             self.count += 1
            #  print(self.count)
             self.list.append(self.book)
             if self.book == ' ':
                return False
        

    def showbook(self):
        # self.list.pop(-1)
        return self.list[:-1]
    
    def no_of_book(self):
        if len(self.list[:-1]) == self.count:
            print("Accurate Counting")
        else:
            print("Ig we've got a problam")
            # print(self.count)
            # print(len(self.list[:]))





harry = Library()
harry.addbook()
print(harry.showbook())
harry.no_of_book()
        
            