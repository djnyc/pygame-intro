import sys
import random as r
import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Platform")


while True:
    if pygame.event.get(pygame.QUIT):
        sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        print("Up")
    if keys[pygame.K_DOWN]:
        print("Down")
    if keys[pygame.K_LEFT]:
        print("Left")
    if keys[pygame.K_RIGHT]:
        print("Right")

    screen.fill((100, 100, 100))

    pygame.display.flip()
