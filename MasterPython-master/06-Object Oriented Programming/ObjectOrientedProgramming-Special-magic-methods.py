## Can we use built-in functions such as len() or print() in user defined objects
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
# we have to create string representation of above method, so that print() can be used
    def __str__(self):
        return f"{self.title} by {self.author} containing {self.pages} pages"

#Lets create len method so that len() can be used
    def __len__(self):
        return self.pages
#lets write delete method so that del() function can be used
    def __del__(self):
        return "Book object is deleted"

# Lets call above method
mybook = Book('The monk who sold his Ferrari','Robin Sharma',300)
print(mybook)
print(len(mybook))
del mybook