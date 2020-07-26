import pygame

# Initializes pygame module
pygame.init()

# Creates the screen for the game
screen = pygame.display.set_mode((800, 600))

# Title and Icon
icon = pygame.image.load('ufo.png')
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(icon)


# Overall Game Loop
running = True
while running:
    # RGB
    screen.fill((0, 100, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Checks if the user closes the window
            running = False
