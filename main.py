# allows us to use code from the pygame library
import pygame
from constants import *
from player import Player

def main():
    # initialize pygame
    pygame.init()

    # GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # limit to 60 FPS framerate
        dt = clock.tick(60) / 1000


# ensures main() is only called when this file is run directly
# won't run as an imported module and is the pythonic way
if __name__ == "__main__":
    main()
