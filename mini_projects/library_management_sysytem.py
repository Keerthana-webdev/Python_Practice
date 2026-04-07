class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Book(title))

    def borrow_book(self, title):
        for b in self.books:
            if b.title == title and b.available:
                b.available = False
                print("Book borrowed")
                return
        print("Book not available")

    def return_book(self, title):
        for b in self.books:
            if b.title == title:
                b.available = True
                print("Book returned")

lib = Library()

lib.add_book("Python")
lib.add_book("Java")

lib.borrow_book("Python")
lib.borrow_book("C")
lib.return_book("Python")
lib.borrow_book("Python")