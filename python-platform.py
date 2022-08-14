import sys
import random as r
import pygame


class Block:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        w, h = screen.get_size()
        if self.x + self.w > 0 and self.x < w and self.y + self.h > 0 and self.y < h:
            pygame.draw.rect(screen, (0, 100, 100), self.rect)


class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.r = 20
        self.color = (100, 0, 100)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Platform")

player = Player(400, 300)

blocks = []

for i in range(100):
    looking = True

    while looking:
        bx, by = r.randint(-1000, 1000), r.randint(-1000, 1000)
        w, h = r.randint(20, 200), r.randint(100, 150)

        next_block = Block(bx, by, w, h)

        if blocks and next_block.rect.collidelist([b.rect for b in blocks]) != -1:
            looking = True
        else:
            looking = False

    blocks.append(next_block)


while True:
    if pygame.event.get(pygame.QUIT):
        sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.move(0, -4)
    if keys[pygame.K_DOWN]:
        player.move(0, 4)
    if keys[pygame.K_LEFT]:
        player.move(-4, 0)
    if keys[pygame.K_RIGHT]:
        player.move(4, 0)

    screen.fill((100, 100, 100))

    for b in blocks:
        b.draw()

    player.draw()

    pygame.display.flip()
