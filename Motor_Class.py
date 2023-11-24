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

        # # PWM Settings
        # self.PWM_freq = 5000  # PWM feq
        # self.left_go_pwm = GPIO.PWM(self.motor1B, self.PWM_freq)
        # self.right_go_pwm = GPIO.PWM(self.motor2A, self.PWM_freq)

        # self.left_back_pwm = GPIO.PWM(self.motor1A, self.PWM_freq)
        # self.right_back_pwm = GPIO.PWM(self.motor2B, self.PWM_freq)
        

        # self.left_go_pwm.start(0)
        # self.right_go_pwm.start(0)
        # self.left_back_pwm.start(0)
        # self.right_back_pwm.start(0)

    def go_forward(self, speed=100):

        # self.left_go_pwm.ChangeDutyCycle(speed)
        # self.right_go_pwm.ChangeDutyCycle(speed)

        # L +
        GPIO.output(self.motor1A, GPIO.LOW)
        GPIO.output(self.motor1B, GPIO.HIGH)
        # R +
        GPIO.output(self.motor2A, GPIO.HIGH)
        GPIO.output(self.motor2B, GPIO.LOW)

    def go_backward(self, speed=100):
        # self.left_back_pwm.ChangeDutyCycle(speed)
        # self.right_back_pwm.ChangeDutyCycle(speed)
        # L -
        GPIO.output(self.motor1A, GPIO.HIGH)
        GPIO.output(self.motor1B, GPIO.LOW)
        # R -
        GPIO.output(self.motor2A, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.HIGH)

    def turn_left(self, speed=100):
        # self.left_go_pwm.ChangeDutyCycle(speed)
        # self.right_back_pwm.ChangeDutyCycle(speed)
        # L +
        GPIO.output(self.motor1A, GPIO.LOW)
        GPIO.output(self.motor1B, GPIO.HIGH)
        # R -
        GPIO.output(self.motor2A, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.HIGH)

    def turn_right(self, speed=100):
        # self.left_back_pwm.ChangeDutyCycle(speed)
        # self.right_go_pwm.ChangeDutyCycle(speed)
        # L -
        GPIO.output(self.motor1A, GPIO.HIGH)
        GPIO.output(self.motor1B, GPIO.LOW)
        # R +
        GPIO.output(self.motor2A, GPIO.HIGH)
        GPIO.output(self.motor2B, GPIO.LOW)

    def stop(self):
        # self.left_go_pwm.ChangeDutyCycle(0)
        # self.right_go_pwm.ChangeDutyCycle(0)
        # self.left_back_pwm.ChangeDutyCycle(0)
        # self.right_back_pwm.ChangeDutyCycle(0)
        # L 0
        GPIO.output(self.motor1A, GPIO.LOW)
        GPIO.output(self.motor1B, GPIO.LOW)
        # R 0
        GPIO.output(self.motor2A, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.LOW)


    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    '''
    PWM speed min : 80
    PWM speed MAX : 100
    '''


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