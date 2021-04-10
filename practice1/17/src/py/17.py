from enum import Enum


class Colors(Enum):
    RED = 1
    BLACK = 2


class Color:
    def __init__(self):
        self.reds = (1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36)
        self.blacks = (2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 29, 31, 33, 35)

    def checkColor(self, num):
        return Colors.RED if self.reds.__contains__(num) else Colors.BLACK


resultNumber = int(input())
numbersArray = [0] * 36
missingNumbers = [i for i in range(0, 37)]
k = 12
redsCount = 0
blacksCount = 0
colors = Color()

while resultNumber != -1:
    numbersArray[resultNumber - 1] += 1
    if missingNumbers.__contains__(numbersArray):
        missingNumbers.remove(resultNumber)
    print(numbersArray.index(max(numbersArray))+1)
    print(missingNumbers)
    if colors.checkColor(resultNumber) is Colors.RED:
        redsCount += 1
    else:
        blacksCount += 1
    k -= 1

    print(redsCount, blacksCount, sep=' ')
    if k == 0:
        missingNumbers = [i for i in range(0, 37)]
        redsCount = 0
        blacksCount = 0
    resultNumber = int(input())