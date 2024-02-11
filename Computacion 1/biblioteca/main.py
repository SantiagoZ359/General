from constants import Constants as constants
from library import Library

#menu
class Main:
    def menu():
        library = Library()
        while True:
            print(constants.MENU)
            opc = int(input(constants.MENU_ANSWER))
            if opc == 1:
                library.add_book()
            
            if opc == 2:
                library.add_client()
            
            if opc == 3:
                library.show_clients()
            
            #if opc == 4:
                #library.book_disponibility()

            if opc == 5:
                library.show_books()

            elif opc == 6:
                break


Main.menu()