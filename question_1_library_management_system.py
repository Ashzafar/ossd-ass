# F2020266454

class Library:
    books = []

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})

    def remove_book(self, title):
        self.books = [book for book in self.books if book["title"] != title]

    def __str__(self):
        return f"Library: {self.name}\nBooks: {self.books}"


class MemberLibrary(Library):
    def __init__(self, name, member):
        super().__init__(name)
        self.member = member
        self.checkedout_books = []

    def checkout_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.checkedout_books.append(book)
                self.remove_book(title)
                break

    def return_book(self, title):
        for book in self.checkedout_books:
            if book["title"] == title:
                self.add_book(book["title"], book["author"])
                self.checkedout_books.remove(book)
                break


# Create a library
x = Library("My Library")
x.add_book("Harry Potter", "J.K. Rowling")
x.add_book("The Lord of the Rings", "J.R.R. Tolkien")
x.add_book("The Hobbit", "J.R.R. Tolkien")

print("Library:")
print(x)
x.remove_book("Harry Potter")
print("Library after removing a book:")
print(x)

# Create a member library
member_x = MemberLibrary("Member's Library", "John")
member_x.checkout_book("The Lord of the Rings")
print("\nMember's Library:")
print(member_x)
member_x.return_book("The Lord of the Rings")
print("\nMember's Library after returning a book:")
print(member_x)