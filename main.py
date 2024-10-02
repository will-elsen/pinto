import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player settings
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]
player_speed = 5
player_velocity_y = 0
gravity = 0.5

# Platform settings
platform_width = SCREEN_WIDTH
platform_height = 20
platform_pos = [0, SCREEN_HEIGHT - platform_height]

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pinto")

# Main game loop
running = True
on_ground = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and on_ground:
        player_velocity_y = -10  # Jump strength
        on_ground = False

    # Apply gravity
    player_velocity_y += gravity
    player_pos[1] += player_velocity_y

    # Collision detection with platform
    if player_pos[1] + player_size > platform_pos[1]:
        player_pos[1] = platform_pos[1] - player_size
        player_velocity_y = 0
        on_ground = True

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    # Draw the platform
    pygame.draw.rect(screen, GREEN, (platform_pos[0], platform_pos[1], platform_width, platform_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()