import RPi.GPIO as GPIO
from lcd import drivers
import time

#led에 붙은 알파벳은 색깔을 구분하기 위함입니다. 그래서 실제 색상과 다를 수 있습니다. 
yled_PIN = 27 #led 핀번호 선언
rled_PIN = 17 #현관등
SWITCH_PIN = 4 #스위치 핀번호 선언-0vv
piezo_PIN = 22 #피에조 부저 핀번호 선언
servo_PIN = 21 #모터 핀번호 선언
pir_PIN = 12 #pir센서 핀번호 선언

display = drivers.Lcd()

GPIO.setmode (GPIO.BCM) #bcm 모드로 변경함 
GPIO.setup(yled_PIN, GPIO.OUT) #led 출력모드
GPIO.setup(rled_PIN, GPIO.OUT) #led 출력모드
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)#내부 풀업저항
GPIO.setup(piezo_PIN, GPIO.OUT) #피에조부저 출력모드
GPIO.setup(pir_PIN, GPIO.IN) #pir센서 입력모드
GPIO.setup(servo_PIN, GPIO.OUT) #서브모터 출력모드

melody = [262, 294, 330, 349, 392, 440, 494, 523] # 도0, 레1, 미2, 파3, 솔4, 라5, 시6, 도7 음계
song = [0,0,0,0,2,4,2,0,4,2,4,2,0,0,0,0,4,4,2,0,4,4,4,4,4,4,2,0,4,4,4,4,4,4,2,0,4,4,5,4,7,4,7,4,2,1,0,0] #곰 세 마리 노래

moter = GPIO.PWM(servo_PIN, 50) 
time.sleep(1)
print('센서 준비 완료')

try:
    while True:
        moter.start(7.5) 
        buzzer = GPIO.PWM(piezo_PIN, 262)
        pir = GPIO.input(pir_PIN)
        button = GPIO.input(SWITCH_PIN)
        buzzer.stop()

        if button == 0 : #버튼이 눌리면 모든 작업이 꺼진다.
            print(button) #버튼값을출력한다
            break  

        elif pir == GPIO.HIGH: #pir센서가 움직임을 감지하면
            print('사람이 들어왔습니다') 
            GPIO.output(yled_PIN, GPIO.HIGH) #현광등켜기
            GPIO.output(rled_PIN, GPIO.HIGH) #거실등켜기
            display.lcd_display_string("* Welcome home *", 1) #lcd 모듈에 문구 출력         
            display.lcd_display_string("* Have NiceDay *", 2) #lcd 모듈에 문구 출력         
            time.sleep(3)
            print("현관등이 꺼집니다.")
            GPIO.output(yled_PIN, GPIO.LOW) #현관등끄기
            if button == 0 : #버튼이 눌리면 모든 작업이 꺼진다.  
                print(button) #버튼값을출력한다
                break  

            print("손 흔들흔들")
            for j in range(0, 3) : # 인형의 팔을 움직인다.
                time.sleep(1)
                moter.ChangeDutyCycle(12.5)
                time.sleep(1)
                moter.ChangeDutyCycle(7.5)
                if button == 0 : #버튼이 눌리면 모든 작업이 꺼진다.  
                    print(button)#버튼값을출력한다
                    break  

            buzzer = GPIO.PWM(piezo_PIN, 262)
            buzzer.start(50)
            print("노래 큐~")
            for i in song:
                buzzer.ChangeFrequency(melody[i]) #노래 출력
                time.sleep(0.5)
                if button == 0 : #버튼이 눌리면 모든 작업이 꺼진다.  
                    print(button)#버튼값을출력한다
                    break  
            print("노래 끝남~") 
            buzzer.stop()

        else :
            if button == 0 : #버튼이 눌리면 모든 작업이 꺼진다.  
                print(button)#버튼값을출력한다
                break
            print("사람없음 ㅇㅇ")
            GPIO.output(yled_PIN, GPIO.LOW) #모든 led가 꺼져있다
            GPIO.output(rled_PIN, GPIO.LOW)
            if button == 0 : #버튼이 눌리면 모든 작업이 꺼진다.  
                print(button)#버튼값을출력한다
                break  

                
        time.sleep(0.1)

        if button == 0 : #버튼이 눌리면 모든 작업이 꺼진다.  
            print(button)#버튼값을출력한다
            break  
        time.sleep(1)
        
finally:
    GPIO.cleanup()
    print('Exit and cleanup') #작업 종료