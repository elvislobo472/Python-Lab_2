class Lib_Mange:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year, topic):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = {
            "title": title,
            "author": author,
            "publisher": publisher,
            "volume": volume,
            "year": year,
            "topic": topic
        }
        print(f"Book '{title}' added successfully.")

    def rem_bk(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed successfully.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def getbk_dets(self, isbn):
        return self.books.get(isbn, f"No book found with ISBN {isbn}.")

    def srch_bk(self, query, by='title'):
        results = [book for book in self.books.values() if query.lower() in book[by].lower()]
        return results if results else f"No books found by {by}: {query}"

    def list_books(self):
        return self.books.values()

    def update_dets(self, isbn, **kwargs):
        if isbn not in self.books:
            print(f"No book found with ISBN {isbn}.")
            return
        self.books[isbn].update(kwargs)
        print(f"Book with ISBN {isbn} updated successfully.")

    def check_avail(self, isbn):
        return isbn in self.books

