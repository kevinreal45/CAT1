#Question one - Library management system

class Book:
    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        
        #is_borrowed attribute is boolean
    
    def mark_as_borrowed(self):
        #if a book is borrowed, a borrowed mark is attached
        pass
    
    def mark_as_returned(self):
        #if a book is returned, is_borrowed attribute should be false, then returned mark is attached
        
        pass
    
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        
    def borrow_book(self):
        #check if book is available to borrow
        pass
    def return_book(self):
        #if a book has been borrowed, then it can be returned
        pass
    def list_borrowed(self):
        #displays a list of all borrowed books
        pass
    
#code to allow member to borrow and return books