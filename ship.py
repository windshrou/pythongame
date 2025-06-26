import pygame

class Ship():

   def __init__(self, screen):
      self.screen = screen
      original_image = pygame.image.load('images/ship.bmp')

      # scale the image
      scale_factor = 0.1
      self.scaled_image = pygame.transform.scale(original_image, 
                                                 (original_image.get_width() * scale_factor, 
                                                  original_image.get_height() * scale_factor))

      self.rect = self.scaled_image.get_rect()
      self.screen_rect = screen.get_rect()
      self.rect.centerx = self.screen_rect.centerx
      self.rect.bottom = self.screen_rect.bottom

   def blitme(self):
       self.screen.blit(self.scaled_image, self.rect)