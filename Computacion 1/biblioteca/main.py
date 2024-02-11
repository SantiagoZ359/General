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
            
            if opc ==3:
                library.show_clients()

            elif opc == 4:
                break


Main.menu()