class Book:
    def __init__(self, author, title,code, disponibility = True):
        self.author = author
        self.title = title
        self.disponibility = disponibility
        self.code = code
    
    def __str__(self):
        return f"{self.author},{self.title},{self.disponibility},{self.code}"
    


