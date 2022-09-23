import pygame
from pathlib import Path
from settings import *

data_folder = Path("graphics/test/")

rock_asset = data_folder / "rock.png"


class Tile(pygame.sprite.Sprite):

    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load(rock_asset).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
