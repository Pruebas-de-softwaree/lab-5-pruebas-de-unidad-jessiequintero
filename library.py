from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def borrow_book(self, user_id, isbn):
        user = self._find_user(user_id)
        book = self._find_book(isbn)

        book.borrow()
        user.register_borrow(book)

    def return_book(self, user_id, isbn):
        user = self._find_user(user_id)
        book = self._find_book(isbn)

        book.return_book()
        user.register_return(book)

    def _find_user(self, user_id):
        for u in self.users:
            if u.user_id == user_id:
                print("User not found")
                return u
        raise ValueError("User not found")

    def _find_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        raise ValueError("Book not found")

if __name__ == "__main__":
    library1 = Library()

    #Se agrega un libro y un usuario pide prestado el libro disponible (Test_I01)
    book2 = Book("Batalia Book", "Batis Kent", 2013, "ISBN009")
    library1.add_book(book2)
    user2 = User("Renis", 2) 
    library1.add_user(user2)
    library1.borrow_book(2,"ISBN009")
    print(user2.get_history())

    #Devolución correcta de libro y se solicita otro préstamo del mismo libro con otro usuario. (Test_I02)
    library1.return_book(2,"ISBN009")
    print(user2.get_history())

    user3 = User("Vicka", 3) 
    library1.add_user(user3)
    library1.borrow_book(3,"ISBN009")
    print(user3.get_history())

