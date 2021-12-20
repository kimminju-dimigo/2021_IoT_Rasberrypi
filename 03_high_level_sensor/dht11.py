#dht11.py
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN = 21

try:
    while True :
        h, t = Adafruit_DHT.read_retry(sensor, PIN)
        if h is not None and t is not None:
            print(f'Temperture={t:.1f}, Humidity={h:.1f}%')
        else :
            print('Read Error')
        time.sleep(1)
finally:
    print('END')