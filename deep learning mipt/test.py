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

A = [5, 1, 4, 5, 14]
B = cumsum_and_erase(A, erase=10)
print(B)


