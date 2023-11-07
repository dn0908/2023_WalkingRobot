import RPi.GPIO as GPIO
import time

class HC_SR04:
    def __init__(self):
        # GPIO_TRIGGER = 11  # GPIO 17
        # GPIO_ECHO = 22  # GPIO 25
        GPIO.setmode(GPIO.BOARD)
        self.GPIO_TRIGGER = 11
        self.GPIO_ECHO = 22

        #GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def hc_get_distance(self):
        GPIO.output(self.GPIO_TRIGGER, False)

        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        pulse_start = time.time()
        pulse_end = time.time()

        while GPIO.input(self.GPIO_ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(self.GPIO_ECHO) == 1:
            pulse_end = time.time()

        # Calculate pulse duration
        pulse_duration = pulse_end - pulse_start

        # Calculate dist 34300 cm/s
        distance = (pulse_duration * 34300) / 2

        return distance

    def cleanup(self):
        GPIO.cleanup()


if __name__ == '__main__':
    try:
        sensor = HC_SR04()
        while True:
            distance = sensor.hc_get_distance()
            print("distance: {:.2f} cm".format(distance))
            time.sleep(0.05)

    except KeyboardInterrupt:
        sensor.cleanup()
