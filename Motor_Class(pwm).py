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

        # Initialize PWM for the motors
        self.pwm_motor1 = GPIO.PWM(self.motor1A, 1000)  # 1000 Hz frequency
        self.pwm_motor2 = GPIO.PWM(self.motor2A, 1000)  # 1000 Hz frequency

        # Start PWM with 0% duty cycle
        self.pwm_motor1.start(0)
        self.pwm_motor2.start(0)

    def set_motor_speed(self, pwm_motor, speed):
        # Convert speed to a duty cycle value between 0 and 100
        duty_cycle = max(0, min(100, speed))
        pwm_motor.ChangeDutyCycle(duty_cycle)

    def go_forward(self, speed=100):
        # L +
        self.set_motor_speed(self.pwm_motor1, speed)
        GPIO.output(self.motor1B, GPIO.HIGH)
        # R +
        self.set_motor_speed(self.pwm_motor2, speed)
        GPIO.output(self.motor2B, GPIO.LOW)

    def go_backward(self, speed=100):
        # L -
        GPIO.output(self.motor1B, GPIO.LOW)
        self.set_motor_speed(self.pwm_motor1, speed)
        # R -
        GPIO.output(self.motor2B, GPIO.HIGH)
        self.set_motor_speed(self.pwm_motor2, speed)

    def turn_left(self, speed=100):
        # L +
        self.set_motor_speed(self.pwm_motor1, speed)
        GPIO.output(self.motor1B, GPIO.HIGH)
        # R -
        GPIO.output(self.motor2B, GPIO.HIGH)
        self.set_motor_speed(self.pwm_motor2, speed)

    def turn_right(self, speed=100):
        # L -
        GPIO.output(self.motor1B, GPIO.LOW)
        self.set_motor_speed(self.pwm_motor1, speed)
        # R +
        self.set_motor_speed(self.pwm_motor2, speed)
        GPIO.output(self.motor2B, GPIO.LOW)

    def stop(self):
        # Stop both motors
        self.set_motor_speed(self.pwm_motor1, 0)
        self.set_motor_speed(self.pwm_motor2, 0)

    def cleanup(self):
        # Stop PWM and clean up GPIO
        self.pwm_motor1.stop()
        self.pwm_motor2.stop()
        GPIO.cleanup()

    def forward(fullspeed):  
        GPIO.output(motor1A, True)
        GPIO.output(motor1B, False)
        pwm1.ChangeDutyCycle(fullspeed) #left
        GPIO.output(motor2A, True)
        GPIO.output(motor2B, False)
        pwm2.ChangeDutyCycle(fullspeed) #right

    def backward():
        GPIO.output(motor1A, False)
        GPIO.output(motor1B, True)
        pwm1.ChangeDutyCycle(50)
        GPIO.output(motor2A, False)
        GPIO.output(motor2B, True)
        pwm2.ChangeDutyCycle(50)
    
    def right(fullspeed, ctrl):
        GPIO.output(motor1A, True)
        GPIO.output(motor1B, False)
        pwm1.ChangeDutyCycle(fullspeed)
        GPIO.output(motor2A, False)
        GPIO.output(motor2B, True)
        # pwm2.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(fullspeed-ctrl)
            
    def left(fullspeed, ctrl):
        GPIO.output(motor1A, False)
        GPIO.output(motor1B, True)
        # pwm1.ChangeDutyCycle(0)

        pwm1.ChangeDutyCycle(fullspeed-ctrl)
        GPIO.output(motor2A, True)
        GPIO.output(motor2B, False)
        pwm2.ChangeDutyCycle(fullspeed)
        
    def stop():
        GPIO.output(motor1A, False)
        GPIO.output(motor1B, False)
        GPIO.output(motor2A, False)
        GPIO.output(motor2B, False)


if __name__ == "__main__":
    Motor_Control = Motor_Control()
    print('Go')
    Motor_Control.go_forward(80)
    time.sleep(5)
    print('back')
    Motor_Control.go_backward(100)
    time.sleep(5)
    Motor_Control.stop()
    print('stopped')
    Motor_Control.cleanup()
