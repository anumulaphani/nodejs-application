
"""
Name:Anumula Phani Kumar
Date:25-01-2017
Brief Project Description:By using Graphical user interface(GUI) this program is a simple reading list that allows a user to track books they wish to read and books they have completed reading. The program maintains a list of books in a file, and each book has:
•  title, author, number of pages, whether it is required or completed (r or c)
Users can choose to see the list of required books or completed books, including a total of the number of pages of the book list. The lists will be sorted by author then by number of pages (increasing). [1]
Users can add new books and mark books as completed.
-the left side of the screen contains buttons for the user to choose actions from, and text entry fields for inputting information for a new book
-the right side contains buttons for each of the books, colour-coded based on their length
-the status bar at the top of the right side shows the number of pages to read or completed
-the status bar at the bottom of the right side shows messages about what to do, or when in list completed mode, shows the book's details when a book is clicked on
-“List Required” is the default (starting) state and shows the books that are required; clicking an item in this state marks it as completed (the button will immediately disappear)
-“List Completed” changes the right side view to show books that have been completed (no length-based colouring); clicking an item in this state shows its details in the bottom status bar
-the user can add a new book by entering text in the input fields and clicking “Add Book”


GitHub URL: https://github.com/anumulaphani/practicals-1/tree/master/assignment2
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty, StringProperty
from kivy.app import App

from book import Book
from booklist import BookList


class LeftPanel(BoxLayout):
    title_input = ObjectProperty(None)
    author_input = ObjectProperty(None)
    length_input = ObjectProperty(None)

    def insert_book(self):
        if (not self.title_input.text
                or not self.author_input.text
                or not self.length_input.text):
            self.parent.book_list_panel.status_bar_text = \
                'All fields must be completed!'
            return

        try:
            length = int(self.length_input.text)
        except Exception as e:
            print(e)
            self.parent.book_list_panel.status_bar_text = \
                'Please enter a valid number!'
            return

        if length <= 0:
            self.parent.book_list_panel.status_bar_text = \
                'Pages must be a positive integer!'
            return

        book = Book(self.title_input.text,
                    self.author_input.text,
                    length,
                    False)

        self.parent.book_list_panel.book_list.add(book)
        self.parent.book_list_panel.book_list.save()
        self.parent.book_list_panel.refresh_books(False)

        self.parent.book_list_panel.status_bar_text = \
            'Book added successfully!'

    def clear_fields(self):
        self.title_input.text = ''
        self.author_input.text = ''
        self.length_input.text = ''


class BookListPanel(GridLayout):
    total_pages_label = ObjectProperty(None)
    book_list_view = ObjectProperty(None)
    status_bar = ObjectProperty(None)
    total_pages_label_text = StringProperty()
    status_bar_text = StringProperty()

    def __init__(self, **kwargs):
        kwargs['cols'] = 1
        super(BookListPanel, self).__init__(**kwargs)
        self.book_list = BookList('books.csv')
        self.book_list_adapter = ListAdapter(data=[],
                                             args_converter=self.book_convert,
                                             cls=ListItemButton,
                                             selection_mode='single',
                                             allow_empty_selection=False)

        self.refresh_books(completed=False)
        # self.add_widget(self.book_list_view)

    def refresh_books(self, completed: bool):
        book_list_data = [book for book in self.book_list.sorted()
                          if book.completed == completed]
        self.book_list_adapter.data = book_list_data

        total_pages = self.book_list.get_total_pages(completed)

        if completed:
            self.status_bar_text = 'Select a book...'
            self.total_pages_label_text = ('Total pages completed: {}'
                                           .format(total_pages))
        else:
            self.status_bar_text = 'Click books to mark them as completed'
            self.total_pages_label_text = ('Total pages to read: {}'
                                           .format(total_pages))

    def book_convert(self, row_index, book):
            if book.is_long():
                book_color = (0.5, 0, 0, 1)  # red
            else:
                book_color = (0, 0.5, 0, 1)  # green

            return {'text': book.title,
                    'on_press': self.book_click,
                    'size_hint_y': None,
                    'height': 25,
                    'deselected_color': book_color,
                    'selected_color': book_color}

    def book_click(self, button):
        selected_book = self.book_list.get_by_title(button.text)

        if selected_book.completed:
            self.status_bar_text = str(selected_book)
        else:
            selected_book.mark_completed()
            self.refresh_books(False)

        self.book_list.save()


class MainWindow(BoxLayout):
    left_panel = ObjectProperty(None)
    book_list_panel = ObjectProperty(None)


class ReadingListApp(App):
    def build(self):
        main_window = MainWindow()
        return main_window

if __name__ == '__main__':
    ReadingListApp().run()
