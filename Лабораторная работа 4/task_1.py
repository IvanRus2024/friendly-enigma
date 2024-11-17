import json

# TODO решите задачу
def task() -> float:
    # Чтение данных из JSON файла
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Инициализация переменной для суммы произведений
    total_sum = 0.0

    # Прохождение по каждому элементу в загруженных данных
    for entry in data:
        # Извлечение значения "score" и "weight"
        score = entry.get("score", 0)  # Если ключа нет, используем 0 по умолчанию
        weight = entry.get("weight", 0)  # Если ключа нет, используем 0 по умолчанию

        # Вычисление произведения и добавление к общей сумме
        total_sum += score * weight

    # Возвращение суммы, округленной до 3 знаков после запятой
    return round(total_sum, 3)

# Печать результата выполнения функции
print(task())
