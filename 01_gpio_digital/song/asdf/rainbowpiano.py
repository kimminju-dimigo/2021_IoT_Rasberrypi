import RPi.GPIO as GPIO
import time
import random

#LED색의 핀번호 지정하기 
R = 16
Y = 20
G = 21

#스위치의 핀번호 지정하기 
S1 = 26
S2 = 19
S3 = 13
S4 = 6
S5 = 5
S6 =11
S7 = 9
S8 = 10

off = 22

#피에조 부저 핀번호 지정하기 
PIEZO = 18

#GPIO의 모드를 BCM으로 바꿔준다. 
GPIO.setmode(GPIO.BCM)

#LED를 아웃으로 바꿔준다. 
GPIO.setup(R, GPIO.OUT)
GPIO.setup(Y, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)

#피에조 부저를 아웃으로 바꿔준다 
GPIO.setup(PIEZO, GPIO.OUT) 

 #내부풀다운/모드 스위치들을 인으로 바꿔준다 
GPIO.setup(S1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(S2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(S3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(S4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(S5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(S6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(S7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(S8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(off, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm = GPIO.PWM(PIEZO,1)

# 도 레 미 파 솔 라 시 도 
melody = [262, 294, 330, 349, 392, 440, 494, 523]

try:
    while True:
        #랜덤함수를 이용항 LED가 랜덤으로 켜지게 한다. 
        #0부터 1까지 무작위 정수를 뽑는다 
        a= random.randrange(0, 2)
        b = random.randrange(0, 2)
        c = random.randrange(0, 2)
        GPIO.output(R, a) #led 빨간색을 키던가 끈다 
        time.sleep(0.1)
        GPIO.output(Y, b) #led 노란색을 키던가 끈다 
        time.sleep(0.1)
        GPIO.output(G, c) #led 초록색을 키던가 끈다 
        time.sleep(0.1)
    
        #스위치 1번이 눌리면 멜로디 리스트 안에 있는 0번째 값을 바탕으로 피에조의 주파수를 바꾼다. 낮은 도  
        if GPIO.input(S1) == GPIO.HIGH:
            pwm.ChangeFrequency(melody[0])
            pwm.start(50)
            time.sleep(0.3)
            pwm.start(1)

        #스위치 2번이 눌리면 멜로디 리스트 안에 있는 1번째 값을 바탕으로 피에조의 주파수를 바꾼다. 레   
        if GPIO.input(S2) == GPIO.HIGH:
            pwm.ChangeFrequency(melody[1])
            pwm.start(50)
            time.sleep(0.3)
            pwm.start(1)
            
        #스위치 3번이 눌리면 멜로디 리스트 안에 있는 2번째 값을 바탕으로 피에조의 주파수를 바꾼다. 미
        if GPIO.input(S3) == GPIO.HIGH:
            pwm.ChangeFrequency(melody[2])
            pwm.start(50)
            time.sleep(0.3)
            pwm.start(1)

        #스위치 4번이 눌리면 멜로디 리스트 안에 있는 3번째 값을 바탕으로 피에조의 주파수를 바꾼다. 파
        if GPIO.input(S4) == GPIO.HIGH:
            pwm.ChangeFrequency(melody[3])
            pwm.start(50)
            time.sleep(0.3)
            pwm.start(1)

        #스위치 5번이 눌리면 멜로디 리스트 안에 있는 4번째 값을 바탕으로 피에조의 주파수를 바꾼다. 솔
        if GPIO.input(S5) == GPIO.HIGH:
            pwm.ChangeFrequency(melody[4])
            pwm.start(50)
            time.sleep(0.3)
            pwm.start(1)

        #스위치 6번이 눌리면 멜로디 리스트 안에 있는 5번째 값을 바탕으로 피에조의 주파수를 바꾼다. 라
        if GPIO.input(S6) == GPIO.HIGH:
            pwm.ChangeFrequency(melody[5])
            pwm.start(50) 
            time.sleep(0.3)
            pwm.start(1)

        #스위치 7번이 눌리면 멜로디 리스트 안에 있는 6번째 값을 바탕으로 피에조의 주파수를 바꾼다. 시
        if GPIO.input(S7) == GPIO.HIGH:
            pwm.ChangeFrequency(melody[6])
            pwm.start(50)
            time.sleep(0.3)
            pwm.start(1)
        
        #스위치 8번이 눌리면 멜로디 리스트 안에 있는 7번째 값을 바탕으로 피에조의 주파수를 바꾼다. 높은 도
        if GPIO.input(S8) == GPIO.HIGH:
            pwm.ChangeFrequency(melody[7])
            pwm.start(50)
            time.sleep(0.3)
            pwm.start(1)
        #스위치가 눌리면 전원이 꺼진다. 
        if GPIO.input(off) == GPIO.HIGH:
            print("종료")
            GPIO.cleanup()    

finally :
    print("끝")
    GPIO.cleanup()