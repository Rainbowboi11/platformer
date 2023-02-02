import pygame
pygame.int()
screnwith = 400
screnhite = 600
screen = pygame.display.set_mode((screnwith,screnhite))
pygame.display.set_caption("Ducky: A Platformer")
bgimig = pygame.image.load("sky.jpeg")
playrimig = pygame.image.load("duck.png")

class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(playrimig, (59,80))
        self.width = 80
        self.height = 59
        self.rect = pygame
        self.rect.center = (x, y)
    def draw():
        screen.blit(self.image, (self.rect.x - 12, self.rect.y -5))
        pygame.draw.rect(screen,WHITE, self.rect, 2)

run = True
while run:
    screen.blit(bgimig,(0,0))
    for event in pgame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
