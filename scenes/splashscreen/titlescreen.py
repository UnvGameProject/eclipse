import pygame
import sys

def mainWindow():
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Text Display Example")

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Create a font object using custom font
    try:
        font = pygame.font.Font("/home/brandon/projects/eclipse/fonts/CosmicLove-O5Zp.ttf", 36)
    except FileNotFoundError:
        print("Custom font not found, using default font")
        font = pygame.font.Font(None, 36)

    # Render the text onto its own surface
    text = "Eclipse"
    text_surface = font.render(text, True, WHITE)  # anti-aliased white text
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))

    # Create a fade surface that covers the whole screen
    fade_surface = pygame.Surface((screen_width, screen_height))
    fade_surface.fill(BLACK)
    alpha = 255          # start fully opaque
    fade_speed = 3       # lower = slower fade

    # Main game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw background
        screen.fill(BLACK)

        # Draw text
        screen.blit(text_surface, text_rect)

        # Fade in by decreasing alpha until 0 (fully transparent)
        if alpha > 0:
            alpha -= fade_speed
            if alpha < 0:
                alpha = 0
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))

        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(60)

    # Quit
    pygame.quit()
    sys.exit()
