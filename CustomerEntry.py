customers = []
while True:
    createEntry = input("Enter Customer (Y/No) : ")
    createEntry = createEntry[0].lower()
    if createEntry == "n":
        break
    else:
        fName, lName = input("Enter Customer Name : ").split()
        customers.append({'fName': fName, 'lName': lName})
for cust in customers:
    print(cust['fName'], cust['lName'])