class book:
    def __init__(self , title, author, isbn, available = True ):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

       
    def display_info(self):
        print(f"{self.title} {self.author} {self.isbn} True")
