from gpiozero import LED
from time import sleep
led = LED(23)
czas = 1
# czas = 0.1
while True:
    led.on()
    sleep(czas)
    led.off()
    sleep(czas)