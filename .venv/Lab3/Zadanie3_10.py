from gpiozero import AngularServo, LED
from time import monotonic, sleep

servo = AngularServo(24, min_angle=-90, max_angle=90)
led = LED(23)

try:
    while True:
        for angle, blink_delay in ((-90, 1), (90, 0.2)):
            servo.angle = angle
            end_time = monotonic() + 3
            while monotonic() < end_time:
                led.on()
                sleep(min(blink_delay, end_time - monotonic()))
                led.off()
                remaining = end_time - monotonic()
                if remaining > 0:
                    sleep(min(blink_delay, remaining))
finally:
    led.off()
    servo.close()
    led.close()