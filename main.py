import datetime
global x
x = datetime.datetime.now()

from myoop import myoop

if __name__ == '__main__':

    print('\n\n')

    sci_book = myoop.ScienceBook('Physics',102,'Shahjahan Topon')

    print(sci_book.book_info())
    sci_book.book_type()


    com_book = myoop.CommerceBook('Accounting',172)

    print(com_book.book_info())
    com_book.book_type()

    print(sci_book)
    print(com_book)

