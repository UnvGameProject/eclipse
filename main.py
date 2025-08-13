from ui import GameWindow
from scenes.splashscreen import titlescreen


def main():
    """Main game function - this is where your game starts"""

    # Create the main game window
    window = GameWindow.GameWindow(
        width=800,
        height=600,
        title="Eclipse Game",
        bg_color=(0, 0, 0)  # Black background
    )

    # Example 1: Simple title screen
    simple_title = titlescreen.TitleScreen(800, 600, "Welcome!")

    # Example 2: Your original Eclipse title with custom font
    eclipse_title = titlescreen.CustomTitleScreen(800, 600)

    # Example 3: Level intro screens
    level_1_intro = titlescreen.LevelIntroScreen(800, 600, 1)
    level_2_intro = titlescreen.LevelIntroScreen(800, 600, 2)

    # Option A: Run a single scene
    print("Running single title screen...")
    window.run_scene(eclipse_title)

    # Option B: Run multiple scenes in sequence
    print("Running scene sequence...")
    window.add_scene(simple_title)
    window.add_scene(level_1_intro)
    window.add_scene(level_2_intro)
    window.run_all_scenes()

    # Always clean up at the end
    window.quit()


def quick_title_demo():
    """Quick demo function showing minimal setup"""
    window = GameWindow.GameWindow(title="Quick Demo")
    title = titlescreen.TitleScreen(800, 600, "Hello World!", font_size=60)
    window.run_scene(title)
    window.quit()


if __name__ == "__main__":
    main()
    # Uncomment this line instead to run the quick demo:
    # quick_title_demo()