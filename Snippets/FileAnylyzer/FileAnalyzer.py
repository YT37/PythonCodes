with open("File.txt", encoding="utf-8") as myFile:

    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:
            break

        print("Line", lineNum)

        wordList = line.split()

        print("Number of Words :", len(wordList))

        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        avgNumChars = charCount / len(wordList)

        print("Avg Word Length : {:.2}".format(avgNumChars))

        lineNum += 1
