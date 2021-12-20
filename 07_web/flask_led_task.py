from flask import Flask
import RPi.GPIO as GPIO

LED_PIN_YELLOW = 17
LED_PIN_BLUE = 5
#Flask 객체 생성 // 이렇게 하면 이름이 바뀌어도 파일 이름으로 들어가게 되어 있음
#__name__ 파일 이름
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_YELLOW, GPIO.OUT)
GPIO.setup(LED_PIN_BLUE, GPIO.OUT)

#0.0.0.0:5000

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!</p>
        <a href="/led/yellow/on">YelloW LED ON</a><br>
        <a href="/led/yellow/off">Yellow LED OFF</a><br>
        <a href="/led/blue/on">BLUE LED ON</a><br>
        <a href="/led/blue/off">BLUE LED OFF</a>
    '''

@app.route("/led/<color>/<op>")
def led_op(color, op):
    if op == "on":
        if color == "yellow":
            GPIO.output(LED_PIN_YELLOW, GPIO.HIGH)
            print("Yellow on")
            return '''
                <p>Yellow ON</p>
                <a href="/">Go Home</a>
            '''
        elif color == "blue":
            GPIO.output(LED_PIN_BLUE, GPIO.HIGH)
            print("BLUE on")
            return '''
                <p>BLUE ON</p>
                <a href="/">Go Home</a>
            '''
            
    elif op == "off":
        if color == "yellow":
            GPIO.output(LED_PIN_YELLOW, GPIO.LOW)
            print("Yellow off")
            return '''
                <p>Yellow OFF</p>
                <a href="/">Go Home</a>
            '''
        elif color == "blue":
            GPIO.output(LED_PIN_BLUE, GPIO.LOW)
            print("BLUE OFF")
            return '''
                <p>BLUE OFF</p>
                <a href="/">Go Home</a>
            '''
       

if __name__=="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()