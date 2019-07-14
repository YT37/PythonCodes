from random import choice
flipList = []
for i in range(1, 101):
    flipList += choice(['H', 'T'])
print("Heads : ", flipList.count('H'))
print("Tails : ", flipList.count('T'))