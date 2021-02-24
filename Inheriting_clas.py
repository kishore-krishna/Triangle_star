class Book():  # superclass
    def __init__(self, author, name):
        self.author = author
        self.name = name

    def __str__(self):
        return '"{}" by {}'.format(self.name, self.author)


class PaperBook(Book):  # subclass1  #inheriting from superclass
    def __init__(self, author, name):
        Book.__init__(self, author, name)


class Ebook(Book):  # subclass2
    def __init__(self, author, name):
        Book.__init__(self, author, name)


shelf1 = Book('JK Rowling', 'Harry Potter')
shelf2 = Book('Stephanie meyer', 'Twilight')

print(shelf1)
print(shelf2)
