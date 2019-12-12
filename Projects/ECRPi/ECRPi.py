import time
import pyfirmata

board = pyfirmata.Arduino("COM7")

it = pyfirmata.util.Iterator(board)
it.start()

LM35 = board.get_pin("a:0:i")
EC = board.get_pin("a:1:i")
print("Now startting")
time.sleep(30)
print("Running")
LM35Read = LM35.read()
ECRead = EC.read()

print(f"Temp :- {int(str(LM35Read)[2:])/10}")
print(f"Conductivity :- {str(ECRead)[2:]}")

