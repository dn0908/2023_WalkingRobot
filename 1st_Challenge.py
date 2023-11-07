from imports import *
from Motor_Class import Motor_Control
from HC_Class import HC_SR04

class RobotControl:
    def __init__(self):
        self.motor = Motor_Control()
        self.sensor = HC_SR04()

    def move_forward(self, speed=100):
        self.motor.go_forward(speed)

    def move_backward(self, speed=100):
        self.motor.go_backward(speed)

    def turn_left(self, speed=100):
        self.motor.turn_left(speed)

    def turn_right(self, speed=100):
        self.motor.turn_right(speed)

    def stop(self):
        self.motor.stop()

    def avoid_obstacles(self):
        while True:
            distance = self.sensor.hc_get_distance()
            if distance <= 15:  # Obstacle detected within 15cm
                self.stop()
                time.sleep(1)  # Stop for 1 second
            else:
                # Continue with user input for robot movement
                command = input("Enter a command (w/a/s/d/q to quit): ").lower()
                if command == 'w':
                    self.move_forward()
                elif command == 's':
                    self.move_backward()
                elif command == 'a':
                    self.turn_left()
                elif command == 'd':
                    self.turn_right()
                elif command == 'q':
                    break
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
