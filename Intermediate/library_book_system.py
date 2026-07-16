class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def show_books(self):
        for i in self.books:
            print(f"title: {i.title} , available: {i.available}")

    def borrow_book(self, title):
        found = False
        for i in self.books:
            if i.title == title and i.available:
                found = True
                print("Book is available")
                i.available = False
                break
            elif i.title == title and not i.available:
                found = True
                print("Book exists but unavailable")
                break
        if not found:
            print("Book not found")

    def return_book(self, title):
        for i in self.books:
            if title == i.title:
                i.available = True

s1 = Library()

while True:
    print("1. Add book  2. Show books  3. Borrow book  4. Return book  5. Exit")
    c = int(input("choice: "))

    if c == 1:
        tit, auth = input("Enter name of the book and author separated by comma: ").split(",")
        s1.add_book(tit, auth)
    elif c == 2:
        s1.show_books()
    elif c == 3:
        bortitle = input("Title of the book you want to borrow: ")
        s1.borrow_book(bortitle)
    elif c == 4:
        rettitle = input("Title of the book you want to return: ")
        s1.return_book(rettitle)
    elif c == 5:
        print("Thanks for checking")
        break
    else:
        print("Choose a valid option")
