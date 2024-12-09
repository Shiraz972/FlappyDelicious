import pygame # type: ignore

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Game loop
running = True
while running:
    # Handle events (e.g., key presses)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects (bird, pipes, score)
    # ...

    # Draw game objects to the screen
    # ...

    # Update the display
    pygame.display.update()

pygame.quit()
