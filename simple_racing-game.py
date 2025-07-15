import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 400
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 80
CAR_WIDTH, CAR_HEIGHT = 20, 40
CAR_SPEED = 4
BG_COLOR = (30, 30, 30)
PADDLE_COLOR = (100, 240, 100)
CAR_COLOR = (240, 100, 100)
TEXT_COLOR = (255, 255, 255)

# Setup Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Racing Game")
clock = pygame.time.Clock()

# Paddle (Player)
paddle_x = 30
paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Cars (AI Opponents)
cars = []
for i in range(3):
    lane_y = 60 + i * 100
    car_x = random.randint(WIDTH // 2, WIDTH - CAR_WIDTH)
    cars.append({'x': car_x, 'y': lane_y, 'speed': CAR_SPEED + random.randint(0, 2)})

# Score
score = 0
font = pygame.font.SysFont(None, 36)

def draw_paddle(y):
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle_x, y, PADDLE_WIDTH, PADDLE_HEIGHT))

def draw_cars():
    for car in cars:
        pygame.draw.rect(screen, CAR_COLOR, (car['x'], car['y'], CAR_WIDTH, CAR_HEIGHT))

def show_score(score):
    score_surf = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_surf, (10, 10))

def check_collision(paddle_y, cars):
    for car in cars:
        if (paddle_x < car['x'] + CAR_WIDTH and
            paddle_x + PADDLE_WIDTH > car['x'] and
            paddle_y < car['y'] + CAR_HEIGHT and
            paddle_y + PADDLE_HEIGHT > car['y']):
            return True
    return False

def reset_cars(cars):
    for car in cars:
        car['x'] = random.randint(WIDTH // 2, WIDTH - CAR_WIDTH)
        car['y'] = 60 + cars.index(car) * 100

# Main Game Loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BG_COLOR)

    # Mouse controls paddle's Y axis
    mouse_y = pygame.mouse.get_pos()[1]
    paddle_y = mouse_y - PADDLE_HEIGHT // 2
    paddle_y = max(0, min(HEIGHT - PADDLE_HEIGHT, paddle_y))

    # Move Cars
    for car in cars:
        car['x'] -= car['speed']
        if car['x'] < -CAR_WIDTH:
            car['x'] = WIDTH
            car['speed'] = CAR_SPEED + random.randint(0, 2)
            score += 1

    # Draw everything
    draw_paddle(paddle_y)
    draw_cars()
    show_score(score)

    # Collision Detection
    if check_collision(paddle_y, cars):
        # Game Over Screen
        game_over_surf = font.render("Game Over! Press R to Restart", True, TEXT_COLOR)
        screen.blit(game_over_surf, (WIDTH // 2 - 150, HEIGHT // 2 - 20))
        pygame.display.flip()
        # Wait for restart
        wait_restart = True
        while wait_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    # Reset everything
                    score = 0
                    reset_cars(cars)
                    wait_restart = False
            clock.tick(10)
    else:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

pygame.quit()
