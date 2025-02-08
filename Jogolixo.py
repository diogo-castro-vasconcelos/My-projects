import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()
largura = 840
altura = 680
Pontos = 0
xplayer = largura/2
yplayer = 650
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
player_imagem = pygame.image.load("Jogolixo.py/Homem final de certeza.png")
player_imagem = pygame.transform.scale(player_imagem, (100, 100))

Lixo1_imagem = pygame.image.load("Jogolixo.py/homem das latas.png")
Lixo1_imagem = pygame.transform.scale(Lixo1_imagem, (150, 150))

Lixo2_imagem = pygame.image.load("Jogolixo.py/meu lanche.png")
Lixo2_imagem = pygame.transform.scale(Lixo2_imagem, (150, 150))

Lixo3_imagem = pygame.image.load("Jogolixo.py/Minha banana.png")
Lixo3_imagem = pygame.transform.scale(Lixo3_imagem, (150, 150))

Lixo4_imagem = pygame.image.load("Jogolixo.py/minha bebida favorita.png")
Lixo4_imagem = pygame.transform.scale(Lixo4_imagem, (150, 150))

player_rect = player_imagem.get_rect(center=(xplayer, yplayer))
Lixo1_rect = player_imagem.get_rect(center=(xlixo1, ylixo1))
Lixo2_rect = player_imagem.get_rect(center=(xlixo2, ylixo2))
Lixo3_rect = player_imagem.get_rect(center=(xlixo3, ylixo3))
Lixo4_rect = player_imagem.get_rect(center=(xlixo4, ylixo4))



while coisa == True:
    tempo = pygame.time.get_ticks()/1000
    ecra.fill((0,0,0))
    mensagem = f"Pontos: {Pontos}"
    mensagem2 = f"Tempo: {tempo}"
    Text_formatado = Fonte.render(mensagem, False, (255,255,255))
    Text_formatado2 = Fonte.render(mensagem2, False, (255,255,255))
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


    if player_rect.colliderect(Lixo1_rect):
        ylixo1 = 0
        Pontos = Pontos + 1 
        velocidade1 != 1

    if player_rect.colliderect(Lixo4_rect):
        Pontos = Pontos + 1
        ylixo4 = 0
        velocidade1 != 1
    if player_rect.colliderect(Lixo3_rect):
        Pontos = Pontos + 1
        ylixo3 = 0
        velocidade1 != 1

    if player_rect.colliderect(Lixo2_rect):
        Pontos = Pontos + 1  
        ylixo2 = 0
        velocidade1 != 1
        
        
    player_rect.center = (xplayer, yplayer)

    Lixo1_rect.center = (xlixo1, ylixo1)
    Lixo2_rect.center = (xlixo2, ylixo2)
    Lixo3_rect.center = (xlixo3, ylixo3)
    Lixo4_rect.center = (xlixo4, ylixo4)


    
        

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

    ecra.blit(player_imagem, player_rect)

    ecra.blit(Lixo1_imagem, Lixo1_rect)
    ecra.blit(Lixo2_imagem, Lixo2_rect)
    ecra.blit(Lixo3_imagem, Lixo3_rect)
    ecra.blit(Lixo4_imagem, Lixo4_rect)
    ecra.blit(Text_formatado, (450,40))
    ecra.blit(Text_formatado2, (50,40))
    pygame.display.update()
