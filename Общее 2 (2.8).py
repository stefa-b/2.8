def cylinder():
    r = float(input("Enter radius: "))
    h = float(input("Enter hight: "))
    # площадь боковой поверхности цилиндра:
    side = 2 * 3.14 * r * h
    # площадь одного основания цилиндра:
    circle = 3.14 * r**2
    # полная площадь цилиндра:
    full = side + 2 * circle
    return full

square = cylinder()
print(square)