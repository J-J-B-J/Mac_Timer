"""A timer class"""

from pygame import init, Surface, QUIT, KEYDOWN, K_RETURN, K_r, KEYUP
from pygame.display import set_mode, set_caption, set_icon, flip
from pygame.image import load
from pygame.font import Font
from pygame.event import get
from pygame.mixer import music
from sys import exit as end_program
from Classes.Settings import Settings
from os import system
from Classes.Text import *
from Classes.Button import Button
from time import time


def one_to_two_digits(num):
    """Take a number and, if it is one digit, return that number with s 0 in
    font of it"""
    num = str(num)
    if len(num) == 1:
        return "0" + num
    return num


class Timer:
    """A class to keeep track of everything."""

    def __init__(self):
        self.settings = Settings().settings

        init()  # Init pygame

        self.screen = set_mode(self.settings["Screen Size"])
        set_caption(self.settings["Screen Caption"])
        logo = load(self.settings["Logo"])
        set_icon(Surface.convert(logo))

        self.background = Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.settings["Screen Background Colour"])

        self.font = Font(None, self.settings["Timer Size"])

        self.hrs = 0
        self.mins = 0
        self.secs = 0
        self.playing = False
        self.sound_played = True
        self.time_text = TimeText("0:00:00", self.font,
                                  self.settings["Timer Colour"],
                                  self.background)
        self.previous_play_time = 0
        self.key_released = True

        self.buttons = [
            ["hrs", 1, Button(self.background, (45, 14))],
            ["hrs", -1, Button(self.background, (45, 82), True)],
            ["mins", 10, Button(self.background, (93, 14))],
            ["mins", -10, Button(self.background, (93, 82), True)],
            ["mins", 1, Button(self.background, (128, 14))],
            ["mins", -1, Button(self.background, (128, 82), True)],
            ["secs", 10, Button(self.background, (176, 14))],
            ["secs", -10, Button(self.background, (176, 82), True)],
            ["secs", 1, Button(self.background, (211, 14))],
            ["secs", -1, Button(self.background, (211, 82), True)],
        ]

    def run(self):
        """Run the main loop for the program."""
        while True:
            for event in get():
                if event.type == QUIT:
                    end_program()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and self.key_released:
                        if self.playing:
                            self.playing = False
                        else:
                            self.playing = True
                            self.sound_played = False
                        self.key_released = False
                    elif event.key == K_r:
                        self.hrs = 0
                        self.mins = 0
                        self.secs = 0
                        self.sound_played = True
                        self.playing = False
                elif event.type == KEYUP:
                    if event.key == K_RETURN:
                        self.key_released = True

            if self.hrs == self.mins == self.secs == 0 and not \
                    self.sound_played:
                self.sound_played = True
                self.timer_up()
                self.playing = False

            self.screen.blit(self.background, (0, 0))
            self.background.fill(self.settings["Screen Background Colour"])
            for button_data in self.buttons:
                button_data[2].blitme()
                if button_data[2].clicked():
                    if button_data[0] == "hrs":
                        self.hrs += button_data[1]
                        if self.hrs < 0:
                            self.hrs += 10
                        elif self.hrs > 9:
                            self.hrs -= 10
                    elif button_data[0] == "mins":
                        self.mins += button_data[1]
                        if self.mins < 0:
                            self.mins += 60
                        elif self.mins > 59:
                            self.mins -= 60
                    elif button_data[0] == "secs":
                        self.secs += button_data[1]
                        if self.secs < 0:
                            self.secs += 60
                        elif self.secs > 59:
                            self.secs -= 60

            if self.playing and self.previous_play_time + 1 <= time():
                self.previous_play_time = time()
                if self.secs > 0:
                    self.secs -= 1
                else:
                    if self.mins > 0:
                        self.mins -= 1
                        self.secs = 59
                    else:
                        if self.hrs > 0:
                            self.hrs -= 1
                            self.mins = 59
                            self.secs = 59
                        else:
                            self.hrs = 0
                            self.mins = 0
                            self.secs = 0

            text = f"{self.hrs}:{one_to_two_digits(self.mins)}:\
{one_to_two_digits(self.secs)}"
            self.time_text = TimeText(text, self.font,
                                      self.settings["Timer Colour"],
                                      self.background)

            self.time_text.blitme()
            flip()

    def timer_up(self):
        """Show a notification and (if configured) play a sound"""
        system(f"""
               osascript -e 'display notification "Your timer just went off" \
               with title "Timer Done"'
               """)
        if self.settings["Play Sound"]:
            music.load(self.settings["Timer Sound"])
            music.set_volume(0.2)
            music.play()


def main():
    """Run the timer."""
    timer = Timer()
    timer.run()


if __name__ == "__main__":
    main()
