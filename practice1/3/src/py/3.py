firstDouble = eval(input("Введите первое число "))
secondDouble = eval(input("Введите второе число "))
print(f'Сложение {firstDouble + secondDouble}')
print(f'Вычитание {firstDouble - secondDouble}')
try:
    print(f'Деление {firstDouble / secondDouble}')
except ArithmeticError:
    print('Деление на ноль')
print(f'Умножение {firstDouble * secondDouble}')
