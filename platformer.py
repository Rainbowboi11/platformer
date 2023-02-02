import pygame
pygame.int()
screnwith = 400
screnhite = 600
screen = pygame.display.set_mode((screnwith,screnhite))
pygame.display.set_caption("Ducky: A Platformer")
bgimig = pygame.image.load("sky.jpeg")
run = True
while run:
    screen.blit(bgimig,(0,0))
    for event in pgame.event.get():
        if event.type == pygame.QUIT:
            run = False
