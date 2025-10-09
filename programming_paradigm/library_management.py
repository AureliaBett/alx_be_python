class Book:
    def __init__(self, title, author):
        self.title = title              # public attribute
        self.author = author            # public attribute
        self.__is_checked_out = False   # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self.__is_checked_out

    def __str__(self):
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self.__books = []   # private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self.__books.append(book)
            print(f"Book added: {book.title} by {book.author}")
        else:
            print("Error: Only Book instances can be added.")

    def check_out_book(self, title):
        """Check out a book by its title if available."""
        for book in self.__books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"You have checked out '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is already checked out.")
                    return
        print(f"No book found with title '{title}'.")

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self.__books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"'{book.title}' has been returned.")
                    return
                else:
                    print(f"'{book.title}' was not checked out.")
                    return
        print(f"No book found with title '{title}'.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self.__books if book.is_available()]
        if not available_books:
            print("No available books in the library.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
