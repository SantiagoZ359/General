class Constants:
    MENU = """
            Hello cliente, welcome, please select an option:
            1 - add a book
            2 - add a client
            3 - show clients registered
            4 - searh a book
            5 - show all books
            6 - exit  
    """
    MENU_ANSWER = "Option: "


    #class book

    ADD_BOOK_INTRO = "To add a book please fill te nexts options:"
    ADD_BOOK_AUTHOR = "Name of the author: "
    ADD_BOOK_TITLE = "Title of the book: "
    ADD_BOOK_CODE = "Code of book: "
    ADD_BOOK_FINISH = "Book added with no errors"
    ADD_BOOK_ERROR = "This book can't be added to list"

    BOOKS_INTRO = "This are all the books in our system:"

    SEARCH_BOOK_INTRO = "Enter the title of the book to search: "
    SEARCH_BOOK_ERROR = "This book don't exist."

    #class client

    ADD_CLIENT_INTRO = "To add a new client we need some information:"
    ADD_CLIENT_NAME = "Client name: "
    ADD_CLIENT_AGE = "Client age: "
    ADD_CLIENT_COUNTRY = "Client country: "
    ADD_CLIENT_FINISH = "Client added correctly"

    SHOW_CLIENTS_INTRO = "Clients allowed in our system: "

    #