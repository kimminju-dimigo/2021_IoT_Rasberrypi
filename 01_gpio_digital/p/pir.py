
import RPi.GPIO as GPIO
import time

LED_PIN2 = 12
PIR_PIN = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def switchPressed(channel):
    print("감지")
    GPIO.output(LED_PIN2, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(LED_PIN2, GPIO.LOW)

GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=switchPressed)

try:
    GPIO.output(LED_PIN2, GPIO.LOW)
finally:
    GPIO.cleanup()
    print('Exit and cleanup')
