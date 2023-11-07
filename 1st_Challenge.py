import RPi.GPIO as GPIO
import time
import pygame
from imports import *
from Motor_Class import Motor_Control
from HC_Class import HC_SR04

# Initialize Pygame
pygame.init()

# Set up the Pygame window
window = pygame.display.set_mode((200, 200))

# Initialize GPIO and HC_SR04
GPIO.setmode(GPIO.BOARD)
GPIO_TRIGGER = 11
GPIO_ECHO = 22
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Set the Pygame clock
clock = pygame.time.Clock()

class RobotControl:
    def __init__(self):
        self.motor = Motor_Control()
        self.sensor = HC_SR04()
        #self.current_speed = 100  # Default speed
        self.direction = None

    def move_forward(self):
        if not self.is_obstacle_detected():
            self.motor.go_forward(100)
            self.direction = 'forward'
        else:
            self.stop()

    def move_backward(self):
        if not self.is_obstacle_detected():
            self.motor.go_backward(100)
            self.direction = 'backward'
        else:
            self.stop()

    def turn_left(self):
        self.motor.turn_left(100)
        self.direction = 'left'

    def turn_right(self):
        self.motor.turn_right(100)
        self.direction = 'right'

    def stop(self):
        self.motor.stop()
        self.direction = None

    def is_obstacle_detected(self):
        distance = self.sensor.hc_get_distance()
        return distance <= 15  # Obstacle detected within 15cm

def main():
    running = True
    robot = RobotControl()
    robot.stop()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("Robot Going FORWARD ... ")
                    robot.move_forward()
                elif event.key == pygame.K_DOWN:
                    robot.move_backward()
                elif event.key == pygame.K_LEFT:
                    print("Turning LEFT ... ")
                    robot.turn_left()
                elif event.key == pygame.K_RIGHT:
                    print("Turning RIGHT ...")
                    robot.turn_right()
                elif event.key == pygame.K_q:
                    print("Key Q pressed ! Robot STOP !")
                    robot.stop()

        if robot.is_obstacle_detected():
            print("OBSTACLE DETECTED... EMERGENCY STOP !!! ")
            robot.stop()
            time.sleep(5)
            print("OBSTACLE REMOVED... GO!")
            robot.move_forward()
            time.sleep(2)

        clock.tick(30)  # Limit the frame rate to 30 FPS

    robot.motor.cleanup()
    GPIO.cleanup()
    pygame.quit()

if __name__ == "__main__":
    main()
