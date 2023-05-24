class Library:
    count = 0
    
    def __init__(self) -> None:
        self.list = []


    def add_book(self, book):
        self.list.append(book)
        Library.count += 1
        print(f"you've taken total of {Library.count}")
        # return self.list
    
    def show_book(self):
        return self.list
        
    # def fine_book(self):
    #     self.time = int(input("enter how many days you've hold the book with yourself"))

    #     if self.time > 15:
    #         self.fine = '30$'
    #     else:
    #         self.fine = '0$'

    
    
    def lend_book(self,book):
        if book in self.list:
            return ("Book has been taken by someone else")
        else:
            # print("You can take the book")
            self.list.append(book)
            return ('you can take the book')

    def give_book(self,book):
            self.time = int(input("enter how many days you've hold the book with yourself: "))

            if self.time > 15:
                 self.fine = 'your fine is :30$'
                 return self.fine
            else:
                self.list.remove(book)
                self.fine = 'your fine is : 0$'
                return self.fine




            
        

        








harry = Library()
# harry.add_book('harry potter')
harry.add_book('harry potter')
print(harry.lend_book("harry potter1"))
print(harry.give_book('harry potter'))



print(harry.show_book())
