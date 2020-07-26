class Author:
    list1=[]
    def __init__(self, author_name, author_age, author_nationality):
        self.author_name = author_name
        self.author_age = author_age
        self.author_nationality = author_nationality
        self.list1.append(self.author_name)


class Book:
    print("           WELCOME TO BOOK WORLD            ")
    list=[]

    def __init__(self, book_name, book_price):
        self.book_name = book_name
        self.book_price = book_price
        self.list.append(self.book_name)

    def is_affordable(self):
        if (self.book_price)< 1000:
            return self.book_name

    def is_expensive(self):
        if self.book_price > 1000:
            return "expensive"


def calculate_total_price_books(books):
    total_price = 0
    for book in books:
        total_price = total_price + book.book_price
    print("The total price of books is: ", total_price)


def no_of_books_written_by_author(author_detail):
    count = 0
    author = input("Enter a author namefor a no of books written author:")
    for book in author_detail:
        if book.author_name.lower() == author.lower():
            count = count + 1
    print("The no of books written by", author, "is", count)



def affordable_books_list(books):
    print("The book name and author name of all affordable books: ")
    details=dict(zip(b1.list,a1.list1))
    for book in range(len(books)):
        affordable_book=books[book].is_affordable()
        for key in details:
            if(affordable_book==key):
                print("book name: ",key,"\t author name: ",details[key])

a1 = Author("guido van rossum", 64, "Dutch")
a2 = Author("Martin Odersky", 61, "German")
a3 = Author("James Gosling", 65, "Canadian")
a4 = Author("dennis ritchie", 79, "American")
a5 = Author("Bjarne Stroustrup", 69, "Danish")
a6 = Author("Martin Odersky", 61, "German")


b1 = Book("python", 999)
b2 = Book("scala", 1500)
b3 = Book("java", 800)
b4 = Book("C", 1999)
b5 = Book("C++", 1499)
b6 = Book("Generic Java", 599)
books = [b1,b2, b3, b4, b5, b6]
author_detail = [a1, a2, a3, a4, a5, a6]
calculate_total_price_books(books)
no_of_books_written_by_author(author_detail)
affordable_books_list(books)

'''
           WELCOME TO BOOK WORLD            
The total price of books is:  7475
Enter a author namefor a no of books written author:martin odersky
The no of books written by martin odersky is 2
The affordable book list is: 
Book name: python 	  author name is: guido van rossum
Book name: java 	  author name is: James Gosling
Book name: Generic Java 	  author name is: Martin Odersky

'''
