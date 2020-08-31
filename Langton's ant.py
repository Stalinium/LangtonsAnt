import pygame
import numpy as np

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

fsize = 10
field = np.ones((int(width / fsize), int(height / fsize)), dtype=int)

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)

class Ant:

    def __init__(self, x, y, currentmove):
        self.pos = np.array([x, y])
        self.moves = [np.array([0, -1]), np.array([1, 0]), np.array([0, 1]), np.array([-1, 0])]
        self.currentmove = currentmove

    def move(self):
        self.square = field[self.pos[0]][self.pos[1]]
        if self.square:
            self.currentmove += 1
            if self.currentmove == 4:
                self.currentmove = 0
        else:
            self.currentmove -= 1
            if self.currentmove == -1:
                self.currentmove = 3

        field[self.pos[0]][self.pos[1]] = not self.square
        self.lastpos = self.pos
        self.pos = np.add(self.pos, self.moves[self.currentmove])                        

ant = Ant(int(field.shape[0] / 2), int(field.shape[1] / 2), 0)
screen.fill(pygame.Color(255, 255, 255))
pygame.display.update()

end = False
while not end:
    
    ant.move()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    color = white
    if not field[ant.lastpos[0]][ant.lastpos[1]]:
        color = black
    pygame.draw.rect(screen, color, pygame.Rect(ant.lastpos[0] * fsize, ant.lastpos[1] * fsize, fsize, fsize))
    pygame.draw.rect(screen, red, pygame.Rect(ant.pos[0] * fsize, ant.pos[1] * fsize, fsize, fsize))      

    pygame.display.update([pygame.Rect(ant.pos[0] * fsize, ant.pos[1] * fsize, fsize, fsize), pygame.Rect(ant.lastpos[0] * fsize, ant.lastpos[1] * fsize, fsize, fsize)])
    
pygame.quit()
