import pygame
from settings import Settings
from ship import Ship
def run_game():
    pygame.init()
    ai_settings = Settings()   
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship =Ship(screen) 
    pygame.display.set_caption("alice invasion")
    while True :
     screen.fill(ai_settings.bg_color)
     ship.blitme()
     pygame .display.flip()
run_game()
