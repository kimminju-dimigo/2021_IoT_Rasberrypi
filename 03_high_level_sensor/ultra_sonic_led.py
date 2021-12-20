import RPi.GPIO as GPIO
import time 

TRIGGER_PIN = 8
ECHO_PIN = 11
LED_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(TRIGGER_PIN, GPIO.HIGH) #10us(1us - > 0.000001)
        time.sleep(0.00001)
        GPIO.output(TRIGGER_PIN, GPIO.LOW)

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
       

        if distance <=20:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print('LED ON')
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print('LED OFF')
    time.sleep(0.1)

        
finally:
    GPIO.cleanup()
    print('Exit and cleanup')
