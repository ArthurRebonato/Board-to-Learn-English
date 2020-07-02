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

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def cria_botao(msg, sqr, cor1, cor2, cor_texto, acao=None):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    if sqr[0] + sqr[2] > mouse[0] > sqr[0] and sqr[1] + sqr[3] > mouse[1] > sqr[1]:
        pygame.draw.rect(gamedisplay, cor2, sqr)
        if clique[0] == 1 and acao != None:
            acao()
    else:
        pygame.draw.rect(gamedisplay, cor1, sqr)
        
    fontePequena = pygame.font.SysFont('comicsansms', 20)
    surface_texto, rect_texto = text_objects(msg, fontePequena, cor_texto)
    rect_texto.center = (sqr[0] + 60, sqr[1] + 20)
    gamedisplay.blit(surface_texto, rect_texto)

def creditos():
    sair = False
    while not sair:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                sair = True
        
        gamedisplay.fill(PRETO)
        fonte = pygame.font.SysFont('comicsansms', 20)
        surface_texto, rect_texto = text_objects("Programador: Arthur Rebonato", fonte, BRANCO)
        rect_texto.center = (400, 200)
        gamedisplay.blit(surface_texto, rect_texto)

        surface_texto, rect_texto = text_objects("Disciplina: Fundamento de Programação", fonte, BRANCO)
        rect_texto.center = (400, 222)
        gamedisplay.blit(surface_texto, rect_texto)

        surface_texto, rect_texto = text_objects("Versao Python:3.8.2", fonte, BRANCO)
		rect_texto.center = (400, 400)
		gamedisplay.blit(surface_texto, rect_texto)

        surface_texto, rect_texto = text_objects("Versao Pygame: 1.9.6", fonte, BRANCO)
		rect_texto.center = (400, 461)
		gamedisplay.blit(surface_texto, rect_texto)

        voltar = fonte.render('Pressione qualquer tecla para voltar ao menu.', False, BRANCO)
		gamedisplay.blit(voltar, (25, 550))

		pygame.display.update()
		clock.tick(15)

def regras():
    sair = False
    while not sair:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair = True
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                sair = True
        
        gamedisplay.fill(PRETO)
        fonte = pygame.font.SysFont('comicsansms', 20)

        info1 = fonte.render('O jogo eh praticado em um tabuleiro de 19 casas.', False, (BRANCO))
		info2 = fonte.render('A peca anda pra frente quando acertar uma traducao.', False, (BRANCO))
		info3 = fonte.render('A peca anda uma casa de cada vez.', False, (BRANCO))
		info4 = fonte.render('O objetivo e chegar no final.', False, (BRANCO))
	
		voltar = fonte.render('Pressione qualquer tecla para voltar ao menu.', False, BRANCO)

		gamedisplay.blit(info1, (5, 65))
		gamedisplay.blit(info2, (5, 95))
		gamedisplay.blit(info3, (5, 115))
		gamedisplay.blit(info4, (5, 145))
		gamedisplay.blit(voltar, (25, 550))

		pygame.display.update()
		clock.tick(60)

def sair():
    pygame.quit()
    quit()

def menu_jogo(game_loop):
	while True:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()
				quit()

		gamedisplay.fill(PRETO)
		fonte = pygame.font.SysFont('comicsansms', 50)
		surface_texto, rect_texto = text_objects("Board to Learn English", fonte, BRANCO)
		rect_texto.center = (400, 200)
		gamedisplay.blit(surface_texto, rect_texto)

		cria_botao("INICIAR",(40, 300, 120, 40), VERDE_CLARO, VERDE_ESCURO, BRANCO, game_loop)
		cria_botao("MANUAL",(240, 300, 120, 40), BRANCO, CINZA, PRETO, regras)
		cria_botao("CREDITOS",(440, 300, 120, 40), BRANCO, CINZA, PRETO, creditos)
		cria_botao("SAIR",(640, 300, 120, 40), VERMELHO_CLARO, VERMELHO, BRANCO, sair)

		pygame.display.update()
		clock.tick(15)

def aleatoria(palavras_ingles):
    aleatoria_ingles = random.choice(palavras_ingles)
    return aleatoria_ingles

def mostrapino(pino,x,y):
    gamedisplay.blit(pino,(x,y))

def message_display(text, tamanho, posicaotextX, posicaotextY, cor):
    largeText = pygame.font.Font('freesansbold.ttf', tamanho)
    TextSurf, TextRect =  text_objects(text, largeText, cor)
    TextRect.center = ((posicaotextX, posicaotextY))
    gamedisplay.blit(TextSurf, TextRect)

def analise_resultado(text, tamanho, posicaotextX, posicaotextY, cor):
    largeText = pygame.font.Font('freesansbold.ttf', tamanho)
    TextSurf, TextRect =  text_objects(text, largeText, cor)
    TextRect.center = ((posicaotextX, posicaotextY))
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

def ganhou():
    message_display("Você venceu!", 115, 400, 300, BRANCO)
    pygame.display.update()

def perdeu():
    message_display("Você perdeu!", 115, 400, 300, BRANCO)
    pygame.display.update()

def movimentoPinoVermelho(p2_acertos, posicaoPinoVermelhoX, posicaoPinoVermelhoY):
    if p2_acertos == 1:
        posicaoPinoVermelhoX = posicaoPinoVermelhoX + 70
        return posicaoPinoVermelhoX, posicaoPinoVermelhoY
    elif p2_acertos > 1 and p2_acertos <= 4:
        posicaoPinoVermelhoX = posicaoPinoVermelhoX + 100
        return posicaoPinoVermelhoX, posicaoPinoVermelhoY
    elif p2_acertos == 5:
        posicaoPinoVermelhoX = posicaoPinoVermelhoX + 90
        return posicaoPinoVermelhoX, posicaoPinoVermelhoY
    elif p2_acertos == 6:
        posicaoPinoVermelhoY = posicaoPinoVermelhoY + 60
        return posicaoPinoVermelhoX, posicaoPinoVermelhoY
    elif p2_acertos == 7:
        posicaoPinoVermelhoY = posicaoPinoVermelhoY + 55
        return posicaoPinoVermelhoX, posicaoPinoVermelhoY
    elif p2_acertos == 8:
        posicaoPinoVermelhoY = posicaoPinoVermelhoY + 60
        return posicaoPinoVermelhoX, posicaoPinoVermelhoY
    elif p2_acertos > 8 and p2_acertos <= 12:
        posicaoPinoVermelhoX = posicaoPinoVermelhoX - 100
        return posicaoPinoVermelhoX, posicaoPinoVermelhoY
    elif p2_acertos > 12 and p2_acertos <= 15:
        posicaoPinoVermelhoY = posicaoPinoVermelhoY + 55
        return posicaoPinoVermelhoX, posicaoPinoVermelhoY
    elif p2_acertos > 15 and p2_acertos <= 18:
        posicaoPinoVermelhoX = posicaoPinoVermelhoX + 100
        return posicaoPinoVermelhoX, posicaoPinoVermelhoY
    elif p2_acertos == 19:
        posicaoPinoVermelhoX = posicaoPinoVermelhoX + 75
        return posicaoPinoVermelhoX, posicaoPinoVermelhoY
    elif p2_acertos == 20:
        posicaoPinoVermelhoX = posicaoPinoVermelhoX + 70
        return posicaoPinoVermelhoX, posicaoPinoVermelhoY
    
def movimentoPinoAzul(p1_acertos, posicaoPinoAzulX, posicaoPinoAzulY):
        if p1_acertos == 1:
            posicaoPinoAzulX = posicaoPinoAzulX + 70
            return posicaoPinoAzulX, posicaoPinoAzulY
        elif p1_acertos > 1 and p1_acertos <= 4:
            posicaoPinoAzulX = posicaoPinoAzulX + 100
            return posicaoPinoAzulX, posicaoPinoAzulY
        elif p1_acertos == 5:
            posicaoPinoAzulX = posicaoPinoAzulX + 70
            return posicaoPinoAzulX, posicaoPinoAzulY
        elif p1_acertos == 6:
            posicaoPinoAzulY = posicaoPinoAzulY + 60
            return posicaoPinoAzulX, posicaoPinoAzulY
        elif p1_acertos == 7:
            posicaoPinoAzulY = posicaoPinoAzulY + 55
            return posicaoPinoAzulX, posicaoPinoAzulY
        elif p1_acertos == 8:
            posicaoPinoAzulY = posicaoPinoAzulY + 60
            return posicaoPinoAzulX, posicaoPinoAzulY
        elif p1_acertos > 8 and p1_acertos <= 12:
            posicaoPinoAzulX = posicaoPinoAzulX - 100
            return posicaoPinoAzulX, posicaoPinoAzulY
        elif p1_acertos > 12 and p1_acertos <= 15:
            posicaoPinoAzulY = posicaoPinoAzulY + 55
            return posicaoPinoAzulX, posicaoPinoAzulY
        elif p1_acertos > 15 and p1_acertos <= 18:
            posicaoPinoAzulX = posicaoPinoAzulX + 100
            return posicaoPinoAzulX, posicaoPinoAzulY
        elif p1_acertos == 19:
            posicaoPinoAzulX = posicaoPinoAzulX + 93
            return posicaoPinoAzulX, posicaoPinoAzulY
        elif p1_acertos == 20:
            posicaoPinoAzulX = posicaoPinoAzulX + 95
            return posicaoPinoAzulX, posicaoPinoAzulY