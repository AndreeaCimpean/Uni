from service import *
from TextRepositories import *
from picklerepository import *
import random
import datetime
from exceptions import *


class UI:
    def __init__(self,bookServ, clientServ, rentalServ,UndoController):
        self._bookService = bookServ
        self._clientService = clientServ
        self._rentalService = rentalServ
        self._UndoController=UndoController


############################################################################################

    def showRentals(self):
        '''
Shows the list of rentals
        '''
        print("-------------LIST OF RENTALS-----------------")
        for i in self._rentalService.get_rentals():
            print(i)

    def add_rentalUI(self):
        #<rentalID>, <bookId>, <clientId>, <rented date>, <returned date>.
        try:
            rid=int(input("Id= "))
            bid=int(input("Book Id= "))
            cid=int(input("Client Id= "))
            self._rentalService.add_rental(rid,bid,cid)
            print("Book was successfully rented!")
        except RentalException as ve:
            print(ve)
    def returnUI(self):
        try:
            cid=int(input("Client Id= "))
            ddate=date.today()
            self._rentalService.return_book(cid,ddate)
            print("Book was successfully returned!")
        except RentalException as ve:
            print(ve)

    def _mostRentedBooksUI(self):
        print("------------MOST RENTED BOOKS---------------")
        for i in self._rentalService.mostOftenRentedBooks():
            print(i)

    def _mostActiveUI(self):
        self.showRentals()
        print("------------MOST ACTIVE CLIENTS---------------")
        for i in self._rentalService.mostActiveclients():
            print(i)

    def _mostRentedauthorUI(self):
        for i in self._rentalService.mostAuthor():
            print(i)

    

###########################################################################################3
    def delete_clientUI(self):
        cid=int(input("Id of the client= "))
        self._clientService.delete_client(cid)
        print("The client was deleted! ")

    def showClients(self):
        '''
Shows the list of clients
        '''
        print("--------------LIST OF CLIENTS----------------")
        for i in self._clientService.get_clients():
            print(i)

    def undoUI(self):
        self._UndoController.undo()

    def redoUI(self):
        self._UndoController.redo()

    def add_clientUI(self):
        try:
            cId=int(input("Id= "))
            cName=input("Name= ")
            client= Client(cId, cName)
            self._clientService.add_client(client)
            print("Client was added successfully!")
        except ClientException as ve:
            print(ve)

    def update_clientUI(self):
        try:
            cid = int(input("Id = "))
            cname = input("Name = ")
            self._clientService.update_client(cid, cname)
            print("Successful update")
        except ClientException as ve:
            print(ve)

    def search_cidUI(self):
        cid=input("id= ")
        for c in self._clientService.search_cid(cid):
            print(c)
    def search_cnameUI(self):
        cname=input("name= ")
        for c in self._clientService.search_cname(cname):
            print(c)

#####################################################################################################3

    def showBooks(self):
        '''
Shows the list of books
        '''
        print("------------LIST OF BOOKS---------------")
        for i in self._bookService.get_books():
            print(i)

    def add_bookUI(self):
        try:
            bId=int(input("Id= "))
            bTitle=input("Title= ")
            bAuthor=input("Author= ")
            book = Book(bId, bTitle, bAuthor)
            self._bookService.add_book(book)
            print("Book was added successfully!")
        except BookException as ve:
            print(ve)

    def delete_bookUI(self):
        try:
            bid=int(input("Id of the book= "))
            self._bookService.delete_book(bid)
            print("The book was deleted! ")
        except BookException as ve:
            print(ve)

    def update_bookUI(self):
        try:
            bid = int(input("Id = "))
            btitle = input("Title = ")
            bauthor = input("Author ")
            self._bookService.update_book(bid, btitle, bauthor)
            print("Successful update! ")
        except BookException as ve:
            print(ve)


    def search_bidUI(self):
        bid=input("id= ")
        for b in self._bookService.search_bid(bid):
            print(b)

    def search_btitleUI(self):
        btitle=input("title= ")
        for b in self._bookService.search_btitle(btitle):
            print(b)


    def search_bauthorUI(self):
        bauthor=input("author= ")
        for b in self._bookService.search_bauthor(bauthor):
            print(b)

    def printMenu(self):
        print("   ")
        print("   ")
        print("************************************************************************")
        print("1.  Show the list of books")
        print("2.  Show the list of clients")
        print("3.  Show the list of rentals")
        print("4.  Add a new book")
        print("5.  Add a new client")
        print("6.  Rent a book")
        print("7.  Delete a book")
        print("8.  Delete a client")
        print("9.  Update a book details")
        print("10. Update a client details")
        print("11. Return a book")
        print("12. Search a client by id")
        print("13. Search a book by id")
        print("14. Search a client by name")
        print("15. Search a book by title")
        print("16. Search a book by author")
        print("17. Statistics: most rented books")
        print("18. Statistics: most active clients")
        print("19. Statistics: most rented author")
        print("20. Undo")
        print("21. Redo")
        print("x. Exit")
        print("************************************************************************")
        print("   ")
        print("   ")

    def start(self):
        while True:
            self.printMenu()
            cmd=input("command: ")
            if cmd=='1':
                self.showBooks()
            elif cmd=='2':
                self.showClients()
            elif cmd=='3':
                self.showRentals()
            elif cmd=='4':
                self.add_bookUI()
            elif cmd=='5':
                self.add_clientUI()
            elif cmd=='6':
                self.add_rentalUI()
            elif cmd=='7':
                self.delete_bookUI()
            elif cmd=='8':
                self.delete_clientUI()
            elif cmd=='9':
                self.update_bookUI()
            elif cmd=='10':
                self.update_clientUI()
            elif cmd=='11':
                self.returnUI()
            elif cmd=='12':
                self.search_cidUI()
            elif cmd=='13':
                self.search_bidUI()
            elif cmd=='14':
                self.search_cnameUI()
            elif cmd=='15':
                self.search_btitleUI()
            elif cmd=='16':
                self.search_bauthorUI()
            elif cmd=='17':
                self._mostRentedBooksUI()
            elif cmd=='18':
                self._mostActiveUI()
            elif cmd=='19':
                self._mostRentedauthorUI()
            elif cmd=='20':
                self.undoUI()
            elif cmd=='21':
                self.redoUI()
            elif cmd=='x':
                break
            else:
                print("Invalid command, please choose one from the menu!")

authors=['Agatha Christie', 'John Smith', 'Jill Murphy', 'Virginia Woolf','Shakespeare','WH Smith','F Scott Fitzgerald','Umberto Eco',
'Paulo Coelho','Jane Austen','DH Lawrence','Emily Bronte','Stephen King','Mary Shelley','JK Rowling','Oscar Wilde','Franz Kafka','Dan Brown','Catherine Cookson','Leo Tolstoy']
titles=['Tom Sawyer', 'The Worst Witch', 'Good place', 'Jane Eyre','A clockwork orange','The name of the rose','Poison','Romeo and Juliet','Macbeth','Pride and Prejudice','Mrs Dalloway','Lady Chatterleys lover','The Great Gatsby',
'The beautiful and damned','And Then There Were None','Murder on the Orient Express','Veronica decides to die','The Master and Margarita','War','Let me hand you my love']

def generate_book():
    bid=random.randint(0,200)
    btitle=random.choice(titles)
    bauthor=random.choice(authors)
    return Book(bid,btitle,bauthor)

def generate_bookList():
    books=[]
    i=0
    book=generate_book()
    books.append(book)
    i=1
    while i<=11:
        book=generate_book()
        for j in books:
            if j.bookId==book.bookId:
                book.bookId+=1
        else:
            books.append(book)
        i+=1
    return books
names=['Ana','Marie','Ada','Mona','Euridice','Hecate','Hestia','Paula','Joy','Amelia','Clare','Raquel','Medeea','Andromeda','Maud','Kira','Louise','Olivia','Sarah','Anne','Lesley','Janet']
def generate_client():
    cid=random.randint(0,500)
    name=random.choice(names)
    return Client(cid,name)

def generate_clientList():
    clients=[]
    i=0
    client=generate_client()
    clients.append(client)
    i=1
    while i<=11:
        client=generate_client()
        for j in clients:
            if j.clientId==client.clientId:
                client.clientId+=1
        else:
            clients.append(client)
        i+=1
    return clients

clients=generate_clientList()
books=generate_bookList()

def generate_rental():
    ids=[]
    cids=[]
    rid=random.randint(0,999)
    for j in books:
        ids.append(j.bookId)
    bid=random.choice(ids)
    for c in clients:
        cids.append(c.clientId)
    cid=random.choice(cids)
    rentdate=date(random.randint(2013,2018),random.randint(1,11), random.randint(1,28))
    returdate=date(random.randint(2013,2018),random.randint(1,11), random.randint(1,28))
    while returdate<rentdate:
        returdate=date(random.randint(2013,2018),random.randint(1,12), random.randint(1,27))
    return Rental(rid,bid,cid,rentdate,returdate)

def generate_rentalList():
    ids=[]
    cids=[]
    for b in books:
        ids.append(b.bookId)
    for c in clients:
        cids.append(c.clientId)
    rentals=[]
    i=0
    rental=generate_rental()
    rentals.append(rental)
    i=1
    while i<=11:
        rental=generate_rental()
        for j in rentals:
            if j.rentId==rental.rentId:
                rental.rentId+=1
            if j.bookId==rental.bookId:
                rental.bookId=random.choice(ids)
            if j.clientId==rental.clientId:
                rental.clientId=random.choice(cids)
        else:
            rentals.append(rental)
        i+=1
    return rentals


'''
rentals=generate_rentalList()
clients=generate_clientList()
books=generate_bookList()
rentals=generate_rentalList()
bookRepo = BookRepository(books)
UndoController=UndoController()
clientRepo = ClientRepository(clients)
rentalRepo = RentalRepository(rentals)
rentalServ = RentalService(UndoController, rentalRepo, bookRepo, clientRepo)
clientServ = ClientService(UndoController, rentalServ, clientRepo)
bookServ = BookService(UndoController,rentalServ,bookRepo)
ui = UI(bookServ, clientServ, rentalServ, UndoController)
ui.start()

'''
'''
books=[]
clients=[]
rentals=[]
bookRepo=BTextRepository("C:/Users/Asus/Desktop/UNDO3/books.txt")
UndoController=UndoController()
clientRepo=CTextRepository("C:/Users/Asus/Desktop/UNDO3/clients.txt")
rentalRepo=RTextRepository("C:/Users/Asus/Desktop/UNDO3/rentals.txt")

rentalServ = RentalService(UndoController, rentalRepo, bookRepo, clientRepo)
clientServ = ClientService(UndoController, rentalServ, clientRepo)
bookServ = BookService(UndoController,rentalServ,bookRepo)

ui = UI(bookServ, clientServ, rentalServ, UndoController)
ui.start()

'''

def writeToBinaryFile(fileName, books):
    f = open(fileName, "wb")
    pickle.dump(books, f)
    f.close()

formatdate="%Y-%m-%d"

clients = [Client(1, "Pop"), Client(2, "Morariu"), Client(3, "Moldovean")]
books= [Book(11,'Ana','Maria')]
rentals= [Rental(int(1),int(11),int(1),datetime.datetime.strptime('2002-02-02', formatdate).date(), datetime.datetime.strptime('2003-03-3', formatdate).date()),Rental(int(1),int(11),int(2),datetime.datetime.strptime('2000-02-02', formatdate).date(), datetime.datetime.strptime('2003-03-3', formatdate).date())]

writeToBinaryFile("C:/Users/Asus/Desktop/UNDO3/rentals.pickle", rentals)
writeToBinaryFile("C:/Users/Asus/Desktop/UNDO3/clients.pickle", clients)
writeToBinaryFile("C:/Users/Asus/Desktop/UNDO3/books.pickle", books)

bookRepo=BookPickleRepository("C:/Users/Asus/Desktop/UNDO3/books.pickle")
UndoController=UndoController()
clientRepo=ClientPickleRepository("C:/Users/Asus/Desktop/UNDO3/clients.pickle")
rentalRepo=RentalPickleRepository("C:/Users/Asus/Desktop/UNDO3/rentals.pickle")

rentalServ = RentalService(UndoController, rentalRepo, bookRepo, clientRepo)
clientServ = ClientService(UndoController, rentalServ, clientRepo)
bookServ = BookService(UndoController,rentalServ,bookRepo)

ui = UI(bookServ, clientServ, rentalServ, UndoController)
ui.start()