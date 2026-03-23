class Book:
    def __init__(self, title, gender, num_pages,author):
        self.__title = title
        self.__gender = gender
        self.__num_pages = num_pages
        self.__author = author
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title
        
    @property
    def gender(self):
        return self.__gender
    
        
    @gender.setter
    def gender(self, gender):
        self.__gender = gender
        
        
    @property
    def num_pages(self):
        return self.__num_pages
    
    @num_pages.setter
    def num_pages(self, num_pages):
        self.__num_pages = num_pages
        
        
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, author):
        self.__title = author
    
    
        