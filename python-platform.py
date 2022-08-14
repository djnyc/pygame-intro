import sys
import random as r
import pygame


class Block:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h

    def draw(self):
        w, h = screen.get_size()
        if self.x + self.w > 0 and self.x < w and self.y + self.h > 0 and self.y < h:
            pygame.draw.rect(screen, (0, 100, 100), pygame.Rect(self.x, self.y, self.w, self.h))


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Platform")

player_color = (100, 0, 100)
player_x, player_y = (400, 300)
player_radius = 20

blocks = []

for i in range(100):
    blocks.append(Block(r.randint(-1000, 1000), r.randint(-1000, 1000), r.randint(20, 200), r.randint(100, 150)))

while True:
    if pygame.event.get(pygame.QUIT):
        sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player_y -= 4
    if keys[pygame.K_DOWN]:
        player_y += 4
    if keys[pygame.K_LEFT]:
        player_x -= 4
    if keys[pygame.K_RIGHT]:
        player_x += 4

    screen.fill((100, 100, 100))

    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)

    for b in blocks:
        b.draw()

    pygame.display.flip()
