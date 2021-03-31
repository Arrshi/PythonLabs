import itertools

pair = []
sums = []


def recursive(s):
    if s == 0:
        return sums.append(sum(list(pair[0])))
    else:
        return sums.append(sum(list(pair[s]))), recursive(s - 1)


def resur_find(n):
    if sums[n] == s:
        return pair[n]
    elif n == 0:
        return -1
    else:
        return resur_find(n - 1)


s, l1, r1, l2, r2 = map(int, input().split())
if l1 > r1 or l2 > r2:
    print('Неправильные начальные условия')

x1 = list(range(l1, r1 + 1, 1))
x2 = list(range(l2, r2 + 1, 1))
pair = list(itertools.product(x1, x2))
recursive(len(pair) - 1)
sums.reverse()
print(resur_find(len(sums) - 1))
