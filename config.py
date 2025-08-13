import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file from project root
load_dotenv()

# Game settings
GAME_TITLE = os.getenv('GAME_TITLE', 'Default Game')
WINDOW_WIDTH = int(os.getenv('WINDOW_WIDTH', 800))
WINDOW_HEIGHT = int(os.getenv('WINDOW_HEIGHT', 600))
FPS = int(os.getenv('FPS', 60))

# Paths - convert to absolute paths based on project root
PROJECT_ROOT = Path(__file__).parent.absolute()
ASSETS_PATH = PROJECT_ROOT / os.getenv('ENTITIES_PATH', './entities')
SCENES_PATH = PROJECT_ROOT / os.getenv('SCENES_PATH', './scenes')
FONTS_PATH = PROJECT_ROOT / os.getenv('FONTS_PATH', './fonts')
IMAGES_PATH = PROJECT_ROOT / os.getenv('IMAGES_PATH', './graphics')
SOUNDS_PATH = PROJECT_ROOT / os.getenv('SOUNDS_PATH', './audio')

# Debug settings
DEBUG_MODE = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
SHOW_FPS = os.getenv('SHOW_FPS', 'false').lower() == 'true'

# Ensure directories exist
ASSETS_PATH.mkdir(exist_ok=True)
FONTS_PATH.mkdir(parents=True, exist_ok=True)
IMAGES_PATH.mkdir(parents=True, exist_ok=True)
SOUNDS_PATH.mkdir(parents=True, exist_ok=True)