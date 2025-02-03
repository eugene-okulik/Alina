class Book:
    page_material = 'paper'
    text = True

    def __init__(self, book_name, author, pages_amount, ISBN, reservation):
        self.book_name = book_name
        self.author = author
        self.pages_amount = pages_amount
        self.ISBN = ISBN
        self.reservation = reservation


class SchoolBook(Book):
    def __init__(self, book_name, author, pages_amount, ISBN, reservation, subject, group, tasks):
        super().__init__(book_name, author, pages_amount, ISBN, reservation)
        self.subject = subject
        self.group = group
        self.tasks = tasks

    def print_result(self):
        if self.reservation:
            print(f'Название:{self.book_name}, Автор:{self.author}, страниц:{self.pages_amount}, '
                  f'предмет:{self.subject}, класс:{self.group}, зарезервирована')
        else:
            print(f'Название:{self.book_name}, Автор:{self.author}, страниц:{self.pages_amount}, '
                  f'предмет:{self.subject}, класс:{self.group}')


school_book1 = SchoolBook('Математика на все века','Иванов','176',
                          '12-прп','True','Математика','10','True')
school_book2 = SchoolBook('История про историю','Петров','453',
                          '34-рат','','История','7','False')
school_book3 = SchoolBook('География для чайников','Сидоров','300',
                          '567-ук','','География','8','True')

school_book1.print_result()
school_book2.print_result()
school_book3.print_result()
