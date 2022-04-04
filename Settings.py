"""A class to manage settings for the program."""

from sys import exit as end_program
from json import load
from pygame import quit as quit_pygame


class Settings:
    """A class to manage settings."""
    def __init__(self):
        self.settings_file = "Settings.json"
        try:
            with open(self.settings_file, "r") as file:
                self.settings = load(file)
        except FileNotFoundError:
            quit_pygame()
            print("An error occured! Settings file was not found!")
            end_program()
