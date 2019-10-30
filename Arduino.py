import pyfirmata
import time

board = pyfirmata.Arduino("COM4")

it = pyfirmata.util.Iterator(board)
it.start()

pot = board.get_pin("a:0:i")
button = board.get_pin("d:10:i")
led = board.get_pin("d:11:p")
led1 = board.get_pin("d:13:o")

while True:
    potRead = pot.read()
    switchRead = button.read()

    if potRead is not None:
        led.write(potRead)

    if switchRead:
        led1.write(1)

    else:
        led1.write(0)

    time.sleep(0.1)
