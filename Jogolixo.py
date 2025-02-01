import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()
largura = 840
altura = 680
Pontos = 0
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
velocidade1 = 0.1
velocidade2 =0.3
velocidade3 =0.2
velocidade4 = 0.1
coisa = True
Fonte = pygame.font.SysFont("Times New Roman", 40 , True, False)
Fonte2 = pygame.font.SysFont("Times New Roman", 40 , True, False)
ecra = pygame.display.set_mode((largura, altura))
    
pygame.display.set_caption("Apanhó lixo")

while coisa == True:
    tempo = pygame.time.get_ticks()/1000
    ecra.fill((0,0,0))
    mensagem = f"Pontos: {Pontos}"
    mensagem2 = f"Tempo: {tempo}"
    Text_formatado = Fonte.render(mensagem, False, (255,255,255))
    Text_formatado2 = Fonte.render(mensagem2, False, (255,255,255))
    player =   pygame.draw.circle(ecra, (255,255,0), (xplayer, yplayer), 10 )
    Lixo1 =   pygame.draw.rect(ecra, (255,0,255), (xlixo1,ylixo1,50,63))
    Lixo2 =  pygame.draw.rect(ecra, (255,0,255), (xlixo2,ylixo2,50,63))
    Lixo3 =    pygame.draw.rect(ecra, (255,0,255), (xlixo3,ylixo3,50,63))
    Lixo4 =    pygame.draw.rect(ecra, (255,255,255), (xlixo4,ylixo4,50,63))
    if tempo >= 25 or Pontos == 10:
        coisa == False
        pygame.quit()
        exit()
    if ylixo1 >= altura:
        ylixo1 = 0
    
    ylixo1 = ylixo1 + velocidade1
    if ylixo2 >= altura:
        ylixo2 = 0
    
    ylixo2 = ylixo2 + velocidade2

    if ylixo3 >= altura:
        ylixo3 = 0
    
    ylixo3 = ylixo3 + velocidade3

    if ylixo4 >= altura:
        ylixo4 = 0
    
    ylixo4 = ylixo4 + velocidade4


    if player.colliderect(Lixo1):
        ylixo1 = 0
        Pontos = Pontos + 1 
        yplayer = 670
        velocidade1 != 1

    if player.colliderect(Lixo4):
        Pontos = Pontos + 1
        ylixo4 = 0
        yplayer = 670
        velocidade1 != 1
    if player.colliderect(Lixo3):
        Pontos = Pontos + 1
        ylixo3 = 0
        yplayer = 670
        velocidade1 != 1

    if player.colliderect(Lixo2):
        Pontos = Pontos + 1  
        ylixo2 = 0
        yplayer = 670
        velocidade1 != 1

    
        

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

    ecra.blit(Text_formatado, (450,40))
    ecra.blit(Text_formatado2, (50,40))
    pygame.display.update()
