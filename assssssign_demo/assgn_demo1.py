# csv header:
# title, author, number of pages, whether it is required or completed (r or c)
TITLE = 0
AUTHOR = 1
PAGES = 2
STATUS = 3


def load_books(filename):
    '''
    read a csv file into a list of lists

    Pseudocode:
    -- create an empty list for books
    -- open a file for reading
    -- for each line in the input file
    -- split line by a comma and append
       the result to books list
    '''
    books = []
    with open(filename, 'r') as fh: #opening a file named as filename to read
        for line in fh.read().splitlines():
            books.append(line.split(','))

    return books


def save_books(filename, books):
    '''
    write a list of lists into a csv file
    '''
    with open(filename, 'w') as fh:
        for book in books:
            args = (book[TITLE], book[AUTHOR], book[PAGES], book[STATUS])
            fh.write("{0},{1},{2},{3}\n".format(*args))


def display_menu():
    print('Menu:')
    print('R - List required books')
    print('C - List completed books')
    print('A - Add new book')
    print('M - Mark a book as completed')
    print('Q - Quit')


def get_user_input():
    c = input('>>> ')
    return c.strip().lower()


def validate_number(num_str):
    '''
    returns True if num_str is a non-negative integer
    and False otherwise (with error message printed)
    '''
    try:
        num = int(num_str)
        if num >= 0:
            return True
        else:
            print('Number must be >= 0')

    except ValueError:
        print('Invalid input; enter a valid number')

    return False


def get_string(message, numeric=False):
    '''
    Returns a non-empty string which can optionaly
    be an integer number
    '''
    have_input = False
    while not have_input:

        user_input = input(message)

        if user_input:
            if numeric:
                if validate_number(user_input):
                    have_input = True
            else:
                have_input = True
        else:
            print('Input can not be blank')

    return user_input


def column_width(books, col):
    '''
    returns the maximum width of data column
    '''
    return max(len(book[col]) for book in books)


def display_books(books, status):
    title_width = column_width(books, TITLE)
    author_width = column_width(books, AUTHOR)
    pages_width = column_width(books, PAGES)

    count = 0
    pages = 0
    for i, book in enumerate(books):
        if book[STATUS] == status:
            count = count + 1
            pages = pages + int(book[PAGES])
            args = (i, book[TITLE], title_width, book[AUTHOR], author_width,
                    book[PAGES], pages_width)
            print("{0}. {1:{2}}   by {3:{4}}     {5:{6}} pages".format(*args))
    if count:  # print it if only have some books listed
        print('Total pages for {0} books: {1}'.format(count, pages))
    else:
        print('No books')


def complete_book(books):
    '''
    Pseudocode:
     -- keep asking user to enter the number of a book
        until they enter a valid input
     -- check the current status of the book:
     -- if the book is marked as required, change it to completed
     -- otherwise do nothing and display error message
    '''
    have_number = False
    while not have_number:
        print('Enter the number of a book to mark as completed')
        user_input = get_user_input()
        if validate_number(user_input):
            n = int(user_input)
            if n < len(books):
                have_number = True
            else:
                print('Number must be < {0}'.format(len(books)))

    if books[n][STATUS] == 'r':
        books[n][STATUS] = 'c'
        print('{0} by {1} marked as completed'.format(books[n][TITLE], books[n][AUTHOR]))
    else:
        print('That book is already completed')

    return books


def main():
    filename = 'books.csv'#assinging a file to books.csv file
    books = load_books(filename)#assigning a file load_books to books

    print('Reading List 1.0 - by MY NAME')
    print(' {0} books loaded from {1}'.format(len(books), filename))#printing the size of the book to the books loaded

    running = True
    while running:

        display_menu()
        answer = get_user_input()
        if answer == 'r':
            print('Required books:')
            display_books(books, 'r')

        elif answer == 'c':
            print('Completed books:')
            display_books(books, 'c')

        elif answer == 'a':
            title = get_string('Title: ')
            author = get_string('Author: ')
            pages = get_string('Pages: ', numeric=True)

            books.append([title, author, str(pages), 'r'])
            print('{0} by {1}, ({2} pages) added to reading list'.format(title, author, pages))#printing the title ,author,pages to the reading list

        elif answer == 'm':
            print('Required books:')
            display_books(books, 'r')

            books = complete_book(books)

        elif answer == 'q':
            running = False

        else:
            print('Invalid menu choice')

    save_books(filename, books)
    print('{0} books saved to {1}'.format(len(books), filename))#printing the size of the books using .format
    print('Have a nice day :)')


if __name__ == '__main__':
    main()

