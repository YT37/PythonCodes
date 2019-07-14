def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def getPrimes(max_number):
    list_of_primes = []
    for num1 in range(2, max_number):
        if isprime(num1):
            list_of_primes.append(num1)
    return list_of_primes


maxNum = int(input("Search For Primes Up To : "))
list_of_primes = getPrimes(maxNum)
for prime in list_of_primes:
    print(prime)
