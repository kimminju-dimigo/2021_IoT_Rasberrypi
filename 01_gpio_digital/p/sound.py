import RPi.GPIO as GPIO
import time

LED_PIN2 = 12
SOUND_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_PIN, GPIO.IN)
GPIO.setup(LED_PIN2, GPIO.OUT)



try:
    while True:
        if GPIO.input(SOUND_PIN) == True:
            GPIO.output(LED_PIN2, True)
            print("on")
            time.sleep(0.5)
        else:
            GPIO.output(LED_PIN2, False)
            print("off")
            time.sleep(0.5)

finally: 
    GPIO.cleanup()
    print("Exit")