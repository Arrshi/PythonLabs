firstVar = int(input("Введите первое число "))
secondVar = int(input("Введите второе число "))

firstVar -= secondVar
secondVar += firstVar
firstVar = secondVar - firstVar

print(f'Первое число {firstVar} Второе число {secondVar}')

thirdVar = secondVar
secondVar = firstVar
firstVar = thirdVar
print(f'Первое число {firstVar} Второе число {secondVar}')
