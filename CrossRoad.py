# Get pygame library
import pygame

# Init pygame
pygame.init()

# Screen stuff
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Crossy RPG"
# Colors in rgb codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Define clock variable
clock = pygame.time.Clock()
TICK_RATE = 60
is_game_over = False

# Create display screen window
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set background color
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

while not is_game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True
        print(event)
    
    # Update display and clock tick
    pygame.display.update()
    clock.tick(TICK_RATE)

pygame.quit()
quit()