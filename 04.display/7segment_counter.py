import RPi.GPIO as GPIO
import time

#GPIO 7개 핀 Pin 번호 설정

SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8]

GPIO.setmaode(GPIO.BCM)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.out)
    GPIO.output(segment, GPIO.LOW)




data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9


try :
    for i in range(10): #0~9
        #0출력
        for j in range(7): #0~6까지
            GPIO.output(SEGMENT_PINS[j], data[i][j])
        time.sleep(1)

        #지우기
        for i in range(7):
            GPIO.output(SEGMENT_PINS[i], GPIO.LOW)

finally:
    GPIO.cleanup()
    print('bye')