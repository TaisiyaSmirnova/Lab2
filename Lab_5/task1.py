import doctest

class House:
    def __init__(self, year_of_construction: float, height:float):
        """
        Создание и подготовка к работе объекта "Дом"

        :param year_of_construction: Год постройки здания
        :param height: Высота здания в метрах

        Примеры:
        >>> house = House(1984, 9460)  # инициализация экземпляра класса
        """
        if not isinstance(year_of_construction, (int, float)):
            raise TypeError("Год постройки должен  быть int или float")
        if height < 0:
            raise ValueError("Год постройки не может быть отрицательным")

        self.year_of_construction = year_of_construction

        if not isinstance(height, (int, float)):
            raise TypeError("Высота здания должна быть int или float")
        if height < 0:
            raise ValueError("Высота здания не может быть отрицательной")

        self.height = height

    def is_year_real(self) -> bool:
        """
        Функция которая проверяет реалистичность года постройки здания

        :return: Является ли год постройки здания положительным числом

        Примеры:
        >>> house = House(1890, 0)
        >>> house.is_year_real()
        """
        ...

    def exceeding_altitude(self) -> bool:
        """
        Проверка превышения высоты здания.

        :raise ValueError: Если высота здания больше высоты самого высокого здания на данный момент, то вызываем ошибку

        Примеры:
        >>> house = House(1284, 890)
        >>> house.exceeding_altitude()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

import doctest


class Hotel:
    def __init__(self, number_of_rooms: float, number_of_stars: float):
        """
        Создание и подготовка к работе объекта "Отель"

        :param number_of_rooms: Количество номеров
        :param number_of_stars: Количество звезд

        Примеры:
        >>> hotel = Hotel(300, 5)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_rooms, (int, float)):
            raise TypeError("Количество номеров должно быть int или float")
        if number_of_rooms >= 450:
            raise ValueError("Количество номеров не может быть больше 450")


        self.number_of_rooms = number_of_rooms

        if not isinstance(number_of_stars, (int, float)):
            raise TypeError("Количество звезд должно быть int или float")
        if number_of_stars >= 6:
            raise ValueError("Максимальное количество звезд в отеле - 5")

        self.number_of_stars = number_of_stars

    def is_rooms(self) -> bool:
        """
        Функция которая проверяет количетсво номеров в отеле

        :return: Количество номеров в отеле бульше нуля, но меньше 450

        Примеры:
        >>> hotel = Hotel(300, 4)
        >>> hotel.is_rooms()
        """
        ...

    def stars_in_hotel(self) -> bool:
        """
        Проверяем количество звезд в отеле.

        :raise ValueError: Если звезд больше 5, то выдает ошибку
        Примеры:
        >>> hotel = Hotel(120, 3)
        >>> hotel.stars_in_hotel()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

import doctest


class Notebook:
    def __init__(self, sheets: float, number_of_storks: float):
        """
        Создание и подготовка к работе объекта "Тетрадь"

        :param sheets: Количество листков в тетрадке
        :param number_of_storks: Количество строк на одном тетрадном листке

        Примеры:
        >>> hotel = Notebook(48, 23)  # инициализация экземпляра класса
        """
        if not isinstance(sheets, (int, float)):
            raise TypeError("Количество листков должно быть int или float")
        if sheets <= 0:
            raise ValueError("Количество листков в тетради не может быть меньше 0")

        self.sheets = sheets

        if not isinstance(number_of_storks, (int, float)):
            raise TypeError("Количество строк должно быть int или float")
        if number_of_storks > 23:
            raise ValueError("Количество строк на одном листке не может быть меньше 23")

        self.number_of_storks = number_of_storks

    def sheets_in_notebook(self) -> bool:
        """
        Функция которая проверяет количетсво листков в тетради

        :return: Количество листков не может быть отрицательным

        Примеры:
        >>> notebook = Notebook(180, 15)
        >>> notebook.sheets_in_notebook()
        """
        ...

    def storks_on_sheet(self) -> bool:
        """
        Проверяем количество строк на листке

        :raise ValueError: Если строк более 23, то выдает ошибку
        Примеры:
        >>> notebook = Notebook(48, 20)
        >>> notebook.storks_on_sheet()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


















