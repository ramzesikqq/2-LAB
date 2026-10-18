# Считываем координаты двух клеток (каждое число с новой строки)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# По условию клетка (1, 1) — белая.
# Сумма её координат 1 + 1 = 2 (чётная).
# Значит, если сумма координат (x + y) чётная — клетка White (белая),
# а если нечётная — клетка Black (чёрная).

color1_is_white = (x1 + y1) % 2 == 0
color2_is_white = (x2 + y2) % 2 == 0

# Проверяем, совпадают ли цвета клеток
if color1_is_white == color2_is_white:
    print("YES")
    if color1_is_white:
        print("White")
    else:
        print("Black")
else:
    print("NO")