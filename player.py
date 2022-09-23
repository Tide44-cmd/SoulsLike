import pygame
from settings import *

data_folder = Path("graphics/test/")

player_asset = data_folder / "player.png"

class Player(pygame.sprite.Sprite):

    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load(player_asset).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)