import RPi.GPIO as GPIO
import time


PIR_PIN =2
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

time.sleep(1)
print('PIR READY...')

try:
    while True:
        val = GPIO.input(PIR_PIN)
        if val == GPIO.HIGH:
            print('움직임 감지')
        else :
            print('움직임 없음')
        
        time.sleep(1)
finally:
    GPIO.cleanup()
    print('Exit and cleanup')