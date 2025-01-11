import pygame
from pygame.locals import *
from sys import exit

pygame.init()
largura = 840
altura = 680
xplayer = largura/2
yplayer = 580
xlixo1 = 630
ylixo1 = 40

ecra = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Apanhó lixo")

while True:
    pygame.draw.circle(ecra, (255,255,0), (xplayer, yplayer), 10 )
    pygame.draw.rect(ecra, (255,0,255), (xlixo1, ylixo1) )
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()