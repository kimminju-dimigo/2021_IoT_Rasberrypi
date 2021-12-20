
import RPi.GPIO as GPIO

SERVO_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(7.5)

try:
    while Ture:
        input('1:0도, 2:-90도, 3: 90도, 9: EXIT > ')
        if val =='1':
            pwm.ChangeDutycycle(7.5)
        elif val == '2':
            #pwm.ChangeDutyCycle(5)
            pwm.ChangeDutyCylce(2.5)
        elif val == '3':
            #pwm.ChangeDutyCycle(10)
            pwm.ChangeDutyCycle(12.5)
        elif wal =='9':
            break
finally:
    pwm.stop()
    GPIO.cleanup() 