from TextRepositories import *
from datetime import date

class BookService:
    def __init__(self,UndoController,RentalService, bookRepo):
        self._UndoController=UndoController
        self._RentalService=RentalService
        self._bookRepository = bookRepo
    def get_books(self):
        return self._bookRepository.get_books()

    def create_book(self,bid,btitle,bauthor):
        book=Book(bid,btitle,bauthor)
        self.add_book(book)
        redo = FunctionCall(self.create_book, book.bookId, book.Author,book.Title)
        undo = FunctionCall(self.delete_book, bid)

        op = Operation(undo, redo)
        self._UndoController.recordOperation(op)
        return book     

    def get_bookTitle_fromid(self,id):
        for i in self.get_books():
            if int(i.bookId)==int(id):
                bookTitle=i.Title
        return bookTitle 

    def get_bookAuthor_fromid(self,id):
        for i in self.get_books():
            if int(i.bookId)==int(id):
                bookAuthor=i.Author
        return bookAuthor

    def add_book(self,book):
        '''
    Adds a new book to the list
    params: book-a new book
        '''
        self._bookRepository.add_book(book)
        undo=FunctionCall(self.delete_book, book.bookId)
        redo=FunctionCall(self.create_book, book.bookId, book.Title, book.Author)
        op=Operation(undo,redo)
        listOp=[]
        listOp.append(op)
        self._UndoController.recordOperation(op)

    def update_book(self, bid, btitle, bauthor):
        oldTitle=self.get_bookTitle_fromid(bid)
        oldAuthor=self.get_bookAuthor_fromid(bid)
        self._bookRepository.update_book(bid, btitle, bauthor)
        undo=FunctionCall(self.update_book, bid, oldTitle, oldAuthor)
        redo=FunctionCall(self.update_book, bid, btitle, bauthor )
        op=Operation(undo,redo)
        listOp=[]
        listOp.append(op)
        self._UndoController.recordOperation(op)
        
        '''
Update the details of a book
params- bid-the id of the book
btitle-the new title
author-the new author

        '''
    def delete_book(self, bid,duringUndoRedo=False):

        '''
Delete a book from the list
params-the id of the book to be deleted
Raises BookException if it doesn't find a book with the id
        '''
        '''
        if self._bookRepository.validateId(bid)==0:
            raise BookException("No id found")
        '''
        bTitle=self.get_bookTitle_fromid(bid)
        bAuthor=self.get_bookAuthor_fromid(bid)
        self._bookRepository.delete_book(bid)

        undo=FunctionCall(self.create_book,bid,bTitle,bAuthor)
        redo=FunctionCall(self.delete_book,bid,True)
        op=Operation(undo,redo)
        listOp=[]
        listOp.append(op)
        self._UndoController.recordOperation(op)
        '''
        rentals=self._RentalService.filterC(None,bid)
        for rent in rentals:
            undo=FunctionCall(self._RentalService.createRental, rent.rentId, rent.bookId, rent.clientId,rent.Rented,rent.Returned)
            redo=FunctionCall(self._RentalService.deleteRental, rent.rentId, False)
            op=Operation(undo,redo)
            listOp.append(op)
        cascadeOp=CascadedOperation(listOp)
        self._UndoController.recordOperation(cascadeOp)
        
        if duringUndoRedo==False:
            for rent in rentals:
                self._RentalService.deleteRental(rent.getId(),False)

        '''

    def search_bid(self,bid):
        search=[]
        for book in self.get_books():
            if str(bid) in str(book.bookId):
                search.append(book)
        return search


    def search_btitle(self, btitle):
        search=[]
        for book in self.get_books():
            if str(btitle.lower()) in str(book.Title.lower()):
                search.append(book)
        return search 


    def search_bauthor(self, bauthor):
        search=[]
        for book in self.get_books():
            if str(bauthor.lower()) in str(book.Author.lower()) and len(bauthor)>1:
                search.append(book)
        return search 




















####################################################################################################################################3
class ClientService:
    def __init__(self, UndoController,RentalService, clientRepo):
        self._UndoController=UndoController
        self._RentalService=RentalService
        self._clientRepository = clientRepo

    def get_clients(self):
        return self._clientRepository.get_clients()
    def create(self,clientId, clientName):
        client=Client(clientId, clientName)
        return client 

    def get_client_Namefromid(self,id):
        for i in self.get_clients():
            if int(i.clientId)==int(id):
                cName=i.Name
        return cName 

    def add_client(self,client):
        '''
        Adds a new client to the list
        client-the new client
        Raises ClientException if the id is already used

        '''
        #if self._clientRepository.validatecId(int(client.clientId))==1:
            #raise ClientException("Id already used")
        #else:
        self._clientRepository.add_client(client)
        undo = FunctionCall(self.delete_client, client.clientId, client.Name)
        redo = FunctionCall(self.create_client, client.clientId, client.Name)
        op = Operation(undo, redo)
        listOp=[]
        listOp.append(op)
        self._UndoController.recordOperation(op)

    def update_client(self, cid, cname):
        '''
Updates the details of a client
params: cid-the id of the client
cname-the new name
        '''
        
        clName=self.get_client_Namefromid(cid)
        self._clientRepository.update_client(cid, cname)
        undo=FunctionCall(self.update_client, cid, clName)
        redo=FunctionCall(self.update_client, cid, cname)
        op=Operation(undo,redo)
        listOp=[]
        listOp.append(op)
        self._UndoController.recordOperation(op)

    def create_client(self, cid, cname):
        client=Client(cid, cname)
        self.add_client(client)
        redo = FunctionCall(self.create_client, client.clientId, client.Name)
        undo = FunctionCall(self.delete_client, cid)

        op = Operation(undo, redo)
        self._UndoController.recordOperation(op)
        return client

    def delete_client(self, clientId, duringUndoRedo=False):
        '''
Deletes a client 
params-cid-the id of the client to be deleted
raises ClientException if the id is not found

        '''
        if self._clientRepository.validatecId(clientId)==0:
            raise ClientException("No id found!")
        clientName=self.get_client_Namefromid(clientId) 
        self._clientRepository.delete_client(clientId) 

        undo = FunctionCall(self.create_client, clientId, clientName)
        redo = FunctionCall(self.delete_client, clientId, True)
        op = Operation(undo, redo)
        listOp=[]
        listOp.append(op)
        self._UndoController.recordOperation(op)
        rentals=self._RentalService.filterC(clientId,None)
        for rent in rentals:
            undo=FunctionCall(self._RentalService.add_undorental, rent.rentId, rent.bookId, rent.clientId,rent.Rented,rent.Returned)
            redo=FunctionCall(self._RentalService.deleteRental, rent.rentId, False)
            op=Operation(undo,redo)
            listOp.append(op)
        cascadeOp=CascadedOperation(listOp)
        self._UndoController.recordOperation(cascadeOp)
        
        if duringUndoRedo==False:
            for rent in rentals:
                self._RentalService.deleteRental(rent.getId(),False)
    def search_cid(self,cid):
        search=[]
        for client in self.get_clients():
            if str(cid) in str(client.clientId):
                search.append(client)
        return search


    def search_cname(self, cname):
        search=[]
        for client in self.get_clients():
            if str(cname.lower()) in str(client.Name.lower()) and len(cname)>1:
                search.append(client)
        return search 


class UndoController:
    def __init__(self):
        # History of program operations (the undo-able ones)
        self._history = []
        # Index of operation to undo/redo
        self._index = 0
        # Are we during an undo/redo operation?
        self._duringUndoRedo = False


    def recordOperation(self, operation):
        '''
        Record how to undo/redo a program operation
        '''
        if self._duringUndoRedo == True:
            return


        #if self._index < len(self._history):
         #   self._history = self._history[:self._index]

        self._history.append(operation)
        self._index += 1

    def undo(self):
        if self._index == 0:
            raise ValueError("No more undos!")

        self._duringUndoRedo = True
        self._index -= 1
        self._history[self._index].undo()
        self._duringUndoRedo = False


    def redo(self):
        
        if self._index == len(self._history):
            raise ValueError("No more redos!")

        self._duringUndoRedo = True
        self._history[self._index].redo()
        self._index += 1
        self._duringUndoRedo = False



#remember which function to call and using which parameters
#Implementation of the command design pattern
class FunctionCall:
    def __init__(self, function, *parameters):
        self._function = function
        self._params = parameters

    #() -> function call operator
    def call(self):
        self._function(*self._params)

# undo/redo are the sides of the same coin

class Operation:
    '''
    Encodes an operation that happened in the program
    '''
    def __init__(self, undoFunction, redoFunction):
        self._undo = undoFunction
        self._redo = redoFunction

    def undo(self):
        self._undo.call()

    def redo(self):
        self._redo.call()

class CascadedOperation:
    def __init__(self, listOperations):
        self._listOperations=listOperations

    def undo(self):
        for op in self._listOperations:
            op.undo()

    def redo(self):
        for op in self._listOperations:
            op.redo()


#####################################################################################################################################################33



class RentalService:
    def __init__(self, UndoController, rentalRepo,bookRepo,clientRepo):
        self._UndoController=UndoController
        self._rentalRepository = rentalRepo
        self._bookRepository=bookRepo 
        self._clientRepository=clientRepo
    def get_rentals(self):
        return self._rentalRepository.get_rentals()

    def createRental(self, rentalId, bookId,clientId, rented, returned,duringUndoRedo=True): 
        rental=Rental(rentalId, bookId,clientId, rented, returned)
        self.add_undorental(rental.rentId, rental.bookId,rental.clientId,rental.Rented,rental.Returned)

        if duringUndoRedo==True:
            redo = FunctionCall(self.createRental, rental.rentId, rental.bookId,rental.clientId,rental.Rented,rental.Returned) 
            undo = FunctionCall(self.deleteRental, rentalId)
            cascadeOp = CascadedOperation(Operation(redo, undo))
            self._UndoController.recordOperation(cascadeOp)              
        return rental 

    def add_undorental(self,rid,bid,cid,rented,returned):
        rental=Rental(rid,bid,cid,rented,returned)
        self._rentalRepository.add_rental(rental)
        undo=FunctionCall(self.deleteRental,rental.rentId)
        redo=FunctionCall(self.createRental, rental.rentId,rental.bookId,rental.clientId,rental.Rented,rental.Returned)
        op=Operation(undo,redo)
        listOp=[]
        listOp.append(op)
        self._UndoController.recordOperation(op)

    def add_rental(self,rid, bid, cid): #<rentalID>, <bookId>, <clientId>, <rented date>, <returned date>.
        '''
Rents a book from the list
params:
rid-the id of the rental
bid-the id of the book to be rented
cid-the client id
Raises RentalException if the rental id is already used or if the book is already rented

        '''
        for i in self._rentalRepository._rentals:
            if int(i.rentId)==int(rid):
                raise RentalException("Rental Id already used!")
            '''
            if int(i.bookId)==int(bid) and i.Returned == None:
                raise RentalException("Book already rented!")
            '''
            #if i.Returned != None:
                #raise RentalException("Book already rented!")
        rentedDate=date.today()
        returnedDay=None 
        rental=Rental(rid,bid,cid,rentedDate,returnedDay)
        self._rentalRepository.add_rental(rental)
        undo=FunctionCall(self.deleteRental,rental.rentId)
        redo=FunctionCall(self.createRental, rental.rentId,rental.bookId,rental.clientId,rental.Rented,rental.Returned)
        op=Operation(undo,redo)
        listOp=[]
        listOp.append(op)
        self._UndoController.recordOperation(op)


    def deleteRental(self, rentalId, duringUndoRedo=True):
        rental = self._rentalRepository.delete(rentalId)
        if duringUndoRedo == True:
            undo = FunctionCall(self.createRental, rental.rentId, rental.bookId, rental.clientId, rental.Rented, rental.Returned)
            redo = FunctionCall(self.deleteRental, rentalId) 
            cascadeOp = CascadedOperation(Operation(redo, undo))
            self._UndoController.recordOperation(cascadeOp)
        return rental


    def update_rental(self, rid,bid,cid,rented,returned ):
        self._rentalRepository.update_rental_details(rid,bid,cid,rented,returned)

    def return_book(self, cid,date):
        '''
Returns a rented book
params:
cid-the id of the client which has the book
date- the date the return is made (today)
Raises RentalException if the id of the client is not found
        '''
        if self._rentalRepository.validaterId(cid)==0:
            raise RentalException("No id found!")
        undoDate=None
        self._rentalRepository.update_rental(cid,date)
        undo=FunctionCall(self.update_rental, cid, undoDate)
        redo=FunctionCall(self.update_rental, cid, date)
        op=Operation(undo,redo)
        listOp=[]
        listOp.append(op)
        self._UndoController.recordOperation(op)       

    def filtercRentals(self,clientId,bookid):
        result=[]
        for rental in self._rentalRepository.get_rentals():
            if clientId != None and rental.clientId != None:
                continue
            if bookid != None and rental.bookId != None:
                continue
            result.append(rental)
        return result 




    def mostOftenRentedBooks(self):
        result = []
        for book in self._bookRepository.get_books():
            rentals = self.filterRentals(None, book)
            result.append(BookRentalCount(book, len(rentals)))

        result.sort(reverse=True)
        return result


    def filterRentals(self, client, book):
        result = []
        for rental in self._rentalRepository.get_rentals():
            if client != None and rental.clientId != client.clientId:
                continue
            if rental.bookId != None and rental.bookId != book.bookId:
                continue
            result.append(rental)
        return result
        
    
    def filtercRentals(self, client, book):
        """
        Return a list of rentals performed by the provided client for the provided car
        client - The client performing the rental. None means all clients
        cars - The rented car. None means all cars 
        """
        result = []
        for rental in self._rentalRepository.get_rentals():
            if book != None and rental.bookId != book.bookId:
                continue
            if rental.clientId != None and rental.clientId != client.clientId:
                continue
            result.append(rental)
        return result
        

    def mostActiveclients(self):
        result = []
        for client in self._clientRepository.get_clients():
            rentals = self.filtercRentals(client, None)

            rentalCount = 0
            for rental in rentals:
                rentalCount += len(rental)
            
            result.append(ClientRentalCount(client, rentalCount))
        
        result.sort(reverse=True)
        return result   
        
    def mostAuthor(self):
        mauthor=[]
        stat=[]
        result=[]
        for i in self.mostOftenRentedBooks():
            stat.append(i)
        mauthor.append(stat[0])
        for k in mauthor:
            for j in self._bookRepository.get_books():
                if k.bookId==j.bookId:
                    found=j.Author
        for b in self._bookRepository.get_books():
            if str(b.Author)==str(found):
                result.append(b)

        return result

    def delete_cRentals(self, clientId):
        i = 0
        while i < len(self.get_rentals()):
            if self.get_rentals()[i].clientId == clientId:
                self._rentalRepository.delete(self.get_rentals()[i].rentalId)
            else:
                i += 1

    def filterC(self, clientId,bookId):
        result = []
        for rental in self._rentalRepository.get_rentals():
            if clientId != None and rental.clientId != clientId:
                continue
            if bookId != None and rental.bookId != bookId:
                continue
            result.append(rental)
        return result       

    def getAllRentalsfromClient(self, clientId):
        i=0
        result=[]
        while i< len(self.get_rentals()):
            if self.get_rentals()[i].clientId == clientId:  
                result.append(self.get_rentals()[i])         
            else:
                i+=1
        return result 




#############################################################################################################################################

class BookRentalCount:
    def __init__(self, book, rentalCount):
        """
        Constructor for this data transfer object
        car - The car for this object
        rentalCount - The number of times/days the car was rented for  
        """
        self._book = book
        self._rentals = rentalCount

    @property
    def book(self):
        return self._book
    
    def __lt__(self, bookRental):
        """
        < operator required for sorting the list
        """
        return self.getRentalCount() < bookRental.getRentalCount()
    
    def __str__(self):
        return str(self.getRentalCount()).ljust(10) + " for book " + str(self.book).ljust(40)
    
    def getRentalCount(self):
        return self._rentals 


class ClientRentalCount:
    def __init__(self, client, rentalCount):
        self._client = client
        self._rentals = rentalCount

    @property
    def client(self):
        return self._client
    
    def __lt__(self, clientRental):
        """
        < operator required for sorting the list
        """
        return self.getRentalCount() < clientRental.getRentalCount()
    
    def __str__(self):
        return str(self.getRentalCount()).ljust(10) + " for client " + str(self.client).ljust(40)
    
    def getRentalCount(self):
        return self._rentals 