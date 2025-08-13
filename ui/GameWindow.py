import pygame
import sys
from abc import ABC, abstractmethod
from enum import Enum


class SceneState(Enum):
    """States that a scene can be in during its lifecycle"""
    FADE_IN = 1
    DISPLAY = 2
    FADE_OUT = 3
    COMPLETE = 4


class Scene(ABC):
    """Base class for all game scenes (title screen, gameplay, menus, etc.)"""

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.state = SceneState.FADE_IN

        # Fade effect settings
        self.alpha = 255  # Start fully faded (black overlay)
        self.fade_speed = 3  # How fast to fade in/out
        self.pause_timer = 0  # Internal timer
        self.pause_length = 300  # How long to display (in frames at 60fps)

    @abstractmethod
    def draw_content(self, screen):
        """Override this method to draw your scene's content"""
        pass

    def update(self):
        """Updates the scene's fade state - called automatically"""
        if self.state == SceneState.FADE_IN:
            self.alpha -= self.fade_speed
            if self.alpha <= 0:
                self.alpha = 0
                self.state = SceneState.DISPLAY

        elif self.state == SceneState.DISPLAY:
            self.pause_timer += 1
            if self.pause_timer >= self.pause_length:
                self.state = SceneState.FADE_OUT

        elif self.state == SceneState.FADE_OUT:
            self.alpha += self.fade_speed
            if self.alpha >= 255:
                self.alpha = 255
                self.state = SceneState.COMPLETE

    def is_complete(self):
        """Returns True when the scene has finished displaying"""
        return self.state == SceneState.COMPLETE


class GameWindow:
    """Main game window that can display different scenes"""

    def __init__(self, width=800, height=600, title="Game Window", bg_color=(0, 0, 0)):
        """
        Create a new game window
        Args:
            width: Window width in pixels
            height: Window height in pixels
            title: Window title bar text
            bg_color: Background color as RGB tuple
        """
        pygame.init()

        self.width = width
        self.height = height
        self.bg_color = bg_color

        # Set up pygame display
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        # Create the black overlay surface for fade effects
        self.fade_surface = pygame.Surface((width, height))
        self.fade_surface.fill((0, 0, 0))

        # Game loop essentials
        self.clock = pygame.time.Clock()
        self.running = True

        # Scene management
        self.current_scene = None
        self.scene_queue = []

    def add_scene(self, scene):
        """Add a scene to be played in sequence"""
        self.scene_queue.append(scene)

    def run_scene(self, scene):
        """
        Run a single scene until it completes
        Returns: True if scene completed normally, False if user quit
        """
        self.current_scene = scene

        while self.running and not scene.is_complete():
            # Handle pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return False  # User closed the window

            # Update the scene (handles fade timing)
            scene.update()

            # Draw everything
            self.screen.fill(self.bg_color)
            scene.draw_content(self.screen)  # Scene draws its content

            # Apply the fade overlay
            self.fade_surface.set_alpha(scene.alpha)
            self.screen.blit(self.fade_surface, (0, 0))

            # Update the display
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS

        return True  # Scene completed successfully

    def run_all_scenes(self):
        """Run all scenes in the queue, one after another"""
        for scene in self.scene_queue:
            if not self.run_scene(scene):
                break  # Stop if user quit
        self.scene_queue.clear()

    def quit(self):
        """Clean shutdown of pygame"""
        pygame.quit()
        sys.exit()