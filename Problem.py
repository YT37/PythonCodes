"""Problem1
Num = int(input("Enter A Number : "))
Range = int(input("Enter A Limit : "))
for i in range(Range):
    print(Num * i)"""
"""Problem2
def pattern(n):
    for i in range(1, n + 1):
        k = i if (i % 2 != 0) else i
        for g in range(k, n):
            if g >= k:
                print(end=" ")
        for j in range(0, k):
            if j == k - 1:
                print("*")
            else:
                print("*", end = " ")
n = 10
pattern(n)"""
"""Problem3
big = 500
small = 300
req = big - small
print(req)"""
"""Problem4
hotDog = 400
hotDogCont = 8
cont = 0
while(hotDog >= hotDogCont):
    hotDog -= hotDogCont
    cont += 1
print("Total Container :- {}".format(cont))"""
"""Problem5
seconds = [66,57,54,53,64,52,59]
l = len(seconds)
for i in range(l):
    for j in range(0,l-i-1):
        if seconds[j] > seconds[j+1]:
            seconds[j],seconds[j+1] = seconds[j+1],seconds[j]
print("The Best Time Is {}".format(seconds[0]))"""
"""Problem6
freeSize = int(input("Size Free : "))
usedSize = int(input("Size Used : "))
deletedSize = int(input("Size Of Deleted File : "))
newSize = int(input("Size Of New File : "))
usedSize -= deletedSize
usedSize += newSize
freeSize += deletedSize
freeSize -= newSize
totalSize = usedSize + freeSize
print("Size of Space Left Is {0} GB And Left Is {1} GB And Total Size Is {2} GB".format(freeSize, usedSize, totalSize))"""
"""Problem7
people = 1200000
days = 365
peopleYear = people * days
print(f"A Bus Can Carry {peopleYear:,} Peole Each Year")"""