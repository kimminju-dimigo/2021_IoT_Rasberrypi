import RPi.GPIO as GPIO
import time

sound_pin = 2
r = 3
y = 4
g = 5
piezo = 10

flag = True

pwm = GPIO.PWM(piezo,1)
melody = [262]

GPIO.setmode(GPIO.BCM)
GPIO.setup(sound_pin, GPIO.IN)
GPIO.setup(r, GPIO.OUT)
GPIO.setup(y, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(piezo, GPIO.OUT)

try:
    while True:

        if GPIO.input(sound_pin) < 100:
            GPIO.output(g, True)
            print("조용하네")
            time.sleep(0.5)

        elif GPIO.input(sound_pin) > 100:
            GPIO.output(g, False)
            GPIO.output(y, True)
            print("살짝 시끄럽네")
            time.sleep(0.5)

        elif GPIO.inpu(sound_pin) >300:
            GPIO.output(y, False)
            GPIO.output(r, True)
            pwm.ChangeFrequency(melody[0])
            pwm.start(50)
            print("시끄러워!")
            time.sleep(0.5)

finally: 
    GPIO.cleanup()
    print("Exit")
