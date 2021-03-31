def isPrime(num):
    d = 2
    while d * d <= num and num % d == 0:
        d += 1
    return d * d > num


a = int(input())
print(isPrime(a))
