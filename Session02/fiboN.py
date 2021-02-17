
def fibon(n):
    series = [0, 1]
    a, b = 0, 1
    for i in range(1, n - 1):
        c = b + a
        series.append(c)
        a, b = b, c

    return series

n = int(input("Enter a number for the Fibonacci sequence: " ))
series = fibon(n)
print("5th Fibonacci term: ", series[5])