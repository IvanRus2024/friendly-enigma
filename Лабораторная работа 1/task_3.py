list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2

# Создание первой команды, используя срез списка
first_team = list_players[:middle_index]

# Создание второй команды, начиная с индекса середины до конца списка
second_team = list_players[middle_index:]

#Вывод результата
print(first_team)
print(second_team)
