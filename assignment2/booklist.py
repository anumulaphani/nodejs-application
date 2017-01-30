from operator import attrgetter
from book import Book


class BookList:
    def __init__(self, path: str):
        if not path:
            self.book_list = []
            return
        self.load(path)

    def get_by_title(self, title: str):
        for book in self.book_list:
            if book.title == title:
                return book
        return False

    def add(self, book: Book):
        found_book = self.get_by_title(book.title)
        if found_book:
            return found_book
        self.book_list.append(book)
        return Book

    def get_total_pages(self, is_completed=False):
        return sum([book.length for book in self.book_list
                    if book.completed == is_completed])

    def load(self, path='books.csv'):
        self.book_list = []
        try:
            with open(path) as data_file:
                for line in data_file:
                    self.book_list.append(BookList.load_book_line(line))
        except EnvironmentError as e:
            print(e)

    @staticmethod
    def load_book_line(line: str):
        raw_data_list = line.strip().split(',')
        return Book(*raw_data_list[0:2],
                    length=int(raw_data_list[2]),
                    completed=raw_data_list[3] == 'c')

    def save(self, path='books.csv'):
        try:
            with open(path, 'w') as data_file:
                for book in self.book_list:
                    data_file.write(BookList.save_book_line(book) + '\n')
        except EnvironmentError as e:
            print(e)

    @staticmethod
    def save_book_line(book: Book):
        return ','.join([book.title,
                         book.author,
                         str(book.length),
                         book.completed_str()[0]])

    def sorted(self, sort_by=None):
        """Sort books by default: author then number of pages."""
        if not sort_by:
            sort_by = ['author', 'length']

        return sorted(self.book_list, key=attrgetter(*sort_by))
