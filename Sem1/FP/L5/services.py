from domain import Book
import copy

class Service:
    def __init__(self):
        self._books = []
        self._history = []
        self.addBook(Book('1a23','Dan Brown','Origins'))
        self.addBook(Book('1b23','Khaled Hosseini','The Kite Runner'))
        self.addBook(Book('1c23','Jose Saramago','Blindness'))
        self.addBook(Book('1d23','Charlotte Bronte','Jane Eyre'))
        self.addBook(Book('1e23','Mircea Eliade','Maitreyi'))
        self.addBook(Book('1f23','Sally Green','Half Bad'))
        self.addBook(Book('1g23','Sally Green','Half Wild'))
        self.addBook(Book('1h23','Rick Yancey','The 5th Wave'))
        self.addBook(Book('1i23','Suzanne Collins','The Hunger Games'))
        self.addBook(Book('1j23','George R.R. Martin','The Winds of Winter'))
        self._history = []

    @property
    def listBooks(self):
        return self._books

    def addBook(self,book):
        '''
        Add the new book to the list of books
        params:
            book - the book
        raise ValueError if the new star does not have a unique isbn
        '''
        for b in self._books:
            if b.Isbn == book.Isbn:
                raise ValueError("Isbn must be unique")

        copyList = copy.deepcopy(self._books)
        self._history.append(copyList)
        self._books.append(book)

    def filterBooks(self,word):
        copyList = copy.deepcopy(self._books)
        self._history.append(copyList)

        self._books.clear()
        for b in copyList:
            title_book = b.Title.split()
            if title_book[0] != word:
                self._books.append(b)
        if self._books == self._history[len(self._history)-1]:
            self._history.pop()
            raise ValueError("There are no books starting with the word: " + word)

    def undo(self):
        if len(self._history) == 0:
            raise ValueError("No more undos!")
        self._books = self._history.pop()

def test_add_book():
    b1 = Book('123','Dan','Title')
    b2 = Book('123','Andreea','Title2')
    s = Service()
    s.addBook(b1)
    assert s.listBooks[len(s.listBooks)-1].Isbn == '123' and s.listBooks[len(s.listBooks)-1].Author == 'Dan' and s.listBooks[len(s.listBooks)-1].Title == 'Title'
    try:
        s.addBook(b2)
        assert False
    except ValueError:
        assert True

test_add_book()

    