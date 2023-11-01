import pygame
from Motor_Class import Motor_Control

def main():
    pygame.init()

    # Motor Control Initialization
    motor_controller = Motor_Control()

    # Initialize pygame
    screen = pygame.display.set_mode((100, 100))
    pygame.display.set_caption("Robot Control")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    motor_controller.go_forward(50)
                elif event.key == pygame.K_DOWN:
                    motor_controller.go_backward(50)
                elif event.key == pygame.K_LEFT:
                    motor_controller.turn_left(50)
                elif event.key == pygame.K_RIGHT:
                    motor_controller.turn_right(50)
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                    motor_controller.stop()

    # Cleanup and exit
    motor_controller.cleanup()
    pygame.quit()

if __name__ == "__main__":
    main()