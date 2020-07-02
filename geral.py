import pygame, time, random, sys

pygame.init()

LARGURA = 800
ALTURA = 600
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (100, 100, 100)
VERMELHO = (120, 0, 0)
VERDE_ESCURO = (0, 120, 0)
VERDE_CLARO = (0, 255, 0)
VERMELHO_CLARO = (255, 0, 0)
AZUL = (0, 0, 255)

gamedisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Board to Learn English')
pygame.font.init()
clock = pygame.time.Clock()