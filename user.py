class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.history = []

    def register_borrow(self, book):
        self.history.append(f"Borrwed: {book.title}")

    def register_return(self, book):
        self.history.append(f"Reurned: {book.title}")

    def get_history(self):
        return self.history

if __name__ == "__main__":
    user1 = User("Jessica", 1)

    #Test_U03 y Test_U04
    user1.register_borrow("El principito")
    user1_history = user1.get_history()
    print(user1_history)