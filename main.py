import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Obstacle Dodge Game")

# Colors
white = (255, 255, 255)
blue = (0, 0, 0)
red = (255, 0, 0)

# Car settings
car_width, car_height = 50, 80
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 10
car_speed = 10

# Obstacle settings
obstacle_width, obstacle_height = 50, 80
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = obstacle_height
obstacle_speed = 5

# Score and font settings
score = 0
font = pygame.font.Font(None, 36)

# Set up game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    if car_x < 0:
        car_x = 0
    elif car_x > screen_width - car_width:
        car_x = screen_width - car_width

    obstacle_y += 2 * obstacle_speed
    if obstacle_y > screen_height:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        score += 1

    screen.fill(white)

    pygame.draw.rect(screen, blue, (car_x, car_y, car_width, car_height))

    pygame.draw.rect(screen, red, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    score_text = font.render("Score: " + str(score), True, blue)
    screen.blit(score_text, (10, 10))

    if car_y < obstacle_y + obstacle_height:
        if (car_x > obstacle_x and car_x < obstacle_x + obstacle_width) or (car_x + car_width > obstacle_x and car_x + car_width < obstacle_x + obstacle_width):
            game_over_text = font.render("Game Over! Final Score: " + str(score), True, blue)
            screen.fill(white)
            screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
            pygame.display.flip()
            
            pygame.time.delay(2000)
            running = False

    pygame.display.update()

    clock.tick(60)

pygame.quit()
