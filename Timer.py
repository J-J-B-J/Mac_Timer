"""A timer class"""

import pygame
import sys


class Timer:
    """A class to keeep track of everything."""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 100))
        pygame.display.set_caption("MacTimer")

    def run(self):
        """Run the main loop for the program."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


def main():
    """Run the timer."""
    timer = Timer()
    timer.run()

if __name__ == "__main__":
    main()
