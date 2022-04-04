"""A class to print text"""
import pygame.font


class Text:
    """A class to take care of text"""
    def __init__(self, text: str, font: pygame.font.Font, colour: list,
                 background: pygame.Surface):
        self.font = font
        self.text = font.render(text, True, tuple(colour))
        self.textpos = self.text.get_rect()
        self.background = background
        self.textpos.center = self.background.get_rect().center

    def blitme(self):
        """Display the text to the screen."""
        self.background.blit(self.text, self.textpos)


class TimeText(Text):
    """A class to take care of the timer text"""
    def __init__(self, text: str, font: pygame.font.Font, colour: list,
                 background: pygame.Surface):
        super().__init__(text, font, colour, background)
        self.textpos.centery = self.background.get_rect().centery
        self.textpos.left = self.background.get_rect().left + 30

    def blitme(self):
        """Display the text to the screen."""
        self.background.blit(self.text, self.textpos)
