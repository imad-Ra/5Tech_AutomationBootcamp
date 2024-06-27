class Book:
    def __init__(self, title, author, year, genre):
        self._title = title
        self._author = author
        self._year = year
        self._genre = genre

    # Getters and setters for book attributes
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.genre}"

    # Helper method to create a Book object from a dictionary
    @staticmethod
    def from_dict(book_dict):
        return Book(book_dict['title'], book_dict['author'], book_dict['year'], book_dict['genre'])

    # Helper method to convert a Book object to a dictionary
    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre
        }
        #adrbbbb
