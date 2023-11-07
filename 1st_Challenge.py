from imports import *
from Motor_Class import Motor_Control
from HC_Class import HC_SR04

class RobotControl:
    def __init__(self):
        self.motor = Motor_Control()
        self.sensor = HC_SR04()
        self.current_speed = 100  # Default speed

    def move_forward(self):
        self.motor.go_forward(self.current_speed)

    def move_backward(self):
        self.motor.go_backward(self.current_speed)

    def turn_left(self):
        self.motor.turn_left(self.current_speed)

    def turn_right(self):
        self.motor.turn_right(self.current_speed)

    def stop(self):
        self.motor.stop()

    def avoid_obstacles(self):
        while True:
            distance = self.sensor.hc_get_distance()
            if distance <= 15:  # Obstacle detected within 15cm
                self.stop()
                time.sleep(1)  # Stop for 1 second
            else:
                if keyboard.is_pressed('w'):
                    self.move_forward()
                elif keyboard.is_pressed('s'):
                    self.move_backward()
                elif keyboard.is_pressed('a'):
                    self.turn_left()
                elif keyboard.is_pressed('d'):
                    self.turn_right()
                else:
                    self.stop()

    def cleanup(self):
        self.motor.cleanup()
        self.sensor.cleanup()

if __name__ == "__main__":
    robot = RobotControl()
    try:
        robot.avoid_obstacles()
    except KeyboardInterrupt:
        robot.cleanup()
