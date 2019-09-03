OrigWord = input("Make An Acronym Of : ")
OrigWord = OrigWord.upper()
list_words = OrigWord.split()

for i in list_words:
    print(i[0], end="")

print()
