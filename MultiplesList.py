from random import randint as R
randList = list(R(1, 1001) for i in range(100))
print(list(filter((lambda x: x % 9 == 0), randList)))