numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

# Нахожу индекс пропущенного элемента
missing_index = numbers.index(None)

# Создаю новый список без пропущенного элемента
filtered_numbers = [num for num in numbers if num is not None]

# Вычисляю среднее арифметическое
average = sum(filtered_numbers) / (len(filtered_numbers) + 1)

# Округляю среднее до двух знаков после запятой
average = round(average, 2)

# Заменяю пропущенный элемент на среднее арифметическое
numbers[missing_index] = average

#Вывожу результат
print("Измененный список:", numbers)
