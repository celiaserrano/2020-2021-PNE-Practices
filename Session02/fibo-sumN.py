def fibosum(n):
    series = [0, 1]
    a, b = 0, 1
    for i in range(1, n - 1):
        c = b + a
        series.append(c)
        a, b = b, c

    res = 0
    for i in series:
        res =+ i




    return res



n = int(input("Enter a number for the Fibonacci sequence: " ))
print(fibosum(n))
