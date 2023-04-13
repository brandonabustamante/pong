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
BALL_RADIUS = 7

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

class Ball:
    MAX_VEL = 5
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
    
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

def draw(win, paddles, ball):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    # Drawing dotted line in the middle of the window
    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        
        pygame.draw.rect(win, WHITE, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))

    ball.draw(win)
    pygame.display.update()

def handle_paddle_movement(keys, left_paddle, right_paddle):
    # left paddle uses w and s keys
    # and checking if the paddle is in bounds (TOP)
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)

    # checking if the paddle is in bounds (BOTTOM)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    # right paddle uses up and down keys
    # and checking if the paddle is in bounds (TOP)
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)

    # checking if the paddle is in bounds (BOTTOM)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
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
    
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    # main game loop
    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball)
        # getting all events IE mouse clicks, keyboard inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        ball.move()

    pygame.quit()

if __name__ == '__main__':
    main()