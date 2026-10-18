import sys

# 1. Исходные данные из условия задачи
bytes_count = 1921000  # Сколько байт занимает число

# 2. Перевод байтов в мегабайты
# Сначала переводим в килобайты (делим на 1024), затем в мегабайты (еще раз делим на 1024)
kilobytes = bytes_count / 1024
megabytes = kilobytes / 1024

print(f"Число занимает: {megabytes} Мегабайт")
print(f"В килобайтах: {kilobytes} КБ")

# 3. Проверка с помощью функции getsizeof()
print("\n--- Проверка через getsizeof ---")
# Записываем число 3 в степени 9090001
number = 3 ** 9090001
size_in_bytes = sys.getsizeof(number)

print(f"Размер числа в байтах (по версии Python): {size_in_bytes}")
print(f"Размер числа в мегабайтах: {size_in_bytes / 1024 / 1024} МБ")