class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Default is False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been marked as borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been marked as returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} doesn't have '{book.title}' borrowed.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f" - {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")


# Sample book list
library_books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald"),
    Book("To Kill a Mockingbird", "Harper Lee"),
    Book("1984", "George Orwell")
]

# Creating a library member
name = input("Enter your name: ")
member_id = input("Enter your member ID: ")
member = LibraryMember(name, member_id)

# User interaction loop
while True:
    print("\nLibrary Menu:")
    print("1. View available books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. View borrowed books")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        print("\nAvailable books:")
        for i, book in enumerate(library_books):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{i + 1}. {book.title} by {book.author} - {status}")
    
    elif choice == "2":
        book_num = int(input("Enter the number of the book to borrow: ")) - 1
        if 0 <= book_num < len(library_books):
            member.borrow_book(library_books[book_num])
        else:
            print("Invalid book number.")
    
    elif choice == "3":
        print("\nYour borrowed books:")
        for i, book in enumerate(member.borrowed_books):
            print(f"{i + 1}. {book.title} by {book.author}")
        book_num = int(input("Enter the number of the book to return: ")) - 1
        if 0 <= book_num < len(member.borrowed_books):
            member.return_book(member.borrowed_books[book_num])
        else:
            print("Invalid book number.")
    
    elif choice == "4":
        member.list_borrowed_books()
    
    elif choice == "5":
        print("Exiting the library system.")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")