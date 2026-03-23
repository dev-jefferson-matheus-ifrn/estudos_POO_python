class Library:
    def __init__(self):
        self.__books = []
        
    @property
    def books(self):
        return self.__books
    
    @books.setter
    def books(self,books):
        self.__books = books
        
    def list_all_books(self):
        for book in self.__books:
            print(book.title, book.gender, book.num_pages,book.author.name)
            
    def insert_new_book(self,book):
        self.__books.append(book)
        
    def find_book_by_author(self,author_name):
        
        for book in self.__books:
            if book.author.name == author_name:
                print(book.title, book.gender, book.num_pages,book.author.name)
                break
            
        
        
        
    