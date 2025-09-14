from Book import book

class Member:
    def __init__(self, name , membership_id , borrowed_books):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = borrowed_books

member1 = Member("Ahmed","456456",["English" , " Arabic" , "Math"])
member2 = Member("Mona" , "1234" , ["Arabic" , "English" ,"Math"])

 