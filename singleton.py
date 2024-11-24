class LibraryCatalog:
    _instance = None
    _books = []
    _observers = []

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(LibraryCatalog, cls).__new__(cls)
        return cls._instance

    def add_book(self, book):
        self._books.append(book)
        self.notify_observers(f"The book '{book}' has been added to the catalog.")

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)
            self.notify_observers(f"The book '{book}' has been removed from the catalog.")

    def get_books(self):
        return self._books

    def find_book(self, title):
        return [book for book in self._books if book.lower() == title.lower()]

    """ Observer """
    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)





