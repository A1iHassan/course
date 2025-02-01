class Book:
    # Class property
    all_books = []

    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        Book.all_books.append(self)

    # Instance Methods
    def borrow(self):
        if self.is_available:
            self.is_available = False
        else:
            print("Book is already borrowed.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
        else:
            print("Book is already available.")

    @classmethod
    def find_books_by_author(cls, author):
        for i in cls.all_books:
            if i.author == author:
                return i.title
        return "Not found"
    
    @classmethod
    def delete_book_by_title(cls, title):
        for i in range(len(cls.all_books)):
            if cls.all_books[i].title == title:
                cls.all_books.pop(i)
                return
        print("No matching book")


    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and len(title) > 0

# Example Usage:
book1 = Book("Python Basics", "John Doe")
book2 = Book("Advanced Python", "John Doe")
book = Book.find_books_by_author("John Doe")
print(book)
Book.delete_book_by_title("Python Basics")
book = Book.find_books_by_author("John Doe")
print(book)
