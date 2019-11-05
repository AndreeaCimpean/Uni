from services import Service
from domain import Book
class UI:
    def __init__(self,service):
        self._service = service

    def print_menu(self):
        print(" ")
        print("   1  to add a new book")
        print("   2  to show all books")
        print("   x  to exit")
        print("   3  filter books")
        print("   u to undo the last operation")

    def start(self):
        while True:
            self.print_menu()
            command = input("> ")
            if command == "x":
                return
            elif command == "2":
                self.show_all_books()
            elif command == "1":
                self.add_book()
            elif command == "3":
                self.filter_books()
            elif command == "u":
                self.undo()
            else:
                print("Not a valid command")
        

    def show_all_books(self):
        print(" ")
        print("LIST OF BOOKS")
        print(" ")
        for b in self._service.listBooks:
            print(b)
        print(" ")

    def add_book(self):
        isbn = input("isbn= ")
        author = input("author= ")
        title = input("title= ")
        self._service.addBook(Book(isbn,author,title))
    
    def filter_books(self):
        try:
            word = input("word= ")
            self._service.filterBooks(word)
        except ValueError as ve:
            print(ve)

    def undo(self):
        try:
            self._service.undo()
        except ValueError as ve:
            print(ve)

s = Service()
ui = UI(s)
ui.start()
    