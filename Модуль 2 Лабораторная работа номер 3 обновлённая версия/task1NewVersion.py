# Базовый класс книги
class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        # Название и автор книги задаются при создании объекта
        self._name = name  # Приватный атрибут для защиты от изменения
        self._author = author  # Приватный атрибут для защиты от изменения

    # Свойство для получения названия книги (только чтение)
    @property
    def name(self):
        return self._name

    # Свойство для получения автора книги (только чтение)
    @property
    def author(self):
        return self._author

    # Метод для строкового представления объекта (для пользователя)
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    # Метод для строкового представления объекта (для разработчика)
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

# Класс для бумажных книг, наследуется от Book
class PaperBook(Book):
    """Класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        # Инициализация базового класса
        super().__init__(name, author)
        # Установка значения pages через сеттер для валидации
        self.pages = pages  # добавлен сеттер

    # Свойство для получения количества страниц (только чтение)
    @property
    def pages(self):
        return self._pages

    # Сеттер для количества страниц
    @pages.setter  # добавлен сеттер
    def pages(self, value: int):
        # Проверка на корректность значения страниц (должно быть положительным целым числом)
        if not isinstance(value, int):  # Проверка типа
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:  # Проверка на положительность
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = value

# Класс для аудиокниг, наследуется от Book
class AudioBook(Book):
    """Класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        # Инициализация базового класса
        super().__init__(name, author)
        # Установка значения duration через сеттер для валидации
        self.duration = duration  # добавлен сеттер

    # Свойство для получения продолжительности книги (только чтение)
    @property
    def duration(self):
        return self._duration

    # Сеттер для продолжительности
    @duration.setter  # добавлен сеттер
    def duration(self, value: float):
        # Проверка на корректность значения продолжительности (должно быть положительным числом)
        if not isinstance(value, (int, float)):  # Проверка типа
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:  # Проверка на положительность
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

# Пример использования классов:
try:
    # Создание объектов книг
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)  # Бумажная книга
    audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)  # Аудиокнига

    # Вывод информации о книгах в удобном формате (__str__)
    print(paper_book)  # Книга Война и мир. Автор Лев Толстой
    print(audio_book)  # Книга 1984. Автор Джордж Оруэлл

    # Вывод информации о книгах в формате для разработчиков (__repr__)
    print(repr(paper_book))  # PaperBook(name='Война и мир', author='Лев Толстой', pages=1225)
    print(repr(audio_book))   # AudioBook(name='1984', author='Джордж Оруэлл', duration=11.50)

except ValueError as e:
    # Обработка ошибок при создании объектов с некорректными данными
    print(e)
except TypeError as e:
    print(e)