def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


def getPrimes(max_number):
    primesLst = []

    for num1 in range(2, max_number):
        if isprime(num1):
            primesLst.append(num1)

    return primesLst


maxNum = int(input("Search For Primes Up To : "))

primes = getPrimes(maxNum)
for prime in primes:
    print(prime)
