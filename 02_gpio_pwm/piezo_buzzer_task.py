import RPi.GPIO as GPIO
import time

BUZZER_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)


#melody = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330 ,330, 294, 392,392,440,440,392,392,330,392,330,294,330,262]

melody = [262, 294, 330, 349, 392, 440, 494, 523]
song = [4,4,5,5,4,4,2,2,4,4,2,2,1,4,4,5,5,4,4,2,4,2,1,2,0,0]
pwm.start(50)

try:
    for i in song: 
        time.sleep(0.5)
        pwm.ChangeFrequency(melody[i])
       
            
finally: 
    pwm.stop()
    GPIO.cleanup()

