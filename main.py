class Book():
    title = ""
    author = ""
    isbn = ""
    available = False
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    
    def __str__(self):
        return f"{self.title}, {self.author}, {self.isbn}"

    def borrow(self):
        if self.available == True:
            self.available = False
        else:
            return "book is not available"
    
    def return_book(self):
        if self.available == False:
            self.available = True
        else:
            return "book is not borrowed"

class Member():
    name = ""
    member_id = ""
    borrowed_books = []
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
    
    def __str__(self):
        return f"{self.name}, {self.member_id}, {self.borrowed_books}"
       
    def borrow_book(self, book):
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        self.borrowed_books.remove(book)

class Library():
    books = []
    members = []
    def __init__(self):
        pass
    def add_book(self, book):
        self.books.append(book)
    def register_member(self, member):
        self.members.append(member)
    def issue_book(self, member_id, isbn):
        for i in self.members:
            if i.member_id == member_id:
                for j in self.books:
                    if j.isbn == isbn:
                        i.borrow_book(j)
        
    def return_book(self, member_id, isbn):
        for i in self.members:
            if i.member_id == member_id:
                for j in self.books:
                    if j.isbn == isbn:
                        i.return_book(j)

# ایجاد کتاب‌ها
book1 = Book("1984", "جورج اورول", "1234567890")
book2 = Book("کشتن مرغ مقلد", "هارپر لی", "0987654321")

# ایجاد کتابخانه و اضافه کردن کتاب‌ها
library = Library()
library.add_book(book1)
library.add_book(book2)

# ثبت یک عضو
member = Member("آلیس", "M001")
library.register_member(member)

# امانت دادن کتاب به عضو
library.issue_book("M001", "1234567890")

# بازگرداندن کتاب
library.return_book("M001", "1234567890")



#https://github.com/MARMARMOOZ/LibraryManagementSystem/