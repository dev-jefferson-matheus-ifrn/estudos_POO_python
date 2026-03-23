from library import Library
from author import Author
from book import Book

library = Library()
author =  Author("Miyamoto Musashi")
five_rings_book = Book("Livro Dos Cinco Aneis","Estrategira", 65, author)

author2 =  Author("JK Rooling")
harry_potter = Book("Harry Potter E A Pedra filosofal","Fantasia", 150 , author2)

library.insert_new_book(five_rings_book)
library.insert_new_book(harry_potter)

library.list_all_books()

library.find_book_by_author(author2.name)