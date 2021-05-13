from random import random
from math import sqrt
from multimethod import multimethod


def read():
    count = int(input("количество чисел требующий сортировки: "))
    firstLine = [int(i) for i in input().split()]
    if count == len(firstLine):
        return firstLine
    restOfLines = [[int(j) for j in input().split()] for i in range(int(sqrt(count) - 1))]
    restOfLines.append(firstLine)
    d = dict()
    d[""] = restOfLines
    return d


@multimethod
def bozoSort(a, b, c, bool=True):
    return bozoSort([a, b, c], bool)


@multimethod
def bozoSort(a: list, bool=True):
    isSorted = False
    while not isSorted:
        index1 = int(random() * len(a))
        index2 = int(random() * len(a))
        a[index1], a[index2] = a[index2], a[index1]
        isSorted = True
        for i in range(1, len(a)):
            if (a[i - 1] > a[i]) if bool else (a[i - 1] < a[i]):
                isSorted = False
                break
    return a


@multimethod
def bozoSort(a: dict, bool=True):
    a = bozoSort([l for b in a[""] for l in b], bool)
    print(a)
    list = []
    for i in range(0, len(a), int(sqrt(len(a)))):
        tempList = []
        for j in range(i, int(i + sqrt(len(a)))):
            tempList.append(a[j])
        list.append(tempList)
    return list


arr = read()
try:
    print(bozoSort(arr[0], arr[1], arr[2]))
    print(bozoSort(arr[0], arr[1], arr[2], False))
except IndexError: {}
except KeyError: {}
print(bozoSort(arr))
print(bozoSort(arr, False))