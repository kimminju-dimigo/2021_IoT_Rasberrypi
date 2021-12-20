from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 17

#Flask 객체 생성 // 이렇게 하면 이름이 바뀌어도 파일 이름으로 들어가게 되어 있음
#__name__ 파일 이름
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#0.0.0.0:5000

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!</p>
        <a href="/led/on">LED ON</a>
        <a href="/led/off">LED OFF</a>
    '''

@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("on")
        return '''
            <p>LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif op == "off":
        GPIO.output(LED_PIN,GPIO.LOW)
        print("off")
        return '''
            <p>LED OFF</p>
            <a href="/">Go Home</a>
        '''

#@app.route("/led/on")
def ON():
    return '''
        <p>LED ON</p>
        <a href="/">Go Home</a>
    '''

#@app.route("/led/off")
def OFF():
    return '''
        <p>LED OFF</p>
        <a href="/">Go Home</a>
    '''

if __name__=="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()