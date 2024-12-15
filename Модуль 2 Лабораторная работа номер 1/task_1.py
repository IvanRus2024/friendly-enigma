import doctest
from abc import ABC, abstractmethod
'''Импорт билиотек:
Doctest, модуль, позволяющий тестировать код с помощью встроенных примеров, которые находятся в документации функций и классов.
Abc, модуль для работы с абстрактными базовыми классами (ABC), позволяет создавать абстрактные методы, которые должны быть реализованы в дочерних классах.
'''

class Furniture(ABC):
    """Абстрактный класс для мебели."""

    def __init__(self, material: str, height: float, width: float) -> None:#Конструктор принимает три параметра: материал, высоту и ширину.
        """
        Инициализация класса Furniture.

        :param material: Материал, из которого изготовлена мебель.
        :param height: Высота мебели в сантиметрах.
        :param width: Ширина мебели в сантиметрах.

        :raises ValueError: Если высота или ширина отрицательны.

        >>> table = Table("Дерево", 75, 120)
        >>> table.material
        'Дерево'
        """
        if height <= 0 or width <= 0:
            raise ValueError("Высота и ширина должны быть положительными.")

        self.material = material
        self.height = height
        self.width = width

    @abstractmethod
    def use(self) -> str:
        """Использовать мебель."""
        ...

    @abstractmethod
    def get_dimensions(self) -> tuple:
        """Получить размеры мебели."""
        ...
#Эти методы объявлены как абстрактные, любой класс, который наследует Furniture, должен реализовать эти методы.

class Table(Furniture):
    """Класс для стола."""

    def use(self) -> str:#Метод use возвращает строку о том, как используется стол.
        """Использовать стол."""
        return "Стол используется для работы или еды."

    def get_dimensions(self) -> tuple:#Метод get_dimensions возвращает размеры стола в виде - (высота, ширина).
        """Получить размеры стола."""
        return self.height, self.width


class Tree(ABC):
    """Абстрактный класс для дерева."""

    def __init__(self, species: str, height: float) -> None:
        """
        Инициализация класса Tree.

        :param species: Вид дерева.
        :param height: Высота дерева в метрах.

        :raises ValueError: Если высота отрицательна.

        >>> oak = Oak("Дуб", 20)
        >>> oak.species
        'Дуб'
        """
        if height < 0:
            raise ValueError("Высота дерева не может быть отрицательной.")

        self.species = species
        self.height = height

    @abstractmethod
    def grow(self) -> str:
        """Дерево растет."""
        ...

    @abstractmethod
    def shed_leaves(self) -> str:
        """Дерево сбрасывает листья."""
        ...


class Oak(Tree):
    """Класс для дуба."""

    def grow(self) -> str:#Метод grow возвращает сообщение о том, как растет дуб
        """Дерево растет."""
        return "Дуб растет медленно, но уверенно."

    def shed_leaves(self) -> str:#Метод shed_leaves сообщает о сбрасывании листьев осенью.
        """Дерево сбрасывает листья."""
        return "Дуб сбрасывает листья осенью."


class SocialNetwork(ABC):
    """Абстрактный класс для социальной сети."""

    def __init__(self, name: str, users_count: int) -> None:
        """
        Инициализация класса SocialNetwork.

        :param name: Название социальной сети.
        :param users_count: Количество пользователей.

        :raises ValueError: Если количество пользователей отрицательно.

        >>> vk = Vk("ВКонтакте", 100000000)
        >>> vk.name
        'ВКонтакте'
        """
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")

        self.name = name
        self.users_count = users_count

    @abstractmethod
    def add_user(self) -> str:
        """Добавить пользователя в сеть."""
        ...

    @abstractmethod
    def remove_user(self) -> str:
        """Удалить пользователя из сети."""
        ...


class Vk(SocialNetwork):
    """Класс для ВКонтакте."""

    def add_user(self) -> str:
        """Добавить пользователя в сеть."""
        return "Пользователь добавлен в ВКонтакте."

    def remove_user(self) -> str:
        """Удалить пользователя из сети."""
        return "Пользователь удален из ВКонтакте."


if __name__ == "__main__":
    doctest.testmod()