class Book:
    count = 1

    def __init__(self,title:str,author:str,year:int,):
        
        self.book_id = Book.count 
        Book.count +=1 
        self.book_title = title
        self.book_author = author
        self.book_year = year
        self.book_is_avaible = True
    
    def __str__(self):
        return(f"АЙДИ:{self.book_id}\n Название:{self.book_title}\n Автор: {self.book_author}\n Год выпуска: {self.book_year}\n Статус: {self.book_is_avaible}")
    


class Library():
    def __init__(self):
        self.books = []



    def add_book(self,book):
        if book not in self.books:

            self.books.append(book)
            print(f"Book  was successfully added")
        elif book in self.books:
            print(f"Book  is already in the Library")
        else:
            print("Error")


    def find_book(self,name):
        
        for good in self.books:
            if name == good.book_title:
                print(f"Found same title book : {good}")
                break
        else:
            print("Книга не найдена")
        
        return
    def show_all(self):
        print("Книги которые у нас есть: \n ")
        for m in self.books:
            print(f"-{m}")

    def show_all_avaibles(self):
        print("Книги которые у нас есть: \n ")
        for m in self.books:
            if m.is_avaible:
                print(m)
    def find_books_by_author(self,author):
        number = 0
        for i in self.books:
            if author.lower() in i.book_author.lower():
                number += 1
                print(f"Нашли книги с вашим автором: {i}")
        print(f"Количество книг с таким автором - {number}")

    def find_book_by_id(self, id):
        for book in self.books:
            if id == book.book_id:
                print(f"найдена книга по Айди {id}\nНазвание {book.book_title} ")
                return(book)
        else:
            print("Книг с таким Айди не найдено")
            return(None)
            

        
    def borrow_book(self,book_id):
        book = self.find_book_by_id(book_id)
        if book :
            if book.book_is_avaible:
                book.book_is_avaible = False
                print(f"Вы успешно взяли  книгу  {book.book_title}")

            else:
                print("Книга уже взята кем-то")
        
    def return_book(self,book_id):
        book = self.find_book_by_id(book_id)
        if book:
            if book.book_is_avaible:
                print("Вы не можете вернуть книгу так как книга и так у нас")
            else:
                print(f"Книга по айди: {book_id} успешно возвращена")
                book.book_is_avaible = True




                


b1 = Book("Остров Сокровищ", "Жуль-Верн", 2000 )
b2 = Book("Клоунский прикол", "Жуль-Верн",2026)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)



while True:
    print(
        """
        Приветствую вас в нашей библиотеке!
        1.Добавить Книгу
        2.Найти Книгу
        3.Найти книгу по автору
        4.Выдать Книгу
        5.Вернуть Книгу
        6.Показать доступные Книги
        7.Показать все книги
        8.Выход
        """)
    action =input("Выберите действие")
    match action:
        case "1":
            name = input("Введите Название книги")
            author = input("Введите автора")
            year_of_pub = int(input("Введите год выпуска"))
            temp_book = Book(name,author,year_of_pub)
            lib.add_book(temp_book)
            print("вы успешно добавили книгу ")
        case "2":
            name = input("Введите название книги")
            lib.find_book(name)
        case "3":
            author_name = input("Введите Автора")
            lib.find_books_by_author(author_name)
        case "4":
            id_book = input("Введите айди книги которую вы хотите взять")
            lib.borrow_book(id_book)
        case "5":
            id_book = input("Введите айди книги которую вы хотите вернуть")
            lib.return_book(id_book)
        case "6":
            lib.show_all_avaiblesh()
        case "7":
            lib.show_all()
        case "8":
            break

 







