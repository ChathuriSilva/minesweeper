import pygame; from random import randint
pygame.font.init()
class Cell:
    def __init__(self, pos, random_mine):
        self.visible = False
        self.mine = random_mine
        self.show_mine = False
        self.size = 30
        self.color = (200, 200, 200)
        self.pos = pos
        self.mine_counter = 0
        self.explosion = False
    def draw(self, surface):
        if self.visible: pygame.draw.rect(surface, self.color, (self.pos[0], self.pos[1], self.size, self.size))
        else: pygame.draw.rect(surface, (50,50,50), (self.pos[0], self.pos[1], self.size, self.size))
        if self.show_mine and self.mine: pygame.draw.circle(surface, (10,10,10), (self.pos[0]+15, self.pos[1]+15), 15)
        if self.explosion: pygame.draw.circle(surface, (255,10,10), (self.pos[0]+15, self.pos[1]+15), 15)
class Grid:
    def __init__(self, player):
        self.player = player
        self.cells = []
        self.search_dirs = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
        for y in range(30):
            self.cells.append([])
            for x in range(30):
                self.cells[y].append(Cell((x*30, y*30), self.random_mines()))
        self.lines =[]
        for y in range(1, 31, 1):
            temp = []
            temp.append((0, y * 30)), temp.append((900, y * 30))
            self.lines.append(temp)
        for x in range(1, 31, 1):
            temp = []
            temp.append((x*30, 0)), temp.append((x*30, 900))
            self.lines.append(temp)
    def random_mines(self):
        if randint(0, 10) > 9: return True
        else: return False
    def draw(self, surface):
        for row in self.cells:
            for cell in row: cell.draw(surface)
        for line in self.lines: pygame.draw.line(surface, (0, 125, 0), line[0], line[1])
    def is_within_bounds(self, x, y): return x >= 0 and x < 30 and y >= 0 and y < 30
    def search(self, x, y):
        if not self.is_within_bounds(x, y):
            return
        cell = self.cells[y][x]
        if cell.visible: return
        if cell.mine:
            cell.explosion = True
            self.player.sub_health()
            return
        cell.visible = True
        num_mines = self.num_of_mines(x, y)
        if num_mines > 0:
            cell.mine_counter = str(num_mines)
            return
        for xx, yy in self.search_dirs: self.search(x+xx, y+yy)
    def num_of_mines(self, x, y):
        counter = 0
        for xx, yy in self.search_dirs:
            if self.is_within_bounds(x + xx, y + yy) and self.cells[y + yy][x + xx].mine: counter += 1
        return counter
    def click(self, x, y):
        grid_x, grid_y = x//30, y//30
        self.search(grid_x, grid_y)