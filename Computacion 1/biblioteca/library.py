from constants import Constants as constants
from book import Book
from client import Client

class Library:
    books = []
    clients = []

    def add_book(self):
        print(constants.ADD_BOOK_INTRO)
        author = input(constants.ADD_BOOK_AUTHOR)
        title = input(constants.ADD_BOOK_TITLE)
        code = int(input(constants.ADD_BOOK_CODE))
        disponibility = True

        book = Book(author,title,code,disponibility)
        self.books.append(book)
        print(constants.ADD_BOOK_FINISH)
        return book
    
    def add_client(self):
        print(constants.ADD_CLIENT_INTRO)

        name = input(constants.ADD_CLIENT_NAME)
        age = input(constants.ADD_CLIENT_AGE)
        country = input(constants.ADD_CLIENT_COUNTRY)

        client = Client(name,age,country)
        self.clients.append(client)
        print(constants.ADD_CLIENT_FINISH)

        return client
    
    def show_clients(self):
        print(constants.SHOW_CLIENTS_INTRO)
        for i in range(len(self.clients)):
            print(self.clients[i])
    
    def show_books(self):
        print(constants.BOOKS_INTRO)
        for i in range(len(self.books)):
            print(self.books[i])

    def book_disponibility(self):
        name_book = input(constants.SEARCH_BOOK_INTRO)

        for i in range(len(self.books)):
            print("entra")
            if self.books[i].name == name_book:
                print("1")
                return self.books[i]
            else:
                print(constants.SEARCH_BOOK_ERROR)
                return None