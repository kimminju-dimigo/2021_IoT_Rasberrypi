import RPi.GPIO as GPIO
import time

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

    while True:

        val1 = GPIO.input(SWITCH_PIN)
        if val1 == GPIO.HIGH:
            print("light off")
            GPIO.output(LED_PIN1, val1)

            if GPIO.input(SOUND_PIN) == True:
                GPIO.output(LED_PIN2, True)
                GPIO.output(LED_PIN1, False)
                time.sleep(0.01)

                val = GPIO.input(PIR_PIN)
                if val == GPIO.HIGH:
                    print('움직임 감지')
                    GPIO.output(LED_PIN2, True)

                else :
                    print('움직임 없음')
                    GPIO.output(LED_PIN2, False)

                time.sleep(0.5)
                
            else : 
                GPIO.output(LED_PIN1, True)
                GPIO.output(LED_PIN2, False)
                time.sleep(0.01)

       
               


finally:
    GPIO.cleanup()
    print('Exit and cleanup')