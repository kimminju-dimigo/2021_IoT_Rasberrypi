import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

#μ£Όνμ : λ(262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) #duty cycle (0~100)

try:
    time.sleep(2)
    pwm.ChangeDutyCycle(0)

finally:
    pwm.stop()
    GPIO.cleanup()
    print(cleanup and exit)