# TODO импортировать необходимые молули
import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
        # Считывание содержимого CSV файла
        with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csv_file:
            # Использование DictReader для чтения CSV
            reader = csv.DictReader(csv_file)

            # Преобразование строки в список словарей
            data = [OrderedDict(row) for row in reader]

        # Сериализация данных в JSON и запись в файл с отступами равными 4
        with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
