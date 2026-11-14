class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("Python Basics", "Ali")
book2 = Book("AI for Beginners", "Sara")
book3 = Book("Data Science", "Ahmed")

book1.display_info()
book2.display_info()
book3.display_info()