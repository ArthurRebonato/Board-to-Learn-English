import pygame, time, random, sys

nome = input("Digite seu nome: ")
while True:
    email = input("Digite seu email: ")
    if email.count("@") > 0 and email.count(".") > 0:
        break
    else:
        print("email invalido")

arquivo = open("HistoricoUsuarios.txt","a")
arquivo.write("Nome: ")
arquivo.write(nome)
arquivo.write("     ")
arquivo.write("Email: ")
arquivo.write(email)
arquivo.write("\n")
arquivo.close()

from geral import cria_botao, creditos, regras, sair, menu_jogo, text_objects, mostrapino, message_display
from geral import analise_resultado, ganhou, perdeu, movimentoPinoAzul, movimentoPinoVermelho, aleatoria

pygame.init()

gamedisplay = pygame.display.set_mode( (800, 600))
clock = pygame.time.Clock()
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (100, 100, 100)
VERMELHO = (120, 0, 0)
VERDE_ESCURO = (0, 120, 0)
VERDE_CLARO = (0, 255, 0)
VERMELHO_CLARO = (255, 0, 0)
AZUL = (0, 0, 255)
pygame.display.set_caption('Board to learn English')
pygame.font.init()
base_font = pygame.font.Font(None, 32)
input_rect = pygame.Rect(250,95,140,32)
pinoAzul = pygame.image.load('assets/Pino Azul Certo.png')
pinoVermelho = pygame.image.load('assets/Pino Vermelho Certo.png')
fundo = pygame.image.load('assets/Fundo com Tabuleiro Certo.png')