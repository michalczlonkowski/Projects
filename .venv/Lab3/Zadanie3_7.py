from gpiozero import LED
from time import sleep
led = LED(23)
tryb = "wolno"
#tryb = "szybko"
while True:
    if tryb == "wolno":
        led.on()
        sleep(1)
        led.off()
        sleep(1)
    else:
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)