# TODO Напишите функцию для поиска индекса товара
def find_item_index(items, item_to_find):
#Возвращает индекс первого вхождения товара в списке или None, если товар не найден
    try:
        return items.index(item_to_find)
    except ValueError:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции для получения индекса товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
