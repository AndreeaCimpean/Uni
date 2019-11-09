from domain import Book
import copy
import names
import random

class Service:
    def __init__(self):
        self._books = []
        self._history = []
        self.generate_list_of_books()
        self._history = []

    def generate_book(self):
        '''
        Generate a random book
        params:
            no params
        output:
            the book generated (as an object of type Book)
        '''
        author = names.get_full_name()
        dictionary = {"first":["The", "Crazy","Red","Good","Bad"],"second":["Bold","Cute","Old","Stylish","Cool"],"third":["Grandma","Tomato","Hedgehog","Book","Potato"]}
        title = ""
        title += dictionary["first"][random.randint(0,4)]
        title += " "
        title += dictionary["second"][random.randint(0,4)]
        title += " "
        title += dictionary["third"][random.randint(0,4)]
        isbn = chr(random.randint(97,122)) + str(random.randint(10000,99999))
        return Book(isbn,author,title)
    
    def generate_list_of_books(self):
        '''
        Generate the initial list of books (a valid list)
        '''
        while len(self.listBooks) < 10:
            try:
                self.addBook(self.generate_book())
            except ValueError:
                pass
        

    @property
    def listBooks(self):
        return self._books

    def addBook(self,book):
        '''
        Add the new book to the list of books, keep in history the state of the list of books before the new book is added
        params:
            book - the book (of type Book)
        raise ValueError if the new book does not have a unique isbn
        '''
        for b in self._books:
            if b.Isbn == book.Isbn:
                raise ValueError("Isbn must be unique")

        copyList = copy.deepcopy(self._books)
        self._history.append(copyList)
        self._books.append(book)

    def filterBooks(self,word):
        '''
        Filter the books by the given word (delete the books starting with that word)
        params:
            word - the given word
        if there are no books starting with the wor raise an error
        otherwise delete the books from the list of books
        '''
        copyList = copy.deepcopy(self._books)
        self._history.append(copyList)

        self._books.clear()
        for b in copyList:
            title_book = b.Title.split()
            if title_book[0].lower() != word.lower():
                self._books.append(b)
        if self._books == self._history[len(self._history)-1]:
            self._history.pop()
            raise ValueError("There are no books starting with the word: " + word)

    def undo(self):
        '''
        Undo the last command that modified data
        '''
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

    