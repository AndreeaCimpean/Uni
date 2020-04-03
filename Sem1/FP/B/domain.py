from datetime import date

class Book:
    def __init__(self,bid,btitle,bauthor):
        self.bookId=bid
        self.Title=btitle 
        self.Author=bauthor

    @property
    def bookId(self):
        return self._bid

    @property
    def Title(self):
        return self._btitle

    @property
    def Author(self):
        return self._bauthor

    @bookId.setter
    def bookId(self, value):
         self._bid=value

    @Title.setter
    def Title(self, value):
         self._btitle=value

    @Author.setter
    def Author(self, value):
         self._bauthor=value

    def __str__(self):
        return "Id: " + str(self.bookId) + ', Title: ' + str(self.Title) + ", Author:" + str(self.Author)

    def __repr__(self):
        return "Id: " + str(self.bookId) + ', Title: ' + str(self.Title) + ", Author:" + str(self.Author)







#################################################################################################################################################
class Client:
    def __init__(self,cid,cname):
        self.clientId=cid
        self.Name=cname 

    @property
    def clientId(self):
        return self._cid

    @property
    def Name(self):
        return self._cname


    @clientId.setter
    def clientId(self, value):
         self._cid=value

    @Name.setter
    def Name(self, value):
         self._cname=value


    def __str__(self):
        return "Id: " + str(self.clientId) + ', Name: ' + str(self.Name)

    def __repr__(self):
        return "Id: " + str(self.clientId) + ', Name: ' + str(self.Name)



#######################################################################################################################################################

class Rental:
    def __init__(self,rid,bid,cid,rentdate,returdate):
        self.rentId=rid
        self.bookId=bid
        self.clientId=cid
        self.Rented=rentdate
        self.Returned=returdate

    @property
    def rentId(self):
        return self._rid
    def getId(self):
        return self._rid 

    @property
    def bookId(self):
        return self._bid

    @property
    def clientId(self):
        return self._cid

    @property
    def Rented(self):
        return self._rentdate

    @property
    def Returned(self):
        return self._returdate

    @rentId.setter
    def rentId(self, value):
         self._rid=value

    @bookId.setter
    def bookId(self, value):
         self._bid=value

    @clientId.setter
    def clientId(self, value):
         self._cid=value

    @Rented.setter
    def Rented(self, value):
         self._rentdate=value

    @Returned.setter
    def Returned(self, value):
         self._returdate=value

    def __len__(self):
        # _start and _end and python date() type
        # self._end - self._start => timedelta
        return int((self._returdate - self._rentdate).days) + 1

    def __str__(self):
        return "Rent Id: " + str(self.rentId) + ', Book Id: ' + str(self.bookId) + ", Client Id: " + str(self.clientId)+ ', Rent date: ' + str(self.Rented) + ", Returned date: " + str(self.Returned)

    def __repr__(self):
        return "Rent Id: " + str(self.rentId) + ', Book Id: ' + str(self.bookId) + ", Client Id: " + str(self.clientId)+ ', Rent date: ' + str(self.Rented) + ", Returned date: " + str(self.Returned)


