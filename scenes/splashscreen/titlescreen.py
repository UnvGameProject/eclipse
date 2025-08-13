import pygame

def mainWindow():
    import pygame
    import sys

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
    BLUE = (0, 0, 255)

    # Create a font object using custom font
    try:
        font = pygame.font.Font("/Users/john/Documents/Coding_Projects/Games/eclipse/fonts/CosmicLove-O5Zp.ttf", 36)
    except FileNotFoundError:
        print("Custom font not found, using default font")
        font = pygame.font.Font(None, 36)

    # Render the text
    text = "Eclipse"
    text_surface = font.render(text, True, BLACK)  # True for anti-aliasing

    # Get text rectangle for positioning
    text_rect = text_surface.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)  # Center the text

    # Main game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw the text
        screen.blit(text_surface, text_rect)

        # Update the display
        pygame.display.flip()

        # Control frame rate
        clock.tick(60)

    # Quit
    pygame.quit()
    sys.exit()