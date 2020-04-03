from repository import *
import datetime
class BTextRepository(BookRepository):
    def __init__(self, fileName):
        super().__init__([])
        self._fileName=fileName
        self._loadFile()
    def _loadFile(self):
        f=open(self._fileName, 'r')
        l=f.readline().strip()
        while len(l) >0:
            tokens=l.split(',')
            book=Book(tokens[0],tokens[1],tokens[2])
            self.add_book(book)
            l=f.readline().strip()
        f.close()
    
    def _saveFile(self):
        f = open(self._fileName, "w")
        try:
            for p in self.getAll():
                pString = str(p.bookId) + "," + str(p.Title)+ "," + str(p.Author) +"\n"
                f.write(pString)
            f.close()
        except Exception as e:
            print("An error occured -" + str(e))

    def add_book(self,book):
        BookRepository.add_book(self, book)
        self._saveFile()

    def update_book(self,bid,btitle,bauthor):
        BookRepository.update_book(self,bid,btitle,bauthor)
        self._saveFile()
    
    def delete_book(self,bid):
        BookRepository.delete_book(self,bid)
        self._saveFile()

class CTextRepository(ClientRepository):
    def __init__(self, fileName):
        super().__init__([])
        self._fileName=fileName
        self._loadFile()

    def _loadFile(self):
        f=open(self._fileName, 'r')
        l=f.readline().strip()
        while len(l) >0:
            tokens=l.split(',')
            client=Client(tokens[0],tokens[1])
            self.add_client(client)
            l=f.readline().strip()
        f.close()
    
    def _saveFile(self):
        f = open(self._fileName, "w")
        try:
            for p in self.getAll():
                pString = str(p.clientId) + "," + str(p.Name)+"\n"
                f.write(pString)
            f.close()
        except Exception as e:
            print("An error occured -" + str(e))

    def add_client(self,client):
        ClientRepository.add_client(self, client)
        self._saveFile()

    def update_client(self,cid,cname):
        ClientRepository.update_client(self,cid,cname)
        self._saveFile()
    def delete_client(self,cid):
        ClientRepository.delete_client(self,cid)
        self._saveFile()
        



class RTextRepository(RentalRepository):
    def __init__(self, fileName):
        super().__init__([])
        self._fileName=fileName
        self._loadFile()

    def _loadFile(self):
        f=open(self._fileName, 'r')
        l=f.readline().strip()
        while len(l) >0:
            tokens=l.split(',')
            formatdate="%Y-%m-%d"
            rental=Rental(tokens[0],tokens[1],tokens[2],datetime.datetime.strptime(tokens[3], formatdate).date(), datetime.datetime.strptime(tokens[4], formatdate).date())
            self.add_rental(rental)
            l=f.readline().strip()
        f.close()
    
    def _saveFile(self):
        f = open(self._fileName, "w")
        try:
            for p in self.getAll():
                pString = str(p.rentId) + "," + str(p.bookId)+","+str(p.clientId) + "," + str(p.Rented)+","+str(p.Returned)+"\n"
                f.write(pString)
            f.close()
        except Exception as e:
            print("An error occured -" + str(e))

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

    