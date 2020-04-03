from repository import *

import pickle 

class BookPickleRepository(BookRepository):
    def __init__(self, fileName):
        self._fileName=fileName
        super().__init__([])
        self._loadFile()


    def _loadFile(self):
        f=open(self._fileName, "rb")
        books=pickle.load(f)
        for p in books:
            BookRepository.add_book(self,p)
        f.close()

    def _saveFile(self):
        f=open(self._fileName, "wb")
        pickle.dump(self.getAll(), f)
        f.close()

    def add_book(self,book):
        BookRepository.add_book(self, person)
        self._saveFile()

    def update_book(self,bid,btitle,bauthor):
        BookRepository.update_book(self,bid,btitle,bauthor)
        self._saveFile()
    
    def delete_book(self,bid):
        BookRepository.delete_book(self,bid)
        self._saveFile()

class ClientPickleRepository(ClientRepository):
    def __init__(self, fileName):
        self._fileName=fileName
        super().__init__([])
        self._loadFile()

    def _loadFile(self):
        f=open(self._fileName, "rb")
        clients=pickle.load(f)
        for p in clients:
            ClientRepository.add_client(self,p)
        f.close()

    def _saveFile(self):
        f=open(self._fileName, "wb")
        pickle.dump(self.getAll(), f)
        f.close()

    def add_client(self,client):
        ClientRepository.add_client(self, client)
        self._saveFile()

    def update_client(self,cid,cname):
        ClientRepository.update_client(self,cid,cname)
        self._saveFile()
    def delete_client(self,cid):
        ClientRepository.delete_client(self,cid)
        self._saveFile()


class RentalPickleRepository(RentalRepository):
    def __init__(self, fileName):
        self._fileName=fileName
        super().__init__([])
        self._loadFile()

    def _loadFile(self):
        f=open(self._fileName, "rb")
        rentals=pickle.load(f)
        for p in rentals:
            RentalRepository.add_rental(self,p)
        f.close()

    def _saveFile(self):
        f=open(self._fileName, "wb")
        pickle.dump(self.getAll(), f)
        f.close()


    def add_rental(self,rental):
        RentalRepository.add_rental(self, rental)
        self._saveFile()

    def delete(self,rid):
        RentalRepository.delete(self,rid)
        self._saveFile()

    def update_rental(self,cid,returneddate):
        RentalRepository.update_rental(self,cid,returneddate)
        self._saveFile()

    def update_rental_details(self,rid,bid,cid,rent,retur):
        RentalRepository.update_rental_details(self,rid,bid,cid,rent,retur)
        self._saveFile()