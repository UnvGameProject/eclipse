import pygame
from ui.GameWindow import Scene


class TitleScreen(Scene):
    """Title screen that displays text with fade in/out effect"""

    def __init__(self, screen_width, screen_height, text="Eclipse",
                 font_path=None, font_size=95, text_color=(255, 255, 255)):
        """
        Create a title screen
        Args:
            screen_width, screen_height: Screen dimensions
            text: Text to display
            font_path: Path to custom font file (optional)
            font_size: Size of the font
            text_color: RGB tuple for text color
        """
        super().__init__(screen_width, screen_height)

        self.text = text
        self.text_color = text_color

        # Try to load custom font, fall back to default
        try:
            if font_path:
                self.font = pygame.font.Font(font_path, font_size)
            else:
                self.font = pygame.font.Font(None, font_size)
        except FileNotFoundError:
            print(f"Font not found: {font_path}, using default font")
            self.font = pygame.font.Font(None, font_size)

        # Create the text surface (this is like "pre-rendering" the text)
        self.text_surface = self.font.render(self.text, True, self.text_color)

        # Get rectangle for centering the text
        self.text_rect = self.text_surface.get_rect(
            center=(self.screen_width // 2, self.screen_height // 2)
        )

    def draw_content(self, screen):
        """Draw the title text on screen"""
        screen.blit(self.text_surface, self.text_rect)


# You can create other specific title screen types here
class CustomTitleScreen(TitleScreen):
    """Example of extending the basic title screen"""

    def __init__(self, screen_width, screen_height):
        # Use your specific font path here
        font_path = "/Users/john/Documents/Coding_Projects/Games/eclipse/fonts/CosmicLove-O5Zp.ttf"
        super().__init__(screen_width, screen_height, "Eclipse", font_path, 95, (255, 255, 255))

        # You can customize timing here
        self.pause_length = 240  # Display for 4 seconds (240 frames at 60fps)
        self.fade_speed = 2  # Slower fade for dramatic effect


class LevelIntroScreen(TitleScreen):
    """Screen to introduce new levels"""

    def __init__(self, screen_width, screen_height, level_number):
        level_text = f"Level {level_number}"
        super().__init__(screen_width, screen_height, level_text,
                         font_size=60, text_color=(255, 255, 0))

        # Quicker timing for level intros
        self.pause_length = 120  # 2 seconds
        self.fade_speed = 5  # Fast fade