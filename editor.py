import pygame, sys
from pygame.math import Vector2 as vector
from settings import *
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos
# Origin is a vector with (x,y) and every element relative to it
class Editor:
  def __init__(self):

    # main setup
    self.display_surface = pygame.display.get_surface()
    self.pan_active = False
    self.pan_offset = vector()

    #navigation
    self.origin = vector()

  #input
  def event_loop(self):
    # event looop
    # close the game
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          self.pan_input(event)

  def pan_input(self, event):

    # middle mouse button pressed or released
    if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[1]:
      self.pan_active = True
      self.pan_offset = vector(mouse_pos()) - self.origin
    if not mouse_buttons()[1]:
      self.pan_active = False

    # panning update
    if self.pan_active:
      self.origin = vector(mouse_pos()) - self.pan_offset

    if event.type == pygame.MOUSEWHEEL:
      if pygame.key.get_pressed()[pygame.K_LCTRL]:
        self.origin.y -= event.y*50
      else:
        self.origin.x -= event.y * 50

  # Drawing
  def draw_tile_lines(self):
    cols = WINDOW_WIDTH // TILE_SIZE
    rows
  def run(self, dt):
    self.display_surface.fill('white')
    self.event_loop()
    pygame.draw.circle(self.display_surface, 'red', self.origin, 10)