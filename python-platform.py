import sys
import random as r
import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Platform")

cx, cy = 400, 300

player = pygame.Rect(400, 300, 20, 20)
platform = pygame.Rect(0, 500, 800, 40)

while True:
    if pygame.event.get(pygame.QUIT):
        sys.exit()

    keys = pygame.key.get_pressed()

    ox, oy = cx, cy

    if keys[pygame.K_UP]:
        cy -= 1
    if keys[pygame.K_DOWN]:
        cy += 1
    if keys[pygame.K_LEFT]:
        cx -= 1
    if keys[pygame.K_RIGHT]:
        cx += 1

    screen.fill((100, 100, 100))

    player.topleft = cx, cy

    if player.colliderect(platform):
        cx, cy = ox, oy
        player.topleft = cx, cy

    pygame.draw.rect(screen, (100, 0, 100), player)
    pygame.draw.rect(screen, (100, 100, 0), platform)


    pygame.display.flip()
