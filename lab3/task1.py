class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс бумажной книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise ValueError(f"Количество страниц должно быть целым числом, получено: {type(value).__name__}.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()} (Бумажная книга, {self.pages} страниц)"


class AudioBook(Book):
    """ Класс аудиокниги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError(f"Продолжительность должна быть числом, получено: {type(value).__name__}.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной.")
        self._duration = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

# Примеры использования классов
paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
audio_book = AudioBook("Звонок", "Кен Кизи", 7.5)

print(paper_book)  # Книга '1984'. Автор Джордж Оруэлл (Бумажная книга, 328 страниц)
print(audio_book)  # Книга Звонок. Автор Кен Кизи
