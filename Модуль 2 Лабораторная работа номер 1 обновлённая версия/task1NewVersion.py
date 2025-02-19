"""
Модуль для работы с мебелью, деревьями и социальными сетями.
Добавлена валидация типов, сеттеры, улучшена логика методов.
Реализованы doctest-примеры.
"""
from abc import ABC, abstractmethod
import doctest


class Furniture(ABC):
    """Абстрактный класс для мебели с валидацией."""
    def __init__(self, material: str, height: float, width: float) -> None:
        """
        Инициализация с проверкой типов и значений
        Пример:
        >>> table = Table("Дерево", 75, 120)
        >>> table.material
        'Дерево'

        Тест на неверные типы:
        >>> Table(123, 75, 120)
        Traceback (most recent call last):
        ...
        TypeError: Материал должен быть строкой
        """
        # Валидация типа материала
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")

        # Валидация числовых значений
        if not isinstance(height, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Высота и ширина должны быть числами")
        if height <= 0 or width <= 0:
            raise ValueError("Размеры должны быть положительными")

        self._material = material
        self._height = float(height)
        self._width = float(width)

    @property
    def material(self):
        """Геттер для материала"""
        return self._material

    @material.setter
    def material(self, value: str):
        """Сеттер с проверкой типа"""
        if not isinstance(value, str):
            raise TypeError("Материал должен быть строкой")
        self._material = value

    # Аналогичные свойства для height и width
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Высота должна быть числом")
        if value <= 0:
            raise ValueError("Высота должна быть положительной")
        self._height = float(value)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Ширина должна быть числом")
        if value <= 0:
            raise ValueError("Ширина должна быть положительной")
        self._width = float(value)

    @abstractmethod
    def use(self, activity: str) -> str:
        """Использовать мебель"""

    @abstractmethod
    def get_dimensions(self) -> tuple:
        """Получить размеры"""


class Table(Furniture):
    """Класс стола с расширенной функциональностью"""
    def use(self, activity: str = "работа") -> str:
        """
        Пример использования:
        >>> table = Table("Стекло", 80, 150)
        >>> table.use("обед")
        'Стол используется для обеда'
        """
        return f"Стол используется для {self._get_correct_form(activity)}"

    def _get_correct_form(self, word: str) -> str:
        """Возвращает слово в правильном падеже"""
        if word == "обед":
            return "обеда"
        return word

    def get_dimensions(self) -> tuple:
        """Пример:
        >>> table = Table("Дерево", 75, 120)
        >>> table.get_dimensions()
        (75.0, 120.0)
        """
        return (float(self._height), float(self._width))

class Tree(ABC):
    """Абстрактный класс дерева с валидацией"""
    def __init__(self, species: str, height: float):
        """
        Пример создания:
        >>> oak = Oak("Дуб", 15.5)
        >>> oak.species
        'Дуб'

        Проверка ошибок:
        >>> Oak(123, 10)
        Traceback (most recent call last):
        ...
        TypeError: Вид дерева должен быть строкой
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть числом")
        if height < 0:
            raise ValueError("Высота не может быть отрицательной")

        self._species = species
        self._height = float(height)

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Вид дерева должен быть строкой")
        self._species = value

    @abstractmethod
    def grow(self, years: int) -> str:
        """Рост дерева"""

    @abstractmethod
    def shed_leaves(self) -> str:
        """Сбрасывание листьев"""


class Oak(Tree):
    """Класс дуба с улучшенной логикой роста"""
    def grow(self, years: int = 1) -> str:
        """
        Пример роста:
        >>> oak = Oak("Дуб", 10)
        >>> oak.grow(5)
        'Дуб вырос на 50 см за 5 лет. Текущая высота: 10.5 м'
        """
        if not isinstance(years, int):
            raise TypeError("Годы должны быть целым числом")

        growth = years * 10  # 10 см в год
        self._height += growth / 100  # конвертация в метры
        return f"{self.species} вырос на {growth} см за {years} лет. Текущая высота: {self._height:.1f} м"

    def shed_leaves(self) -> str:
        return "Дуб сбрасывает листья осенью"


class SocialNetwork(ABC):
    """Абстрактный класс социальной сети"""
    def __init__(self, name: str, users_count: int):
        """
        Пример:
        >>> vk = VK("ВКонтакте", 97_000_000)
        >>> vk.name
        'ВКонтакте'
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(users_count, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")

        self._name = name
        self._users_count = users_count

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой")
        self._name = value

    @abstractmethod
    def add_user(self, count: int = 1) -> str:
        """Добавление пользователей"""


class VK(SocialNetwork):
    """Класс для ВКонтакте с улучшенным управлением пользователями"""
    def add_user(self, count: int = 1) -> str:
        """
        Пример добавления:
        >>> vk = VK("ВК", 10)
        >>> vk.add_user(3)
        'Добавлено 3 пользователей. Всего: 13'
        """
        if not isinstance(count, int):
            raise TypeError("Количество должно быть целым числом")
        if count <= 0:
            raise ValueError("Количество должно быть положительным")

        self._users_count += count
        return f"Добавлено {count} пользователей. Всего: {self._users_count}"

    def remove_user(self, count: int = 1) -> str:
        """Удаление пользователей"""
        if not isinstance(count, int):
            raise TypeError("Количество должно быть целым числом")
        if count <= 0:
            raise ValueError("Количество должно быть положительным")

        self._users_count = max(0, self._users_count - count)
        return f"Удалено {count} пользователей. Осталось: {self._users_count}"


if __name__ == "__main__":
    # Создание экземпляров и проверки
    ikea_table = Table("Стекло", 75.5, 120.0)
    ancient_oak = Oak("Дуб черешчатый", 25.3)
    vk = VK("ВКонтакте", 97_000_000)

    # Проверка принадлежности классам
    print(isinstance(ikea_table, Furniture))  # True
    print(type(ancient_oak) is Oak)           # True

    # Запуск тестов
    doctest.testmod(verbose=True)