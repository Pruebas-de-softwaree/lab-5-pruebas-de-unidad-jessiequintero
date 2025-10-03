class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            raise ValueError("The book is already borrowed")
        self.borrowed = True

    def return_book(self):
        if not self.borrowed:
            raise ValueError("The book is not currently borrowed")
        self.borrowed = False

if __name__ == "__main__":
    book1 = Book("2010", "Jackie Quint", 2008, "ISBN003")

    #Test_U01
    book1_borrow = book1.borrow()
    print(book1.borrowed)
    
    #Test_U02
    book1_return = book1.return_book()
    print(book1.borrowed)


