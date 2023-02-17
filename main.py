# This is a sample Python script.
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# !/usr/bin/env python
import pygame
import sys
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('images', 'snowman.png')).convert()
        img = pygame.transform.scale(img, (45, 60))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        # When space is pressed, call player.jump()
        def jump(self):
            self.jumping = True

        # Figure out what our starting position was and save it
        self.base = self.rect.y

        def update(self):
            if self.jumping:

                # Jump until we are 100 pixels above our starting point
                if not self.falling:
                    # Pygame starts with 0, 0 in the upper left of the screen
                    self.rect.y -= 1
                    if self.rect.y < self.base - 100:
                        self.falling = True
                    else:
                        # Othewise, it is time to fall
                        self.rect.y += 1
                        # If this is True we are back on ground level
                        if self.rect.y == self.base:
                            self.falling = False
                            self.jumping = False

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('CIS Hackathon!')

player = Player()
player.rect.x = 200
player.rect.y = 300
visible = pygame.sprite.Group()
visible.add(player)
running = True

def update(self):
    if self.rect.y >= 0 and self.rect.y <= 300:
        self.rect.y += 10
    else:
        self.rect.y -= 10
    if self.rect.x >= 0 and self.rect.x <= 500:
        self.rect.x -= 10

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                # W pressed, move us up!
                player.rect.y -= 10
            if event.key == pygame.K_s:
                # S pressed, move us down!
                player.rect.y += 10
            if event.key == pygame.K_a:
                # A pressed, move us up!
                player.rect.x -= 10
            if event.key == pygame.K_d:
                # D pressed, move us up!
                player.rect.x += 10
            if event.key == pygame.K_t:
                # T pressed, say something
                print("Hello!")
        update(player)


    visible.update()
    screen.fill((255, 255, 255))
    visible.draw(screen)
    pygame.display.update()