base = input("Enter A String To Hide : ")

secret = ""

for char in base:
    secret += str(ord(char) - 23)

print("Secret Message : ", secret)

base = ""

for i in range(0, len(secret) - 1, 2):
    code = secret[i] + secret[i + 1]
    base += chr(int(code) + 23)

print("Original Message :", base)
