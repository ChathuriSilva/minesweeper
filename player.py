import pygame
class Player:
    def __init__(self): self.health = 5
    def sub_health(self): self.health -= 1
    def get_health(self): return self.health
class Stats:
    def draw(surface, label, pos):
        textsurface = pygame.font.SysFont('comicsansms', 24).render(label, False, (181, 255, 255))
        surface.blit(textsurface, (pos[0], pos[1]))