class Library:
    books=[]
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
    def add_book(self,title,author):
        self.books.append({"title":title,"author":author})
    def remove_book(self,title):
        self.books = [book for book in self.books if book["title"] != title]
    def __str__(self):
        return f"Library: {self.name}\nBooks: {self.books}"
class MemberLibrary(Library):
    checkedout_books=[]
    def __init__(self,name,member):
        super().__init__(name)
        self.member = member
    def checkout_book(self,title,author):
        self.checkedout_books.append({"title":title,"author":author})
    def return_book(self,title):
        self.checkedout_books = [book for book in self.books if book["title"] != title]   
    
x=Library("My Library")
x.add_book("Harry Potter","J.K. Rowling")
x.add_book("The Lord of the Rings","J.R.R. Tolkien")
x.add_book("The Hobbit","J.R.R. Tolkien")
print(x)
x.remove_book("Harry Potter")
print(x)