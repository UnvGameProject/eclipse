from time import sleep

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
        font = pygame.font.Font("/Users/john/Documents/Coding_Projects/Games/eclipse/fonts/CosmicLove-O5Zp.ttf", 95)
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

    # Fade control variables
    alpha = 255  # start fully opaque (black screen covering text)
    fade_speed = 3  # how fast we fade (lower = slower)
    fade_is_done = False  # tracks if we've finished fading IN
    pause_timer = 0  # counts frames during the pause
    pause_length = 300  # how long to pause (2 seconds at 60fps)

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

        # STEP 1: Fade IN (make text visible)
        if not fade_is_done:
            # Make the black overlay more transparent each frame
            alpha -= fade_speed
            if alpha <= 0:
                alpha = 0
                fade_is_done = True  # fade in is complete
        else:
            # STEP 2: Pause (let people read the text)
            if pause_timer < pause_length:
                pause_timer += 1
            else:
                # STEP 3: Fade OUT (hide text again)
                # Make the black overlay more opaque each frame
                alpha += fade_speed
                if alpha >= 255:
                    alpha = 255

        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))

        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(60)

    # Quit
    pygame.quit()
    sys.exit()