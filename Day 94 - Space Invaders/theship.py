import pygame
class TheShip:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.ship_image = self.mask.to_surface()

    def draw_ship(self, window):
        window.blit(self.image, (self.x, self.y))
