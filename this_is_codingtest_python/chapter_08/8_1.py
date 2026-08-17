def pibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return pibo(n-1) + pibo(n-2)

print(pibo(10))