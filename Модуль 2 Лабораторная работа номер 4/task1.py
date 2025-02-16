class ConiferTree:
    """
    Базовый класс для хвойных деревьев.
    Реализует основные свойства и методы работы с деревьями.
    """

    def __init__(self, name: str, height: float, age: int):
        if height < 0 or age < 0:
            raise ValueError("Возраст и высота не могут быть отрицательными.")
        self.name = name  # Название дерева
        self._height = height  # Высота дерева (в метрах)
        self._age = age  # Возраст дерева (в годах)

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if value < 0:
            raise ValueError("Высота не может быть отрицательной.")
        self._height = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self._age = value

    def grow(self, years: int) -> None:
        """Моделирует рост дерева за указанное количество лет."""
        if years < 0:
            raise ValueError("Количество лет роста не может быть отрицательным.")
        self.age += years
        self.height += years * 0.5  # Условная модель роста

    def __str__(self) -> str:
        return f"{self.name} (Высота: {self.height} м, Возраст: {self.age} лет)"

    def __repr__(self) -> str:
        return f"ConiferTree(name='{self.name}', height={self.height}, age={self.age})"


class Pine(ConiferTree):
    """
    Класс для сосны. Добавлено свойство количества шишек.
    """

    def __init__(self, name: str, height: float, age: int, cone_count: int):
        super().__init__(name, height, age)
        if cone_count < 0:
            raise ValueError("Количество шишек не может быть отрицательным.")
        self.cone_count = cone_count

    @property
    def cone_count(self) -> int:
        return self._cone_count

    @cone_count.setter
    def cone_count(self, value: int) -> None:
        if value < 0:
            raise ValueError("Количество шишек не может быть отрицательным.")
        self._cone_count = value

    def grow(self, years: int) -> None:
        """Добавляет логику увеличения количества шишек при росте."""
        super().grow(years)
        self.cone_count += years * 10

    def __str__(self) -> str:
        return f"{super().__str__()} (Шишек: {self.cone_count})"


class Spruce(ConiferTree):
    """
    Класс для ели. Добавлено свойство количества ветвей.
    """

    def __init__(self, name: str, height: float, age: int, branch_count: int):
        super().__init__(name, height, age)
        if branch_count < 0:
            raise ValueError("Количество ветвей не может быть отрицательным.")
        self.branch_count = branch_count

    @property
    def branch_count(self) -> int:
        return self._branch_count

    @branch_count.setter
    def branch_count(self, value: int) -> None:
        if value < 0:
            raise ValueError("Количество ветвей не может быть отрицательным.")
        self._branch_count = value

    def grow(self, years: int) -> None:
        """Добавляет логику увеличения количества ветвей при росте."""
        super().grow(years)
        self.branch_count += years * 5

    def __str__(self) -> str:
        return f"{super().__str__()} (Ветвей: {self.branch_count})"


# Примеры использования классов
if __name__ == "__main__":
    pine = Pine(name="Сосна", height=10.0, age=20, cone_count=50)
    spruce = Spruce(name="Ель", height=8.0, age=15, branch_count=100)

    print(pine)  # Сосна (Высота: 10.0 м, Возраст: 20 лет) (Шишек: 50)
    print(spruce)  # Ель (Высота: 8.0 м, Возраст: 15 лет) (Ветвей: 100)

    pine.grow(5)
    spruce.grow(3)

    print(pine)  # Сосна (Высота: 12.5 м, Возраст: 25 лет) (Шишек: 100)
    print(spruce)  # Ель (Высота: 9.5 м, Возраст: 18 лет) (Ветвей: 115)


# Тесты
def test_pine_growth():
    pine = Pine(name="Сосна", height=10.0, age=20, cone_count=50)
    pine.grow(5)

    assert pine.height == 12.5  # Рост высоты
    assert pine.age == 25  # Рост возраста
    assert pine.cone_count == 100


def test_spruce_growth():
    spruce = Spruce(name="Ель", height=8.0, age=15, branch_count=100)
    spruce.grow(3)

    assert spruce.height == 9.5  # Рост высоты
    assert spruce.age == 18  # Рост возраста
    assert spruce.branch_count == 115


def test_negative_values():
    try:
        Pine(name="Сосна", height=-1.0, age=20, cone_count=50)
    except ValueError as e:
        assert str(e) == "Возраст и высота не могут быть отрицательными."


# Запуск тестов
if __name__ == "__main__":
    test_pine_growth()
    test_spruce_growth()
