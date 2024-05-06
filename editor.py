import pygame
from settings import *

class Editor:
  def __init__(self):

    # main setup
    self.display_surface = pygame.display.get_surface()

  def run(self, dt):
    self.display_surface.fill('white')
    