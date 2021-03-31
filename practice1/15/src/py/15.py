from random import randrange

randValue = randrange(0, 100)
isWin = False
count = 5

while not isWin and count > 0:
    tempInt = int(input("Введите Число : "))
    if tempInt == randValue:
        isWin = True
    count -= 1
    if isWin:
        print("Поздравляю! Вы угадали")
        print("Хотите начать сначала? (1 - ДА )")
        if input() == '1':
            count = 5
            randValue = randrange(0, 100)
            isWin = False
            continue
    elif count == 0:
        print(f'Вы проиграли. Было загадано: {randValue}')
        print("Хотите начать сначала? (1 - ДА )")
        if input() == '1':
            count = 5
            randValue = randrange(0, 100)
            continue
    if randValue > tempInt:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
