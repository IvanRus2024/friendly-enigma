# TODO Найдите количество книг, которое можно разместить на дискете
disk_capacity_mb = 1.44    # емкость дискеты в мегабайтах
pages_in_book = 100    # количество страниц в книге
lines_per_page = 50    # количество строк на странице
chars_per_line = 25    # количество символов в строке
bytes_per_char = 4        # количество байт для хранения одного символа

# Вычислю объем одной книги
total_chars_in_book = pages_in_book * lines_per_page * chars_per_line
book_size_bytes = total_chars_in_book * bytes_per_char

# Преобразую емкость дискеты в байты
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024  # 1 Мб = 1024 * 1024 байт

# Найду количество книг, которое можно разместить на дискете
num_books = int (disk_capacity_bytes // book_size_bytes)

#Выведу результат
print("Количество книг, помещающихся на дискету:", num_books)
