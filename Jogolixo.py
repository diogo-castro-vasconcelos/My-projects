import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()
largura = 840
altura = 680
xplayer = largura/2
yplayer = 580
xlixo1 = 740
xlixo2 = 140
xlixo3 = 340
xlixo4 = 540
ylixo1 = 0
ylixo2 = 0
ylixo3 = 0
ylixo4 = 0
relogio = pygame.time.Clock()

ecra = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Apanhó lixo")

while True:
    relogio.tick(50)
    ecra.fill((0,0,0))
    pygame.draw.circle(ecra, (255,255,0), (xplayer, yplayer), 10 )
    pygame.draw.rect(ecra, (255,0,255), (xlixo1,ylixo1,50,63))
    pygame.draw.rect(ecra, (255,0,255), (xlixo2,ylixo2,50,63))
    pygame.draw.rect(ecra, (255,0,255), (xlixo3,ylixo3,50,63))
    pygame.draw.rect(ecra, (255,0,255), (xlixo4,ylixo3,50,63))
    
    if ylixo1 >= altura:
        ylixo1 = 0
    
    ylixo1 = ylixo1 + 7
    if ylixo2 >= altura:
        ylixo2 = 0
    
    ylixo2 = ylixo2 + 8

    if ylixo3 >= altura:
        ylixo3 = 0
    
    ylixo3 = ylixo3 + 9

    if ylixo4 >= altura:
        ylixo4 = 0
    
    ylixo4 = ylixo4 + 10


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
