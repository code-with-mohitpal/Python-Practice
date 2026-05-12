# =========================
# Q2 Book Reviews
# =========================

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        for r in self.reviews:
            print(r)


book = Book("Python Basics", "ABC")
book.add_review("Excellent")
book.add_review("Very Helpful")
print("Total Reviews:", book.count_reviews())
book.display_reviews()
