"""A timer class"""

import pygame
from sys import exit as end_program
from Settings import Settings
from os import system


class Timer:
    """A class to keeep track of everything."""

    def __init__(self):
        self.settings = Settings().settings

        pygame.init()

        self.screen = pygame.display.set_mode(self.settings["Screen Size"])
        pygame.display.set_caption(self.settings["Screen Caption"])

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.settings["Screen Background Colour"])

        self.font = pygame.font.Font(None, self.settings["Font Size"])

        self.hrs = 0
        self.mins = 0
        self.secs = 0
        self.sound_played = False

    def run(self):
        """Run the main loop for the program."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_program()

                elif event.type == pygame.TEXTINPUT:
                    self.timer_up()

            if self.hrs == self.mins == self.secs == 0 and not \
                    self.sound_played:
                self.sound_played = True
                self.timer_up()

            self.screen.blit(self.background, (0, 0))

            pygame.display.flip()

    def timer_up(self):
        """Show a notification and (if configured) play a sound"""
        system(f"""
               osascript -e 'display notification "" with title "Timer Done"'
               """)
        pygame.mixer.music.load(self.settings["Timer Sound"])
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()


def main():
    """Run the timer."""
    timer = Timer()
    timer.run()


if __name__ == "__main__":
    main()
