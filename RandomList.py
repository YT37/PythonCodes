import random

numList = []

for i in range(5):
    numList.append(random.randrange(1, 10))

for i in numList:
    print(i)
