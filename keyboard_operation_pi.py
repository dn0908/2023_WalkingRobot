import pygame
from Motor_Class import Motor_Control

def main():
    motor_controller = Motor_Control()

    # Init pygame
    pygame.init()
    screen = pygame.display.set_mode((100, 100))

    # Init key state variables
    up_key_pressed = False
    down_key_pressed = False
    left_key_pressed = False
    right_key_pressed = False

    space_pressed = False

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not up_key_pressed:
                    motor_controller.go_forward(50)
                    up_key_pressed = True
                elif event.key == pygame.K_DOWN and not down_key_pressed:
                    motor_controller.go_backward(50)
                    down_key_pressed = True
                elif event.key == pygame.K_LEFT and not left_key_pressed:
                    motor_controller.turn_left(50)
                    left_key_pressed = True
                elif event.key == pygame.K_RIGHT and not right_key_pressed:
                    motor_controller.turn_right(50)
                    right_key_pressed = True
                elif event.key == pygame.K_SPACE:  # Spacebar : stop motor
                    motor_controller.stop()
                    space_pressed = True
                elif event.key == pygame.K_q:  # Quit program when 'Q' key pressed
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up_key_pressed = False
                elif event.key == pygame.K_DOWN:
                    down_key_pressed = False
                elif event.key == pygame.K_LEFT:
                    left_key_pressed = False
                elif event.key == pygame.K_RIGHT:
                    right_key_pressed = False
                elif event.key == pygame.K_SPACE:
                    space_pressed = False

        if not space_pressed:
            motor_controller.resume()

    # Cleanup and exit
    motor_controller.stop()
    motor_controller.cleanup()
    pygame.quit()

if __name__ == "__main__":
    main()