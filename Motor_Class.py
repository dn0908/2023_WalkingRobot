from imports import *

class Motor_Control:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        # LEFT MOTOR
        self.motor1A = 13  # GPIO 27
        self.motor1B = 15  # GPIO 22
        # RIGHT MOTOR
        self.motor2B = 16  # GPIO 23
        self.motor2A = 18  # GPIO 24

        # Set the GPIO pins as outputs
        GPIO.setup(self.motor1A, GPIO.OUT)
        GPIO.setup(self.motor1B, GPIO.OUT)
        GPIO.setup(self.motor2A, GPIO.OUT)
        GPIO.setup(self.motor2B, GPIO.OUT)

    def go_forward(self, speed=100):
        # L +
        GPIO.output(self.motor1A, GPIO.LOW)
        GPIO.output(self.motor1B, GPIO.HIGH)
        # R +
        GPIO.output(self.motor2A, GPIO.HIGH)
        GPIO.output(self.motor2B, GPIO.LOW)

    def go_backward(self, speed=100):
        # L -
        GPIO.output(self.motor1A, GPIO.HIGH)
        GPIO.output(self.motor1B, GPIO.LOW)
        # R -
        GPIO.output(self.motor2A, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.HIGH)

    def turn_left(self, speed=100):
        # L +
        GPIO.output(self.motor1A, GPIO.LOW)
        GPIO.output(self.motor1B, GPIO.HIGH)
        # R 0
        GPIO.output(self.motor2A, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.LOW)

    def turn_right(self, speed=100):
        # L 0
        GPIO.output(self.motor1A, GPIO.LOW)
        GPIO.output(self.motor1B, GPIO.LOW)
        # R +
        GPIO.output(self.motor2A, GPIO.HIGH)
        GPIO.output(self.motor2B, GPIO.LOW)

    def stop(self):
        # L 0
        GPIO.output(self.motor1A, GPIO.LOW)
        GPIO.output(self.motor1B, GPIO.LOW)
        # R 0
        GPIO.output(self.motor2A, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.LOW)


    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    Motor_Control = Motor_Control()
    print('Go')
    Motor_Control.go_forward(80)
    time.sleep(5)
    Motor_Control.go_backward(100)
    time.sleep(5)
    # print('Back')
    # Motor_Control.go_backward(100)
    # time.sleep(5)
    # print('turning LEFT ...')
    # Motor_Control.turn_left(100)
    # time.sleep(5)
    #print('turning RIGHT ...')
    #Motor_Control.turn_right(100)
    #time.sleep(5)
    Motor_Control.stop()
    print('stopped')