# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"You're reading '{self.title}' by {self.author}.")

    def info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# Subclass (Inheritance)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.__file_size = file_size  # Encapsulated (private) attribute

    def download(self):
        print(f"Downloading '{self.title}' ({self.__file_size}MB)...")

    def info(self):  # Overriding parent method (Polymorphism)
        return f"E-Book: '{self.title}' by {self.author}, {self.pages} pages, {self.__file_size}MB"

# Example usage
physical_book = Book("My Afrcan Roots", "Tshepo Masango", 208)
ebook = EBook("Africa CODE", "Gugu Mokoena", 356, 5)

physical_book.read()
print(physical_book.info())

ebook.read()
ebook.download()
print(ebook.info())
