class Book:
    def __init__(self,name,author,price,published,year):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.published_in = published
        self.year_published = year
    
    def add_book(self):
        print("Book Name: "+self.book_name)
        print("Book Author: "+self.book_author)
        print("Book Price: "+str(self.book_price))
        print("Book was published in: "+str(self.published_in))
        print("Book Added")
        print("This Book was printed "+str(self.year_published)+" years ago")


book1 = Book("Harry Potter and the Philosopher's Stone","J.K.Rowling",1928,1997,25)
book1.add_book()

book2 = Book("Diary of a Wimpy Kid","Jeff Kinney",700,2017,5)
book2.add_book()