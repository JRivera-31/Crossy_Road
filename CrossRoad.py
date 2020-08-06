# Get pygame library
import pygame

# Screen stuff
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Crossy RPG"
# Colors in rgb codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Define clock variable
clock = pygame.time.Clock()

class Game:

    TICK_RATE = 60
    is_game_over = False

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
    
        # Create display screen window
        self.game_screen = pygame.display.set_mode((width, height))
        # Set screen stuff
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(SCREEN_TITLE)

    def run_game_loop(self):
        is_game_over = False

        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                print(event)

            # game_screen.blit(player_image, (375, 375))

            # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
            # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)
            
            # Update display and clock tick
            pygame.display.update()
            clock.tick(self.TICK_RATE)

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (50, 50))
        self.x_pos = x
        self.y_pos = y

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))
        


# Init pygame
pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit()