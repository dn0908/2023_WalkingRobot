from imports import *

class Motor_Control:
    def __init__(self):
        # LEFT MOTOR
        self.motor1A = 13  # GPIO 27
        self.motor1B = 15  # GPIO 22

        # RIGHT MOTOR
        self.motor2A = 16  # GPIO 23
        self.motor2B = 18  # GPIO 24

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.motor1A, GPIO.OUT)
        GPIO.setup(self.motor1B, GPIO.OUT)
        GPIO.setup(self.motor2A, GPIO.OUT)
        GPIO.setup(self.motor2B, GPIO.OUT)

    def go_forward(self):
        GPIO.output(self.motor1A, GPIO.HIGH)
        GPIO.output(self.motor1B, GPIO.LOW)
        GPIO.output(self.motor2A, GPIO.HIGH)
        GPIO.output(self.motor2B, GPIO.LOW)

    def go_backward(self):
        GPIO.output(self.motor1A, GPIO.LOW)
        GPIO.output(self.motor1B, GPIO.HIGH)
        GPIO.output(self.motor2A, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.HIGH)

    def turn_left(self):
        GPIO.output(self.motor1A, GPIO.LOW)
        GPIO.output(self.motor1B, GPIO.HIGH)
        GPIO.output(self.motor2A, GPIO.HIGH)
        GPIO.output(self.motor2B, GPIO.LOW)

    def turn_right(self):
        GPIO.output(self.motor1A, GPIO.HIGH)
        GPIO.output(self.motor1B, GPIO.LOW)
        GPIO.output(self.motor2A, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.motor1A, GPIO.LOW)
        GPIO.output(self.motor1B, GPIO.LOW)
        GPIO.output(self.motor2A, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    Motor_Control = Motor_Control()
    print('Go')
    Motor_Control.go_forward()
    time.sleep(2)
    print('Back')
    Motor_Control.go_backward()
    time.sleep(2)
    print('turning LEFT')
    Motor_Control.turn_left()
    time.sleep(2)
    print('turning RIGHT')
    Motor_Control.turn_right()
    time.sleep(2)
    Motor_Control.stop()
    print('stopped')