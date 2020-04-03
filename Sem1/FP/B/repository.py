from domain import *
import datetime

class BookRepository:
    def __init__(self,books):
        self._books=books


    def getAll(self):
        return self._books
    def add_book(self,book):
        '''
        Adds a new book to the list
        book-the new book
        Raises BookException if the id is already used
        '''
        '''
        if self.validateId(int(book.bookId))==1:
            raise BookException("Id is already used!")
        '''
        self._books.append(book)

    def get_books(self):
        return self._books.copy()

    def validateId(self,bid):
        '''
    Checks if a book id is in the list
    bid-the id checked
    returs 1 if it is already in the list, 0 otherwise
        '''
        for i in self._books:
            if int(i.bookId)==int(bid):
                return 1 
        return 0
    def update_book(self, bid, btitle, bauthor):
        '''
Updates the details of a book
params:
bid-the id of the book
btitle-the new title
bauthor-the new author
Raises BookException if the id is not found
        '''
        for i in self._books:
            if int(i.bookId)==int(bid):
                i.Title=btitle 
                i.Author=bauthor 
        if self.validateId(bid)==0:
            raise BookException("No id found!")
    def delete_book(self,bid):
        '''
Deletes a book from the list
params-id-the id of the book
        '''
        z=self._books.copy()
        self._books.clear()
        for i in z:
            if int(i.bookId)!=int(bid):
                self._books.append(i)































class ClientRepository:
    def __init__(self, clients):
        self._clients=clients

    def getAll(self):
        return self._clients
    def validatecId(self,cid):
        '''
Checks if a client id is already used
cid-the client id
returns 1 if it is used, 0 otherwise
        '''
        for i in self._clients:
            if int(i.clientId)==int(cid):
                return 1 
        return 0

    def add_client(self,client):
        '''
Adds a new client to the list
params: client-the new client
raises ClientException if the id is already used
        '''
        #if self.validatecId(int(client.clientId))==1:
            #raise ClientException("Id already used!")
        self._clients.append(client)

    def get_clients(self):
        return self._clients.copy()


    def update_client(self, cid, cname):
        '''
Updates the details of a client
params cid-the id of the client
cname-the new name
raises ClientException if the id is not found
        '''
        for i in self._clients:
            if int(i.clientId)==int(cid):
                i.Name=cname 
        if self.validatecId(cid)==0:
            raise ClientException("No id found!")
    

    def delete_client(self,cid):
        '''
Deletes a client from the list
cid-the id of the client
        '''
        z=self._clients.copy()
        self._clients.clear()
        for i in z:
            if int(i.clientId)!=int(cid):
                self._clients.append(i)





















class RentalRepository:
    def __init__(self, rentals):
        self._rentals=rentals
    def getAll(self):
        return self._rentals

    def add_rental(self,rental):
        '''
Adds a new rental to the list
params: rental-the new rental
        '''
        self._rentals.append(rental)

    def get_rentals(self):
        return self._rentals.copy()

    def update_rental(self, cid, returneddate):
        '''
Updates the return date of a rental
params: cid-the client id
returneddate-the day the book was returned
        '''
        for i in self._rentals:
            if i.clientId==cid:
                i.Returned=returneddate 

    def update_rental_details(self,rid,bid,cid,rent,retur):
        for i in self._rentals:
            if int(i.rentId)==int(rid):
                i.bookId=bid
                i.clientId=cid 
                i.Rented=datetime.date(rent)
                i.Returned=datetime.date(retur)

    def validaterId(self,cid):
        '''
        Checks if a rental id is already used
        params: cid-the client id
        '''
        for i in self._rentals:
            if int(i.clientId)==int(cid):
                return 1 
        return 0

    def delete(self,rid):
        z=self._rentals.copy()
        self._rentals.clear()
        for i in z:
            if int(i.rentId)!=int(rid):
                self._rentals.append(i)

    def __len__(self):
        return len(self._rentals)
