class Library:

    def __init__(self, name):
        self.name = name

        self.books= []


    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f"Book '{book}' added to the library.")
        else:
            print(f"Book '{book}' is already in the library.")
        
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from the library.")
        else:
            print(f"Book '{book}' not found in the library.")

    def list_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books in the library.")

class DigitalLibrary(Library):
    
    def download_book(self, book):
        if book in self.books:
            print(f"Downloading '{book}'...")
        else:
            print(f"Book '{book}' not found in the library.")

library1 = DigitalLibrary("Block-B")
library1.add_book("Rajiv")
library1.add_book("Sundeep")
library1.list_books()
library1.download_book("Rajiv")
