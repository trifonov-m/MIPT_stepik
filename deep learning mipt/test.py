import math


def cumsum_and_erase(a, erase=1):
    ch = a[0]
    if ch != erase:
        B = [ch]
    else:
        B = []
    for i in range(1, len(a)):
        ch += a[i]
        if ch != erase:
            B.append(ch)
    return B


def f(x):
    return (math.tan(x) * math.log(math.cos(x**2) + 1))


x = 0
x0 = 10**(-6)
print(f'{(f(x + x0) - f(x)) / x0: .2f}')

