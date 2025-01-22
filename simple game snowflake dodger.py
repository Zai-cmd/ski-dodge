import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ski Dodger")

# Load character image
ski_character = pygame.image.load('ski.png')
ski_character = pygame.transform.scale(ski_character, (50, 50))
character_width = ski_character.get_width()
character_height = ski_character.get_height()

# Load tree image
tree_image = pygame.image.load('tree.png')
tree_image = pygame.transform.scale(tree_image, (30, 30))

# Character position
character_x = (SCREEN_WIDTH // 2) - (character_width // 2)
character_y = SCREEN_HEIGHT - character_height - 10

# Tree properties
tree_width = tree_image.get_width()
tree_height = tree_image.get_height()
tree_speed = 5
tree_frequency = 10  # Lower value means more frequent trees

# Game variables
clock = pygame.time.Clock()
score = 0
speed_increase = 0.01  # Increase in speed per frame

# Font for displaying score
font = pygame.font.Font(None, 36)

# Function to draw trees
def draw_trees(trees):
    for tree in trees:
        screen.blit(tree_image, (tree.x, tree.y))

# Main game loop
def game_loop():
    global character_x, tree_speed, score
    running = True
    trees = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and character_x > 0:
            character_x -= 5
        if keys[pygame.K_RIGHT] and character_x < SCREEN_WIDTH - character_width:
            character_x += 5

        # Add new trees
        if random.randint(1, tree_frequency) == 1:
            trees.append(pygame.Rect(random.randint(0, SCREEN_WIDTH - tree_width), 0, tree_width, tree_height))

        # Move trees
        for tree in trees:
            tree.y += tree_speed

        # Remove trees that have fallen off the screen
        trees = [tree for tree in trees if tree.y < SCREEN_HEIGHT]

        # Check for collisions
        for tree in trees:
            if tree.colliderect(pygame.Rect(character_x, character_y, character_width, character_height)):
                running = False  # End game on collision

        # Increase speed and score
        tree_speed += speed_increase
        score += 1

        # Draw everything
        screen.fill(BLACK)
        draw_trees(trees)
        screen.blit(ski_character, (character_x, character_y))

        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    # Game over screen
    screen.fill(BLUE)
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

game_loop()
pygame.quit()