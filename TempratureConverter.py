import time
T = int(input("What Do You Want To Convert To ? 1. Celsius  2. Fahrenheit"
              "\nEnter Number: "))
if T == 1:
    OperationC = float(input("Enter Temperature In Fahrenheit : "))
    C = 5 / 9 * (OperationC - 32)
    print("Converting...Please Wait")
    time.sleep(2)
    print("Temperature = ", C, "°C")

elif T == 2:
    OperationF = float(input("Enter Temperature In Celsius : "))
    F = (OperationF * 1.8) + 32
    print("Converting...Please Wait")
    time.sleep(2)
    print("Temperature = ", F, "°F")
