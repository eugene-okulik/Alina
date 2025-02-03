class Book:
    page_material = 'paper'
    text = True

    def __init__(self, book_name, author, pages_amount, ISBN, reservation):
        self.book_name = book_name
        self.author = author
        self.pages_amount = pages_amount
        self.ISBN = ISBN
        self.reservation = reservation

    def print_result(self):
        if self.reservation:
            print(f'Название:{self.book_name}, Автор:{self.author}, страниц:{self.pages_amount}, '
                  f'материал:{self.page_material}, зарезервирована')
        else:
            print(f'Название:{self.book_name}, Автор:{self.author}, страниц:{self.pages_amount}, '
                  f'материал:{self.page_material}')


book1 = Book('Идиот','Достоевский','300','123','True')
book2 = Book('Мертвые души','Гоголь','280','456','')
book3 = Book('Мцыри','Лермонтов','50','789','')
book4 = Book('Горе от ума','Грибоедов','130','987','')
book5 = Book('Селекция','Линней','540','654','')

book1.print_result()
book2.print_result()
book3.print_result()
book4.print_result()
book5.print_result()
