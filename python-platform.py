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

        new_rect = self.rect.move(-viewport.x, -viewport.y)

        if new_rect.colliderect(screen.get_rect()):
            pygame.draw.rect(screen, (0, 100, 100), new_rect)


class Player:
    def __init__(self, x, y):
        self.vx, self.vy = 0, 0
        self.rect = pygame.Rect(x, y, 20, 20)
        self.color = (100, 0, 100)
        self.g = 1
        self.ox, self.oy = None, None

    def draw(self):
        new_rect = self.rect.move(-viewport.x, -viewport.y)

        pygame.draw.rect(screen, self.color, new_rect)

    def move(self, dx, dy):
        self.vx += dx
        self.vy += dy

        if self.vy < -8:
            self.vy = -8


    def update(self):

        self.ox, self.oy = self.rect.topleft

        self.rect.move_ip(self.vx, self.vy)

        self.vx = 0
        self.vy += self.g


    def revert(self):
        self.rect.x, self.rect.y = self.ox, self.oy

        self.vx, self.vy = 0, 0


class Viewport:
    def __init__(self):
        self.x, self.y = 0, 0
        self.envelope = 80

    def move(self, player):
        w, h = screen.get_size()

        px, py = player.rect.topleft

        if px - self.x < self.envelope:
            self.x += px - self.x - self.envelope
        if px - self.x > w - self.envelope:
            self.x += px - self.x - (w - self.envelope)
        if py - self.y < self.envelope:
            self.y += py - self.y - self.envelope
        if py - self.y > h - self.envelope:
            self.y += py - self.y - (h - self.envelope)


pygame.init()

screen = pygame.display.set_mode((800, 600))

viewport = Viewport()

pygame.display.set_caption("Platform")

player = Player(400, 300)

blocks = []

for i in range(100):
    looking = True

    while looking:
        bx, by = r.randint(-10, 10) * 100, r.randint(-10, 10) * 100
        w, h = r.randint(2, 4) * 50, 50

        next_block = Block(bx, by, w, h)

        if blocks and next_block.rect.collidelist([b.rect for b in blocks]) != -1:
            looking = True
        elif next_block.rect.colliderect(player.rect):
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

    viewport.move(player)

    screen.fill((100, 100, 100))

    player.update()

    if player.rect.collidelist([b.rect for b in blocks]) != -1:
        player.revert()

    for b in blocks:
        b.draw()

    player.draw()

    pygame.display.flip()
