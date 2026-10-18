# Задаем исходные переменные из условия
width = 17        # ширина (целое число)
height = 12.0     # высота (число с плавающей точкой)

# Вычисляем выражения
expr1 = width // 2
expr2 = width / 2.0
expr3 = height / 3
expr4 = 1 + 2 * 5

# Выводим результаты в удобном формате
print(f"1. width // 2   = {expr1}, тип: {type(expr1).__name__}")
print(f"2. width / 2.0  = {expr2}, тип: {type(expr2).__name__}")
print(f"3. height / 3   = {expr3}, тип: {type(expr3).__name__}")
print(f"4. 1 + 2 * 5    = {expr4}, тип: {type(expr4).__name__}")