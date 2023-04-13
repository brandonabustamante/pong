################################################################################
import pygame

pygame.init()

#   CONSTANTS
WIDTH = 700
HEIGHT = 500
FPS = 60
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# input is tuple with two parameters
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

# Window title
pygame.display.set_caption("Pong")

class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(
            win, self.COLOR, (self.x, self.y, self.width, self.height))
    
    def move(self, up=True):

        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

def draw(win, paddles):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()

def handle_paddle_movement(keys, left_paddle, right_paddle):
    # left paddle uses w and s keys
    if keys[pygame.K_w]:
        left_paddle.move(up=True)

    if keys[pygame.K_s]:
        left_paddle.move(up=False)

    # right paddle uses up and down keys
    if keys[pygame.K_UP]:
        right_paddle.move(up=True)

    if keys[pygame.K_DOWN]:
        right_paddle.move(up=False)

def main():
    run = True
    clock = pygame.time.Clock()

    # setting left paddle to ceter
    left_paddle = Paddle(
        10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    # setting right paddle to center 
    right_paddle = Paddle(
        WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, 
        PADDLE_WIDTH, PADDLE_HEIGHT)

    # main game loop
    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle])
        # getting all events IE mouse clicks, keyboard inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

    pygame.quit()

if __name__ == '__main__':
    main()