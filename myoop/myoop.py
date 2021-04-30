import main

class Book():

    '''
    This is a parent class.
    '''

    def __init__(self, name = 'NAME', page = 0, author = 'AUTHOR'):
        self.name = name
        self.page = page
        self.author = author

    def book_info(self):
         raise NotImplementedError ("Subclass must implement this abstract method.\n")


class ScienceBook(Book):

    '''
    This is a child class.
    '''

    def book_info(self):
        return ("Book: {}, Page: {}, Author: {}\n".format(self.name, self.page, self.author))

    def book_type(self):
        print('Book type: Science.')
        print('Current time from global x outside class is {}\n'.format(main.x))

    def __str__(self): 
        return '{} is written by {} has {} page(s), which is a science catagory book.\n'.format(self.name, self.author, self.page)


class CommerceBook(Book):

    '''
    This is a child class.
    '''

    def book_info(self):
        return ("Book: {}, Page: {}, Author: {}\n".format(self.name, self.page, self.author))

    def book_type(self):
        print('Book type: Commerce.')
        print('Current time from global x outside class is {}\n'.format(main.x))

    def __str__(self): 
        return '{} is written by {} has {} page(s), which is a commerce catagory book.\n'.format(self.name, self.author, self.page)



