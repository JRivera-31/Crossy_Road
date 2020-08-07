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
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        direction = 0

        treasure = GameObject("treasure.png", 375, 50, 50, 50)
        player_character = PlayerCharacter("player.png", 375, 700, 50, 50)
        enemy_0 = EnemyCharacter("enemy.png", 20, 400, 50,50)

        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                # When user presses down a key
                elif event.type == pygame.KEYDOWN:
                    # if the key is up arrow
                    if event.key == pygame.K_UP:
                        direction = 1
                    # if the key is down arrow
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # if the user releases the key
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            self.game_screen.fill(WHITE_COLOR)
            # Draw treasure
            treasure.draw(self.game_screen)

            # Update player position
            player_character.move(direction, self.height)

            enemy_0.move(self.width)
            # Draw player
            player_character.draw(self.game_screen)
            enemy_0.draw(self.game_screen)
            
            if player_character.detect_collision(enemy_0):
                is_game_over = True
            elif player_character.detect_collision(treasure):
                is_game_over = True

            # Update display and clock tick
            pygame.display.update()
            clock.tick(self.TICK_RATE)

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (50, 50))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


class PlayerCharacter(GameObject):

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # move character up and down
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        
        # Make sure character never goes passed bottom of the screen
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40
        
    def detect_collision(self, other_body):
        # Check if overlap in y position
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        # Check if overlap in x position
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        return True


class EnemyCharacter(GameObject):
    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # move character up and down
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED

# Init pygame
pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit()