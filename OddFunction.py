def odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
    

def changeList(list, func):
    oddList = []
    for i in list:
        if func(i):
            oddList.append(i)
    return oddList


aList = range(1, 21)
print(changeList(aList, odd))
