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

        # PWM Settings
        self.PWM_freq = 1000  # PWM feq
        self.left_motor_pwm = GPIO.PWM(self.motor1A, self.PWM_freq)
        self.right_motor_pwm = GPIO.PWM(self.motor2A, self.PWM_freq)
        

        self.left_motor_pwm.start(0)
        self.right_motor_pwm.start(0)

    def go_forward(self, speed=50):
        self.left_motor_pwm.ChangeDutyCycle(speed)
        self.right_motor_pwm.ChangeDutyCycle(speed)
        GPIO.output(self.motor1B, GPIO.HIGH)
        GPIO.output(self.motor2B, GPIO.HIGH)

    def go_backward(self, speed=50):
        self.left_motor_pwm.ChangeDutyCycle(speed)
        self.right_motor_pwm.ChangeDutyCycle(speed)
        GPIO.output(self.motor1B, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.LOW)

    def turn_left(self, speed=50):
        self.left_motor_pwm.ChangeDutyCycle(speed)
        self.right_motor_pwm.ChangeDutyCycle(speed)
        GPIO.output(self.motor1B, GPIO.HIGH)
        GPIO.output(self.motor2B, GPIO.LOW)

    def turn_right(self, speed=50):
        self.left_motor_pwm.ChangeDutyCycle(speed)
        self.right_motor_pwm.ChangeDutyCycle(speed)
        GPIO.output(self.motor1B, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.HIGH)

    def stop(self):
        self.left_motor_pwm.ChangeDutyCycle(0)
        self.right_motor_pwm.ChangeDutyCycle(0)

    # def resume(self, speed=50):
    #     self.left_motor_pwm.ChangeDutyCycle(speed)
    #     self.right_motor_pwm.ChangeDutyCycle(speed)
    #     GPIO.output(self.motor1B, GPIO.HIGH)
    #     GPIO.output(self.motor2B, GPIO.HIGH)

    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    Motor_Control = Motor_Control()
    print('Go')
    Motor_Control.go_forward(100)
    time.sleep(2)
    print('Back')
    Motor_Control.go_backward(100)
    time.sleep(2)
    print('turning LEFT ...')
    Motor_Control.turn_left(100)
    time.sleep(2)
    print('turning RIGHT ...')
    Motor_Control.turn_right(100)
    time.sleep(2)
    Motor_Control.stop()
    print('stopped')