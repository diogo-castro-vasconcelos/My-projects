import pygame
import time
from pygame.locals import *
from sys import exit

pygame.init()

coisa = True
largura = 840
altura = 680
x = 75
y = 0
x2 = 200
y2 = 0
x3 = 400
y3 = 0
x4 = 700
y4 = 0
x5 = 550
y5 = 0
xplayer = 0
yplayer = altura/2
xfim = largura
yfim = altura
velocidade_player = 5  # Velocidade de movimento do jogador
ecra = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption("Jogo do Sapo")

def criar_caixa_mensagem(tela, mensagem, pos_x, pos_y, cor_texto=(255, 255, 255), cor_fundo=(0, 0, 0), tamanho_fonte=32):
    fonte = pygame.font.Font(None, tamanho_fonte)
    texto_surface = fonte.render(mensagem, True, cor_texto)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = (pos_x, pos_y)
    padding = 20
    fundo_rect = pygame.Rect(
        texto_rect.left - padding,
        texto_rect.top - padding,
        texto_rect.width + (padding * 2),
        texto_rect.height + (padding * 2)
    )
    pygame.draw.rect(tela, cor_fundo, fundo_rect)
    pygame.draw.rect(tela, cor_texto, fundo_rect, 2)
    tela.blit(texto_surface, texto_rect)

def perdeste():
    print("Perdeste!!")
    criar_caixa_mensagem(
        tela=ecra,
        mensagem="O sapo foi atropelado! Fim de jogo",
        pos_x=320,
        pos_y=240,
        cor_texto=(255, 255, 255),
        cor_fundo=(0, 0, 0),
        tamanho_fonte=32
    )

def Ganhaste():
    print("Ganhaste!!")
    criar_caixa_mensagem(
        tela=ecra,
        mensagem="O sapo chegou ao outro lado! Parabéns!",
        pos_x=320,
        pos_y=240,
        cor_texto=(255, 255, 255),
        cor_fundo=(0, 0, 0),
        tamanho_fonte=32
    )

def desenhar_carro(superficie, x, y, cor, tamanho=(60, 30)):
    # Corpo do carro
    pygame.draw.rect(superficie, cor, (x, y, tamanho[0], tamanho[1]))
    # Rodas
    pygame.draw.circle(superficie, (0,0,0), (x + 10, y + tamanho[1]), 5)
    pygame.draw.circle(superficie, (0,0,0), (x + tamanho[0] - 10, y + tamanho[1]), 5)
    return pygame.Rect(x, y, tamanho[0], tamanho[1])

def desenhar_sapo(superficie, x, y):
    # Corpo do sapo (verde)
    corpo = pygame.draw.ellipse(superficie, (34, 139, 34), (x, y, 40, 35))
    # Olhos (brancos com centro preto)
    pygame.draw.circle(superficie, (255, 255, 255), (x + 10, y + 10), 5)
    pygame.draw.circle(superficie, (255, 255, 255), (x + 30, y + 10), 5)
    pygame.draw.circle(superficie, (0, 0, 0), (x + 10, y + 10), 2)
    pygame.draw.circle(superficie, (0, 0, 0), (x + 30, y + 10), 2)
    return corpo

while coisa == True:
    # Desenhar fundo da estrada
    ecra.fill((70,70,70))  # Cor cinza para asfalto
    
    # Desenhar faixas da estrada
    for i in range(0, altura, 50):
        pygame.draw.rect(ecra, (255,255,255), (largura//2 - 5, i, 10, 30))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Verificar teclas pressionadas para movimento contínuo
    teclas = pygame.key.get_pressed()
    if teclas[K_d] and xplayer < largura - 40:  # Limita movimento à direita
        xplayer += velocidade_player
    if teclas[K_a] and xplayer > 0:  # Limita movimento à esquerda
        xplayer -= velocidade_player
    if teclas[K_s] and yplayer < altura - 35:  # Limita movimento para baixo
        yplayer += velocidade_player
    if teclas[K_w] and yplayer > 0:  # Limita movimento para cima
        yplayer -= velocidade_player

    # Desenhar carros
    carro_vermelho = desenhar_carro(ecra, x, y, (180,30,60))
    carro_verde = desenhar_carro(ecra, x3, y3, (15,250,190))
    carro_azulescuro = desenhar_carro(ecra, x4, y4, (40,3,200))
    carro_branco = desenhar_carro(ecra, x5, y5, (255,255,255))
    carro_azul = desenhar_carro(ecra, x2, y2, (30,120,60))
    
    # Jogador (sapo)
    player = desenhar_sapo(ecra, xplayer, yplayer)

    # Linha de chegada
    End = pygame.draw.line(ecra, (255,0,0), (largura,0), (largura,altura), 30)

    # Movimento dos carros
    if y >= altura:
        y = 0
    y = y + 2.5
    if y2 >= altura:
        y2 = 0
    y2 = y2 + 3
    if y3 >= altura:
        y3 = 0
    y3 = y3 + 5
    if y4 >= altura:
        y4 = 0
    y4 = y4 + 4
    if y5 >= altura:
        y5 = 0
    y5 = y5 + 3.5

    # Colisões
    if player.colliderect(carro_vermelho) or \
       player.colliderect(carro_verde) or \
       player.colliderect(carro_azul) or \
       player.colliderect(carro_azulescuro) or \
       player.colliderect(carro_branco):
        coisa = False
        perdeste()

    if player.colliderect(End):
        coisa = False
        Ganhaste()

    pygame.display.update()
    relogio.tick(85)

time.sleep(4)
print('Fim')