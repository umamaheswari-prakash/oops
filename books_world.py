class Author:
    def __init__(self, author_name, author_age, author_nationality):
        self.author_name = author_name
        self.author_age = author_age
        self.author_nationality = author_nationality


class Book:
    print("           WELCOME TO BOOK WORLD            ")

    def __init__(self, book_name, book_price, author_name, author_age, author_nationality, ):
        self.book_name = book_name
        self.book_price = book_price
        self.author_name = author_name
        self.author_age = author_age
        self.author_nationality = author_nationality
        self.obj_author = Author(author_name, self.author_age, self.author_nationality)


def calculate_total_price_books(books_details):
    total_price = 0
    for book in books_details:
        total_price = total_price + book.book_price
    print("The total price of books is: ", total_price)


def no_of_books_written_by_author(books_details):
    count = 0
    author = input("Enter a author namefor a no of books written author:")
    for book in books_details:
        if book.author_name.lower() == author.lower():
            count = count + 1
    print("The no of books written by", author, "is", count)


def affordable_books_list(books_details):
    print("The affordable book list is: ")
    for book in books_details:
        if (book.book_price < 1000):
            print("Book name:", book.book_name, "\t  author name is:", book.author_name)


b1 = Book("gunrudo", 79, "swedan", "python", 1200)
b2 = Book("python", 999, "guido van rossum", 64, "Dutch")
b3 = Book("scala", 1500, "Martin Odersky", 61, "German")
b4 = Book("java", 800, "James Gosling", 65, "Canadian")
b5 = Book("C", 1999, "dennis ritchie", 79, "American")
b6 = Book("C++", 1499, "Bjarne Stroustrup", 69, "Danish")
b7 = Book("Generic Java", 599, "Martin Odersky", 61, "German")
books_details = [b1, b2, b3, b4, b5, b6, b7]
calculate_total_price_books(books_details)
no_of_books_written_by_author(books_details)
affordable_books_list(books_details)



'''
           WELCOME TO BOOK WORLD            
The total price of books is:  7475
Enter a author namefor a no of books written author:martin odersky
The no of books written by martin odersky is 2
The affordable book list is: 
Book name: gunrudo 	  author name is: swedan
Book name: python 	  author name is: guido van rossum
Book name: java 	  author name is: James Gosling
Book name: Generic Java 	  author name is: Martin Odersky

'''