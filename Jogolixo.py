import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()
largura = 840
altura = 680
xplayer = largura/2
yplayer = 670
xlixo1 = 740
xlixo2 = 140
xlixo3 = 340
xlixo4 = 540
ylixo1 = 0
ylixo2 = 0
ylixo3 = 0
ylixo4 = 0
coisa = True
ecra = pygame.display.set_mode((largura, altura))
b =   pygame.draw.circle(ecra, (255,255,0), (xplayer, yplayer), 10 )
a =   pygame.draw.rect(ecra, (255,0,255), (xlixo1,ylixo1,50,63))
c =  pygame.draw.rect(ecra, (255,0,255), (xlixo2,ylixo2,50,63))
d =    pygame.draw.rect(ecra, (255,0,255), (xlixo3,ylixo3,50,63))
e =    pygame.draw.rect(ecra, (255,0,255), (xlixo4,ylixo3,50,63))
    
pygame.display.set_caption("Apanhó lixo")

while coisa == True:
    ecra.fill((0,0,0))
    
    if ylixo1 >= altura:
        ylixo1 = 0
    
    ylixo1 = ylixo1 + 0.7
    if ylixo2 >= altura:
        ylixo2 = 0
    
    ylixo2 = ylixo2 + 0.8

    if ylixo3 >= altura:
        ylixo3 = 0
    
    ylixo3 = ylixo3 + 0.9

    if ylixo4 >= altura:
        ylixo4 = 0
    
    ylixo4 = ylixo4 + 1.0


    if a.colliderect(b):
        coisa == False
        

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                xplayer = xplayer + -50
            if event.key == K_d:
                xplayer = xplayer + 50
            if event.key == K_RIGHT:
                xplayer = xplayer + 50
            if event.key == K_LEFT:
                xplayer = xplayer + -50

    
    pygame.display.update()
