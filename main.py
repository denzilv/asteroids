# allows us to use code from the pygame library
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # initialize pygame
    pygame.init()

    # GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pygame.Surface.fill(screen, "black")
            pygame.display.flip()

# ensures main() is only called when this file is run directly
# won't run as an imported module and is the pythonic way
if __name__ == "__main__":
    main()
