import time
import RPi.GPIO as GPIO

# LEFT MOTOR
motor1A = 13 #GPIO 27
motor1B = 15 #GPIO 22

# RIGHT MOTOR
motor2A = 16 #GPIO 23
motor2B = 18 #GPIO 24

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(motor2A, GPIO.OUT)
GPIO.setup(motor2B, GPIO.OUT)

GPIO.output(motor1A, GPIO.HIGH)
GPIO.output(motor1B, GPIO.LOW)
# GPIO.output(motor2A, GPIO.HIGH)
# GPIO.output(motor2B, GPIO.LOW)
time.sleep(1)

print('end')
GPIO.output(motor1A, GPIO.LOW)
GPIO.output(motor1B, GPIO.LOW)
GPIO.output(motor2A, GPIO.LOW)
GPIO.output(motor2B, GPIO.LOW)
GPIO.cleanup()