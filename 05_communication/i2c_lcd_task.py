from lcd import drivers
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN = 26

display = drivers.Lcd()

try:
    print("start")
    while True:
        now = datetime.datetime.now()
        #print(now.strftime("%x%X"))
        display.lcd_display_string(now.strftime("%x%X"), 1)

        h, t = Adafruit_DHT.read_retry(sensor, PIN)
        if h is not None and t is not None:
            #print(f'Temperture={t:.1f}C, Humidity={h:.1f}%')
            display.lcd_display_string(f"{t:.1f}*C, {h:.1f}%",2)
            #time.sleep(1)
        else :
            print('Read Error')
            display.lcd_display_string("ERROR", 2)
            #time.sleep(1)

finally :
    print("Cleaning up!") 
    display.lcd_clear()