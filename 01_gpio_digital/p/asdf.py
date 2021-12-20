import RPi.GPIO as GPIO
import time

flag = True
fflag = False

LED_PIN1 = 13
LED_PIN2 = 12

PIR_PIN = 4
SOUND_PIN = 22
SWITCH_PIN = 21
GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(SOUND_PIN, GPIO.IN)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN)

pwm = GPIO.PWM(LED_PIN2, 50)
pwm.start(0)


GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운

time.sleep(2)
print('light ready!!')
time.sleep(1)


try:

    GPIO.output(LED_PIN1, True)

    while True:        
        val = GPIO.input(SWITCH_PIN)
        if val == True:
            print('clean up and exit')
            GPIO.cleanup()

        val = GPIO.input(SOUND_PIN)
        if val == True:
            GPIO.output(LED_PIN2,True)
            print('on')
            time.sleep(2)
        else:
            print("NO!")

finally:
    GPIO.cleanup()
    print('Exit and cleanup')