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

palavras_ingles = ["backpack","book","compass","pencil case","calculator","dictionary","eraser","folder",
"lead","lunchbox","pen","pencil","ruler","paper","scissors","sharpener","brush","crayon","marker","paint",
"board","alarm clock","bed","blanket","bucket","cup","fork","knife","plate","refrigerator","spoon","clock",
"couch","curtains","fireplace","lamp","table","telephone","television","shower","garage","door","window",
"garden","stairs","balcony","porch","roof","doorbell","furniture","bookshelf","cushion","tablecloth",
"chair","glass","bowl","fridge","cabinet","stove","oven","sink","mattress","mirror","towels","bathtub",
"toilet paper","computer","printer","desk","trash can","broom","soap","mop"]

traducao_portugues = ["mochila","livro","compasso","estojo","calculadora","dicionario","borracha","pasta",
"grafite","lancheira","caneta","lapis","regua","papel","tesoura","apontador","pincel","giz de cera",
"canetinha","tinta","quadro","despertador","cama","cobertor","balde","copo","garfo","faca","prato",
"geladeira","colher","relogio","sofa","cortinas","lareira","lampada","mesa","telefone","televisao",
"chuveiro","garagem","porta","janela","jardim","escada","sacada","varanda","telhado","campainha","mobilia",
"estante de livros","almofada","toalha de mesa","cadeira","vidro","tigela","freezer","armario","fogao",
"forno","pia","colchao","espelho","toalhas","banheira","papel higienico","computador","impressora",
"escrivaninha","lixeira","vassoura","sabao","esfregao"]

def game_loop():
    posicaoPinoAzulX = 110 #X começa no 110
    posicaoPinoAzulY = 180 #Y começa no 180
    posicaoPinoVermelhoX = 135 #X começa no 135
    posicaoPinoVermelhoY = 165 #Y começa no 165
    p1_acertos = 0
    p2_acertos = 0
    ganhador = False
    perdedor = False
    user_text = ''
    palavra = aleatoria(palavras_ingles)
    while True:
        gamedisplay.fill(BRANCO)
        gamedisplay.blit(fundo, (0,0))

        pygame.draw.rect(gamedisplay,BRANCO,input_rect,2)
        text_surface = base_font.render(user_text, True,(0,0,0))
        gamedisplay.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100,text_surface.get_width() + 10)

        message_display("Board to Learn English", 60, 400, 35, PRETO)
        message_display("A palavra é:", 20, 100, 80, BRANCO)
        message_display(palavra, 20, 220, 80, BRANCO)
        message_display("Digite sua tradução:", 20, 140, 110, BRANCO)
        mostrapino(pinoAzul,posicaoPinoAzulX,posicaoPinoAzulY)
        mostrapino(pinoVermelho,posicaoPinoVermelhoX,posicaoPinoVermelhoY)

        if p2_acertos == 20:
            perdeu()
            time.sleep(5)
            perdedor = True
        elif p1_acertos == 20:
            ganhou()
            time.sleep(5)
            ganhador = True
        
        if perdedor == True:
            menu_jogo(game_loop)
        elif ganhador == True:
            menu_jogo(game_loop)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    posicao = palavras_ingles.index(palavra)
                    if user_text.lower() == traducao_portugues[posicao]:
                        analise_resultado("Resposta correta!", 30, 400, 150, BRANCO)
                        palavra = aleatoria(palavras_ingles)
                        user_text = ''
                        p1_acertos += 1
                        posicaoPinoAzulX, posicaoPinoAzulY = movimentoPinoAzul(p1_acertos, posicaoPinoAzulX, posicaoPinoAzulY)
                    elif user_text.lower() != traducao_portugues[posicao]:
                        analise_resultado("Resposta incorreta!", 30, 400, 150, BRANCO)
                        palavra = aleatoria(palavras_ingles)
                        user_text = ''
                        p2_acertos += 1
                        posicaoPinoVermelhoX, posicaoPinoVermelhoY = movimentoPinoVermelho(p2_acertos, posicaoPinoVermelhoX, posicaoPinoVermelhoY)
                else:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                
        pygame.display.update()
        clock.tick(60)

menu_jogo(game_loop)
pygame.quit()
quit()