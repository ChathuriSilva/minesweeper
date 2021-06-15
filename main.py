import pygame ; from board import Grid; from player import Player, Stats; from enum import Enum, auto
surface = pygame.display.set_mode((1200, 600))
class States(Enum):
    running = auto()
    game_over = auto()
state = States.running
player = Player()
grid = Grid(player)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN and state == States.running:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid.click(pos[0], pos[1])
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                grid.mark_mine(pos[0]//30, pos[1]//30)
    surface.fill((181, 23, 158))
    if player.get_health() == 0: state = States.game_over
    if state == States.game_over: Stats.draw(surface, 'Game Over', (920, 350))
    grid.draw(surface)
    Stats.draw(surface, 'Lives remaining = '+str(player.get_health()), (950, 100))
    pygame.display.flip()