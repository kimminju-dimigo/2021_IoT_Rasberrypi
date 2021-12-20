import RPi.GPIO as GPIO
import time 

TRIGGER_PIN = 4
ECHO_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.stup(ECHO_PIN, GPIO.IN)

try:
    while True:
        GPIO.output(TRIGGER_PIN, GPIO.HIGH) #10us(1us - > 0.000001)
        time.sleep(0.00001)
        GPIO.ouput(TRIGGER_PIN, GPIO.LOW)

        while GPIO.input(ECHO_PIN)==0:
            pass
        start = time.time()
        print(start)

        while GPIO.input(ECHO_PIN)==1:
            pass
        stop =time.time()
        print(stop)

    
        duration_time = stop - start
        distance = 17160 * duration_time

        print('Distance : %01Fcm' %distance)
        time.sleep(0.1)
        
finally:
    GPIO.cleanup()
    print('Exit and cleanup')
