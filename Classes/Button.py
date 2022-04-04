"""A sprite to hold a button"""
import pygame.sprite
from Classes.Settings import Settings


class Button:
    """A class for arrow buttons"""
    def __init__(self, background: pygame.Surface, coordinates: tuple,
                 down_arrow=False):
        self.Settings = Settings().settings
        self.background = background
        self.image = pygame.image.load(self.Settings["Arrow Image"])
        self.image = pygame.transform.scale(self.image, (15, 15))
        if down_arrow:
            self.image = pygame.transform.flip(self.image, False, True)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = coordinates

        self.mouse_released_yet = True

    def blitme(self):
        """Draw me to the screen"""
        self.background.blit(self.image, self.image_rect)

    def clicked(self):
        """Determine if this sprite has been clicked"""
        mouse_pos = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
        if self.image_rect.colliderect(mouse_rect) and \
                pygame.mouse.get_pressed()[0]:
            if self.mouse_released_yet:
                self.mouse_released_yet = False
                return True
            else:
                return False
        self.mouse_released_yet = True
        return False
