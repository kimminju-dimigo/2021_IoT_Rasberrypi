import RPi.GPIO as GPIO

LED_PIN1  = 19
LED_PIN2 = 20
LED_PIN3 = 21

SWITCH_PIN1 = 13
SWITCH_PIN2 = 12
SWITCH_PIN3 = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)

#누르지 않았을 떄 : 0, 눌렀을 때: 1

GPIO.setup(SWITCH_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



try:
    while True:
        val1 = GPIO.input(SWITCH_PIN1)
        print(val1)
        GPIO.output(LED_PIN1, val1)

        val2 = GPIO.input(SWITCH_PIN2)
        print(val2)
        GPIO.output(LED_PIN2, val2)
        
        val3 = GPIO.input(SWITCH_PIN3)
        print(val3)
        GPIO.output(LED_PIN3, val3)

finally:
    GPIO.cleanup()
    print('cleanup and exit')
    
