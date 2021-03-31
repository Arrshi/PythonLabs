arr = [i for i in input().split()]

arr[0] = int(arr[0])
arr[2] = int(arr[2])


def summ(a, b):
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        print("Divide by zero!!")
        return -1
    else:
        return a / b


def subtract(a, b):
    return a - b


operations = {
    "+": summ,
    "-": subtract,
    "*": mul,
    "/": div
}

print(operations[arr[1]](arr[0], arr[2]))
