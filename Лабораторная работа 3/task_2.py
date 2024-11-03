# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):
    # Разделение строк на списки участников с использованием заданного разделителя
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Нахождение пересечения двух множеств
    common_participants = participants1.intersection(participants2)

    # Сортировка общего списка и возвращение его в виде списка
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

# Проверка работы функции с разделителем "|"
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common_participants)
