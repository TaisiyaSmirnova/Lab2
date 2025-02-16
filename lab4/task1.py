class Vehicle:
    """
    Базовый класс для всех транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Конструктор для класса Vehicle.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self._brand = brand  # Инкапсуляция, чтобы защищать атрибут
        self._model = model
        self._year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.
        """
        return f"{self._year} {self._brand} {self._model}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление транспортного средства.
        """
        return f"Vehicle(brand='{self._brand}', model='{self._model}', year={self._year})"

    def move(self) -> str:
        """
        Символизирует движение транспортного средства.
        Метод будет перегружен в дочерних классах.
        """
        return "Транспортное средство движется."


class Car(Vehicle):
    """
    Класс для автомобилей, наследующий от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """
        Конструктор для класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param doors: Количество дверей.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self._doors = doors  # Инкапсуляция, чтобы защитить атрибут

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.
        """
        vehicle_str = super().__str__()  # Получаем строковое представление базового класса
        return f"{vehicle_str}, Двери: {self._doors}"

    def move(self) -> str:
        """
        Символизирует движение автомобиля.
        """
        return "Автомобиль едет по дороге."


class Bicycle(Vehicle):
    """
    Класс для велосипедов, наследующий от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, gear_count: int) -> None:
        """
        Конструктор для класса Bicycle.

        :param brand: Марка велосипеда.
        :param model: Модель велосипеда.
        :param year: Год выпуска велосипеда.
        :param gear_count: Количество передач.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self._gear_count = gear_count  # Инкапсуляция, чтобы защитить атрибут

    def __str__(self) -> str:
        """
        Возвращает строковое представление велосипеда.
        """
        vehicle_str = super().__str__()  # Получаем строковое представление базового класса
        return f"{vehicle_str}, Количество передач: {self._gear_count}"

    def move(self) -> str:
        """
        Символизирует движение велосипеда.
        """
        return "Велосипед движется с ветерком!"
