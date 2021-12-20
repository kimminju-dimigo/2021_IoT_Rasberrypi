import RPi.GPIO as GPIO
import time


PIR_PIN = 4
LED_PIN2 = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR_PIN, GPIO.IN)


GPIO.setup(LED_PIN2, GPIO.OUT)


time.sleep(2)
print('PIR READY...')

try:
    while True:
        val = GPIO.input(PIR_PIN)
        if val == GPIO.HIGH:
            print('움직임 감지')
            GPIO.output(LED_PIN2, True)

        else :
            print('움직임 없음')
            GPIO.output(LED_PIN2, False)

        time.sleep(2)
finally:
    GPIO.cleanup()
    print('Exit and cleanup')