class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Book added: {book.title} by {book.author}")
        else:
            print("Error: Only Book instances can be added.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"You have checked out '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is already checked out.")
                    return
        print(f"No book found with title '{title}'.")

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"'{book.title}' has been returned.")
                    return
                else:
                    print(f"'{book.title}' was not checked out.")
                    return
        print(f"No book found with title '{title}'.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No available books in the library.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
