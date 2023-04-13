import pygame

pygame.init()

#   CONSTANTS
WIDTH = 700
HEIGHT = 500
# tuple with two parameters
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# Window title
pygame.display.set_caption("Pong")


def main():
    run = True

    # main game loop
    while run:
        # getting all events IE mouse clicks, keyboard inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
    pygame.quit()

if __name__ == '__main__':
    main()