
class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        if books is None:  # если книги не переданы, инициализируем пустой список
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if not self.books:  # если библиотека пуста
            return 1
        else:
            return self.books[-1].id + 1  # увеличить id последней книги на 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):  # используем enumerate для получения индекса и книги
            if book.id == book_id:
                return index
        return -1  # вернуть -1, если книга не найдена


if __name__ == '__main__':
    # Инициализируем пустую библиотеку
    empty_library = Library()
    print(empty_library.get_next_book_id())  # Проверяем следующий id для пустой библиотеки

    # Создаем список книг
    list_books = [
        Book(id_=1, name="test_name_1", pages=200),
        Book(id_=2, name="test_name_2", pages=400),
    ]

    # Инициализируем библиотеку с книгами
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для библиотеки с книгами

    # Проверяем индекс для книги, которая существует
    print(library_with_books.get_index_by_book_id(1))  # Индекс книги с id 1