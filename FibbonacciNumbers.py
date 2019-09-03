def fib(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        result = (n - 1) + (n - 2)
        return result


print(fib(3))
print(fib(4))

numFibValues = int(input("How many Fibonacci values should be found : "))

i = 1

while i < numFibValues:

    fibValue = fib(i)
    print(fibValue)
    i += 1

print("All Done")
