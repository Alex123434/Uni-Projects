# Special Methods

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # Number of pages in the book
    def __len__(self):
        return self.pages
    
    # Delete the book object when it goes out of scope
    def __del__(self):
        print(f"The book {self.title} by {self.author} has been deleted.")
    
Book = Book("Pependence","Penes", 300)

print(Book) 
print(len(Book))

# Deleting the object
del Book
