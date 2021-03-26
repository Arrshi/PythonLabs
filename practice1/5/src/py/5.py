i = [eval(a) for a in input().split()]


def func(t):
    return i[0] + i[1] * t - (9.8 * t * t) / 2


print(f'Расстояние {func(i[2])}')
