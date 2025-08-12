import pygame

def mainWindow():
    pygame.init()
    screen = pygame .display.set_mode((800, 600))

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    running = True
    clock = pygame .time.clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False