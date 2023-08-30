

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_WIDTH = 100
CAR_HEIGHT = 120
ROAD_COLOR = (100, 100, 100)
LINE_COLOR = (0, 255, 0)
FPS = 60

# Load car image
car_image = pygame.image.load('car.png')
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Self-Driving Car Simulation")

# Car properties
car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 10
car_speed = 5

# Road properties
road_left = SCREEN_WIDTH // 2.5
road_right = 2.5 * SCREEN_WIDTH // 4


# Initialize background position
background_y = 0

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the background (and the road lines) to create the illusion of the car moving forward
    background_y += car_speed

    # If the background has moved completely off the screen, reset its position
    if background_y > SCREEN_HEIGHT:
        background_y = 0
        # Initialize car position randomly within road limits
        car_x = random.randint(road_left, road_right - CAR_WIDTH)
        car_y = SCREEN_HEIGHT - CAR_HEIGHT - 10

    # Clear the screen
    screen.fill(ROAD_COLOR)

    # Draw the road lines on the moving background
    line_y = background_y
    while line_y < SCREEN_HEIGHT:
        pygame.draw.rect(screen, LINE_COLOR, (road_left - 5, line_y, 10, 30))
        pygame.draw.rect(screen, LINE_COLOR, (road_right - 5, line_y, 10, 30))
        line_y += 50

    # Draw the car image on the moving background
    screen.blit(car_image, (car_x, car_y))

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
