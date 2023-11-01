from imports import *

class Motor_Control:
    def __init__(self):
        # LEFT MOTOR
        self.motor1A = 13  # GPIO 27
        self.motor1B = 15  # GPIO 22

        # RIGHT MOTOR
        self.motor2B = 16  # GPIO 23
        self.motor2A = 18  # GPIO 24

        # PWM Settings
        self.PWM_freq = 1000  # PWM feq
        self.left_motor_pwm = GPIO.PWM(self.motor1A, self.PWM_freq)
        self.right_motor_pwm = GPIO.PWM(self.motor2A, self.PWM_freq)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.motor1B, GPIO.OUT)
        GPIO.setup(self.motor2B, GPIO.OUT)

        self.left_motor_pwm.start(0)
        self.right_motor_pwm.start(0)

    def go_forward(self, speed=50):
        self.left_motor_pwm.ChangeDutyCycle(speed)
        self.right_motor_pwm.ChangeDutyCycle(speed)
        GPIO.output(self.motor1B, GPIO.LOW)
        GPIO.output(self.motor2B, GPIO.LOW)

    def go_backward(self, speed=50):
        self.left_motor_pwm.ChangeDutyCycle(speed)
        self.right_motor_pwm.ChangeDutyCycle(speed)
        GPIO.output(self.motor1B, GPIO.HIGH)
        GPIO.output(self.motor2B, GPIO.HIGH)

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

    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    Motor_Control = Motor_Control()
    print('Go')
    Motor_Control.go_forward(50)
    time.sleep(2)
    print('Back')
    Motor_Control.go_backward(50)
    time.sleep(2)
    print('turning LEFT ...')
    Motor_Control.turn_left(20)
    time.sleep(2)
    print('turning RIGHT ...')
    Motor_Control.turn_right(20)
    time.sleep(2)
    Motor_Control.stop()
    print('stopped')