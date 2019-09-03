import time

choice = int(
    input(
        "What Do You Want To Convert To ? 1. Celsius  2. Fahrenheit" "\nEnter Number: "
    )
)
if choice == 1:
    intc = float(input("Enter Temperature In Fahrenheit : "))
    c = 5 / 9 * (intc - 32)
    print("Converting...Please Wait")
    time.sleep(2)
    print(f"Temperature =  {c} °C")

elif choice == 2:
    intf = float(input("Enter Temperature In Celsius : "))
    f = (intf * 1.8) + 32
    print("Converting...Please Wait")
    time.sleep(2)
    print(f"Temperature =  {f} °F")
