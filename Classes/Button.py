"""A sprite to hold a button"""
from Classes.Settings import Settings
from pygame import Surface, Rect
from pygame.image import load
from pygame.transform import scale, flip
from pygame.mouse import get_pos, get_pressed


class Button:
    """A class for arrow buttons"""
    def __init__(self, background: Surface, coordinates: tuple,
                 down_arrow=False):
        self.Settings = Settings().settings
        self.background = background
        self.image = load(self.Settings["Arrow Image"])
        self.image = scale(self.image, (15, 15))
        if down_arrow:
            self.image = flip(self.image, False, True)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = coordinates

        self.mouse_released_yet = True

    def blitme(self):
        """Draw me to the screen"""
        self.background.blit(self.image, self.image_rect)

    def clicked(self):
        """Determine if this sprite has been clicked"""
        mouse_pos = get_pos()
        mouse_rect = Rect(mouse_pos[0], mouse_pos[1], 1, 1)
        if self.image_rect.colliderect(mouse_rect) and \
                get_pressed()[0]:
            if self.mouse_released_yet:
                self.mouse_released_yet = False
                return True
            else:
                return False
        self.mouse_released_yet = True
        return False
