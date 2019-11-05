class Book:
    def __init__(self,isbn,author,title):
        self._isbn = isbn
        self._author = author
        self._title = title

    @property
    def Isbn(self):
        return self._isbn

    @Isbn.setter
    def Isbn(self,value):
        self._isbn = value

    @property
    def Author(self):
        return self._author

    @Author.setter
    def Author(self,value):
        self._author = value

    @property
    def Title(self):
        return self._title

    @Title.setter
    def Title(self,value):
        self._title = value

    def __str__(self):
        return "isbn: " + str(self.Isbn) + ", author: " + str(self.Author) + ", title: " + str(self.Title)
    

def test_book():
    b = Book('1234','Andreea','Cartea mea')
    assert b.Isbn == '1234' and b.Author == 'Andreea' and b.Title == 'Cartea mea'

test_book()