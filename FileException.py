try:
    myFile = open("File.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)

else:
    print("File :", myFile.read())
    myFile.close()

finally:
    print("Finished Working With File")
