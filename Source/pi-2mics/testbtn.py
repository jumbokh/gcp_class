import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
BTN_PIN = 11
GPIO.setup(BTN_PIN, GPIO.IN)
def mycallback(channel):    
        print("Button pressed")
        try:
           GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, \
                   callback=mycallback, bouncetime=200)
           while True:
              time.sleep(10)
        finally:                                 
              GPIO.cleanup()
