import RPi.GPIO as GPIO
import time

LED_PIN = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#PWm 인스턴스생성
#주파수 설정 (50hz)
pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0) #duty cycle (0~100)

try:
    while True:
        for i in range(3):  #range(0, 3 ,1)
            #서서히 켜지게하기cs 
            for j in range(0, 101, 5): #start, end, stepdl
                pwm.ChangeDutyCycle(j)
                time.sleep(0.1)
            #서서히 꺼지게하기
            for j in range(100, -1, -5):
                pwm.ChangeDutyCycle(j)
                time.sleep(0.1)
finally:
    pwm.stop() #pmw 종료 
    GPIO.cleanup()
    print('cleanup and exit')
