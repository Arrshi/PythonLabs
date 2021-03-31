import math


def triangle_by_length():
    a = eval(input("Введите значение a= "))
    b = eval(input("Введите значение b= "))
    c = eval(input("Введите значение c= "))
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def triangle_by_dots():
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0


method = input("Метод : ")

operations = {
    "1": triangle_by_length,
    "2": triangle_by_dots
}

print(operations[method]())
