from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_Y = 21
LED_B = 17

#Flask 객체 생성 // 이렇게 하면 이름이 바뀌어도 파일 이름으로 들어가게 되어 있음
#__name__ 파일 이름
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_Y, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

#0.0.0.0:5000

@app.route("/")
def hello():
    return render_template("led2_task.html")

@app.route("/led/<op>")
def led_op(op) :
    if op == "yellow_on" :
        GPIO.output(LED_Y, GPIO.HIGH)
        print("Yellow on")
        return "LED_Yellow ON"

    elif op=="blue_on" :
        GPIO.output(LED_B, GPIO.HIGH)
        print("Blue on")
        return "LED_Blue ON"

    elif op == "yellow_off":
        GPIO.output(LED_Y, GPIO.LOW)
        print("Yellow off")
        return "LED_Yellow OFF"
        
    elif op=="blue_off" :
        GPIO.output(LED_B,GPIO.LOW)
        print("Blue off")
        return "LED_Blue OFF"
        
    else :
        return "Error"

if __name__=="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()