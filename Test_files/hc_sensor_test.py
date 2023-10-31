import RPi.GPIO as GPIO
import time
def measure():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    timeOut = start
    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()
        if time.time()-timeOut > 0.012:
            return -1
    while GPIO.input(GPIO_ECHO)==1:
        if time.time()-start > 0.012:
            return -1
        stop = time.time()
        elapsed = stop-start
        distance = (elapsed * 34300)/2
        return distance
GPIO.setmode(GPIO.BOARD)
GPIO_TRIGGER = 11 #GPIO 17
GPIO_ECHO = 22 #GPIO 25
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.output(GPIO_TRIGGER, False)
time.sleep(.1)
for i in range(10):
    print(measure())
    time.sleep(0.5)