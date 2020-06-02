import pygame
from random import randint

from jogopython import constants
from jogopython.zombie import Zombie

pygame.init()

# variaveis do personagem                              ## x é a largura da tela
x_personagem = 1000                                     ## y é a altura da tela
y_personagem = 200
largPersonagem = 5
altPersonagem = 20
esquerda = False
direita = False
costas = False
frente = False
andar = 0

x_esposa = 120
y_esposa = 200



zombie = Zombie(570, 300, 9, pygame.image.load("images/zombie1_costa1.png"))
zombie2 = Zombie(300, 380, 6, pygame.image.load("images/zombie2_costa1.png"))
zombie3 = Zombie(300, 495, 6, pygame.image.load("images/zombie3_costa1.png"))
zombie4 = Zombie(570, 495, 9, pygame.image.load("images/zombie4_costa1.png"))
zombie5 = Zombie(500, 600, randint(5, 10), pygame.image.load("images/zombie5_costa1.png"))
zombie6 = Zombie(430, 700, randint(3, 7), pygame.image.load("images/zombie6_costa.png"))
zombie7 = Zombie(470, 700, randint(5, 10), pygame.image.load("images/zombie7_costa.png"))
zombie1_frente = Zombie(290, -8, -9, pygame.image.load("images/zombie3_frente1.png"))
zombie2_frente = Zombie(255, -15, -8, pygame.image.load("images/zombie2_frente1.png"))

personagem = pygame.image.load("images/jhon_frente1.png")                # imagens da  movimentção personagem
personagem_direita = [pygame.image.load("images/jhon_Direita1.png"),
                      pygame.image.load("images/jhon_Direita2.png"),
                      pygame.image.load("images/jhon_Direita3.png"), ]


personagem_esquerda = [pygame.image.load("images/jhon_Esquerda1.png"),
                       pygame.image.load("images/jhon_Esquerda2.png"),
                       pygame.image.load("images/jhon_Esquerda3.png"), ]

personagem_frente = [pygame.image.load("images/jhon_frente1.png"),
                     pygame.image.load("images/jhon_frente2.png"),
                     pygame.image.load("images/john_frente3.png"), ]

personagem_costa = [pygame.image.load("images/jhon_Costa1.png"),
                    pygame.image.load("images/jhon_Costa2.png"),
                    pygame.image.load("images/jhon_Costa3.png"), ]

esposa = pygame.image.load("images/Esposa.png")




        #loop da musica do Jogo


inicio = pygame.image.load("images/inicioo.jpg")
fundo = inicio
historia1 = pygame.image.load("images/fumaça_1.jpg")
historia2 = pygame.image.load("images/fumaça_2.jpg")
fundo1 = pygame.image.load('images/Cenario1.jpg')
fundo2 = pygame.image.load('images/Fundo2.jpg')
fundo3 = pygame.image.load("images/Fundo3.jpg")
fundo4 = pygame.image.load("images/Fundo4.jpg")
fundoFinal = pygame.image.load("images/Final.png")
gameover = pygame.image.load("images/GameOver.jpg")
vida_personagem = 4
font = pygame.font.SysFont("arial black",18)
texto = font.render("VIDA: "+ str(vida_personagem), True, (255, 255, 255), (77, 121, 255))
pos_texto = texto.get_rect()
pos_texto.center = (50,18,)


def desenhos():                              # # codigo da movimnetação do personagem
    global andar

    janela.blit(fundo, (0, 0))
    if andar + 1 >= 25:
        andar = 0
    if frente:
        janela.blit(personagem_esquerda[andar // 10], (x_personagem, y_personagem))
        andar += 1
    elif costa:
        janela.blit(personagem_direita[andar // 10], (x_personagem, y_personagem))
        andar += 1
    elif direita:
        janela.blit(personagem_frente[andar // 10], (x_personagem, y_personagem))
        andar += 1
    elif esquerda:
        janela.blit(personagem_costa[andar // 10], (x_personagem, y_personagem))
        andar += 1
    else:
        janela.blit(personagem, (x_personagem, y_personagem))
        andar = 0


janela = pygame.display.set_mode((constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL))   # temanho da janela
pygame.display.set_caption("JOGO PYTHON")
janela.blit(personagem, (x_personagem, y_personagem))     # exibir personagem na tela


janela_aberta = True
pygame.display.update()

                                 # laço para manter a janela aberta
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()             # Comando para o controle do persongem
    if comandos[pygame.K_UP]:
        y_personagem -= constants.VELOCIDADE_PERSONAGEM
        esquerda = True
        direita = False
        costa = False
        frente = False
    elif comandos[pygame.K_DOWN]:
        y_personagem += constants.VELOCIDADE_PERSONAGEM
        direita = True
        esquerda = False
        costa = False
        frente = False
    elif comandos[pygame.K_RIGHT]:
        x_personagem += constants.VELOCIDADE_PERSONAGEM
        direita = False
        esquerda = False
        frente = False
        costa = True
    elif comandos[pygame.K_LEFT]:
        x_personagem -= constants.VELOCIDADE_PERSONAGEM
        direita = False
        esquerda = False
        frente = True
        costa = False
    else:
        esquerda = False
        direita = False
        frente = False
        costa = False
        walkcount = 0


    pygame.display.update()
    desenhos()

    #mudar imagem inicia para historia

    if fundo == inicio and comandos[pygame.K_RIGHT]:     #tela inicio aporetar e mudar tela
        fundo = historia1
        x_personagem = 20000
        pygame.display.update()

    elif fundo == historia1 and comandos[pygame.K_UP]:      #segunda tela das historias
        fundo = historia2
        x_personagem = 10000
        pygame.display.update()

    elif fundo == historia2 and comandos[pygame.K_RIGHT]:    #terçeira tela das historias

        fundo = fundo1
        x_personagem = 115
        y_personagem = 170
        pygame.display.update()

        #mudança de telas

        pygame.mixer.init()
        pygame.mixer.music.load("musics/Call of Duty 4 Modern Warfare OST - All In.mp3")
        pygame.mixer.music.play(-1)

        # troca de tela

    if fundo == fundo1:
        janela.blit(texto, pos_texto)
        if x_personagem < 22:               # colisão tela 1
           x_personagem = 23
        if y_personagem < 122:
            y_personagem = 123
        if y_personagem > 180:
            y_personagem = 181
        if x_personagem > 772:           #troca fundo1 p/fundo2
            fundo = fundo2
            x_personagem = 90        #localização_personagem tela2
            y_personagem = 192


    if fundo == fundo2:
        janela.blit(texto, pos_texto)
        if x_personagem < 3:          #para voltar a tela anterior
            x_personagem = 4
        if y_personagem < 193:               # colisão tela 2
            y_personagem = 194
        if y_personagem > 204:
            y_personagem = 205
        if x_personagem > 750:           #troca fundo2 p/ fundo3
            fundo = fundo3
            x_personagem = 10

    if fundo == fundo3:
        janela.blit(texto, pos_texto)
        if x_personagem < 4:             # if para voltar a tela anterior
            fundo = fundo2

        if y_personagem < 118:          # if colisão tela 3
            y_personagem = 119

        if y_personagem > 200 and not (410 < x_personagem < 500):
            y_personagem = 198

        if y_personagem > 500 and (410 < x_personagem < 500):               #troca fundo3 p/ fundo4
            fundo = fundo4
            x_personagem = 300
            y_personagem = 108

    if fundo == fundo2:                 # if para zombies tela 2
        zombie.andarVertical(janela, -2)
        zombie2.andarVertical(janela, -2)
        zombie3.andarVertical(janela, -2)
        zombie4.andarVertical(janela, -2)
        if y_personagem in range(zombie.vertical - 20, zombie.vertical) and \
                x_personagem in range(zombie.horizontal - 15, zombie.horizontal + 15):
                vida_personagem -= 1
                texto = font.render("VIDA: " + str(vida_personagem), True, (255, 255, 255), (77, 121, 255))

                if vida_personagem == 0:
                 y_personagem = 1000
                 fundo = gameover
        if y_personagem in range(zombie2.vertical - 15, zombie2.vertical) and \
                x_personagem in range(zombie2.horizontal - 15, zombie2.horizontal + 15):
               vida_personagem -= 1
               texto = font.render("VIDA: " + str(vida_personagem), True, (255, 255, 255), (77, 121, 255))
               if vida_personagem == 0:
                y_personagem = 1000
                fundo = gameover

        if y_personagem in range(zombie3.vertical - 15, zombie3.vertical) and \
                x_personagem in range(zombie3.horizontal - 15, zombie3.horizontal + 15):
            vida_personagem -= 1
            texto = font.render("VIDA: " + str(vida_personagem), True, (255, 255, 255), (77, 121, 255))
            if vida_personagem == 0:
                y_personagem = 1000
                fundo = gameover

        if y_personagem in range(zombie4.vertical - 15, zombie4.vertical) and \
                x_personagem in range(zombie4.horizontal - 15, zombie4.horizontal + 15):
            vida_personagem -= 1
            texto = font.render("VIDA: " + str(vida_personagem), True, (255, 255, 255), (77, 121, 255))
            if vida_personagem == 0:
                y_personagem = 1000
                fundo = gameover

    if fundo == fundo3:                   #if dos zombies tela 3
        zombie5.andarVertical(janela, 150)
        zombie6.andarVertical(janela, 150)
        zombie7.andarVertical(janela, 150)
        zombie1_frente.andarVerticalContratio(janela, 200, -8)
        zombie2_frente.andarVerticalContratio(janela, 200, -15)

    if y_personagem in range(zombie1_frente.vertical - 15, zombie1_frente.vertical) and \
            x_personagem in range(zombie1_frente.horizontal - 15, zombie1_frente.horizontal + 15):
        vida_personagem -= 1
        texto = font.render("VIDA: " + str(vida_personagem), True, (255, 255, 255), (77, 121, 255))
        if vida_personagem == 0:
            y_personagem = 1000
            fundo = gameover

    if y_personagem in range(zombie2_frente.vertical - 15, zombie2_frente.vertical) and \
            x_personagem in range(zombie2_frente.horizontal - 15, zombie2_frente.horizontal + 15):
        vida_personagem -= 1
        texto = font.render("VIDA: " + str(vida_personagem), True, (255, 255, 255), (77, 121, 255))
        if vida_personagem == 0:
            y_personagem = 1000
            fundo = gameover

    if y_personagem in range(zombie5.vertical - 15, zombie5.vertical) and \
            x_personagem in range(zombie5.horizontal - 15, zombie5.horizontal + 15):
        vida_personagem -= 1
        texto = font.render("VIDA: " + str(vida_personagem), True, (255, 255, 255), (77, 121, 255))
        if vida_personagem == 0:
            y_personagem = 1000
            fundo = gameover

    if y_personagem in range(zombie6.vertical - 15, zombie6.vertical) and \
            x_personagem in range(zombie6.horizontal - 15, zombie6.horizontal + 15):
        vida_personagem -= 1
        texto = font.render("VIDA: " + str(vida_personagem), True, (255, 255, 255), (77, 121, 255))
        if vida_personagem == 0:
            y_personagem = 1000
            fundo = gameover

    if y_personagem in range(zombie7.vertical - 15, zombie7.vertical) and \
            x_personagem in range(zombie7.horizontal - 15, zombie7.horizontal + 15):
        vida_personagem -= 1
        texto = font.render("VIDA: " + str(vida_personagem), True, (255, 255, 255), (77, 121, 255))
        if vida_personagem == 0:
            y_personagem = 1000
            fundo = gameover

    if fundo == fundo4:
        if x_personagem < 255:
            x_personagem = 256
        x_esposa = 420
        y_esposa = 110
        if y_personagem < 55:
            y_personagem = 57        ##colisôes ultima tela
        if y_personagem > 420:
            y_personagem = 422

        if y_personagem > 100 and (200 < x_personagem > 300):
            y_personagem = 99


        if x_personagem > 380:
            fundo = fundoFinal
            y_personagem = 1000
        janela.blit(esposa, (x_esposa, y_esposa))
        pygame.display.update()


    if fundo == fundo3:
       if x_personagem > 710:
          x_personagem = 708


     #colisão

pygame.quit()
janela.blit()




