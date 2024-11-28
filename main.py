import json

class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f'"{self.title}" given'
        else:
            return f'"{self.title}" already given'

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f'"{self.title}" returned.'
        else:
            return f'"{self.title}" wasn\'t given.'
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

    def serialize(self):
        return json.dumps(self.__dict__)

class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_checked_out:
            book.check_out()
            self.borrowed_books.append(book)
            return f'"{self.name}" borrowed "{book.title}".'
        else:
            return f'"{book.title}" isn\'t available.'

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f'Reader "{self.name}" returned "{book.title}".'
        else:
            return f'Reader "{self.name}" doesn\'t have "{book.title}".'

    def serialize(self):
        return json.dumps({
            'name': self.name,
            'reader_id': self.reader_id,
            'borrowed_books': [b.serialize() for b in self.borrowed_books]
        })

class Libertarian:
    def __init__(self, name):
        self.name = name

    def add_book(self, book, library):
        library.books.append(book)
        return f'"{self.name}" added book "{book.title}".'

    def remove_book(self, book, library):
        if book in library.books:
            library.books.remove(book)
            return f'"{self.name}" deleted book "{book.title}".'
        else:
            return f'"{book.title}" throws 404'

    def serialize(self):
        return json.dumps(self.__dict__)

class Library:
    def __init__(self):
        self.books = []

    def list_books(self):
        if not self.books:
            raise Exception('No books!!1')
        return books

    def serialize(self):
        return json.dumps({
            'books': [b.serialize() for b in self.books]
        })


def test():
    l = Library()
    ln = Libertarian('phil')
    b = Book('how to pet a python', 'van rossum', 3332278, 1354)
    ln.add_book(b, l)
    r = Reader('me', 123)
    r.borrow_book(b)
    print(b.serialize())
    print(r.serialize())
    print(l.serialize())
    print(ln.serialize())

test()
