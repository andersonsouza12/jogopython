import pygame

pygame.init()
# variaveis do personagem                            ## x é a largura da tela
x_personagem = 1000                                     ## y é a altura da tela
y_personagem = 200
velocidade_personagem = 10
esquerda = False
direita = False
costas = False
frente = False
andar = 0
                                  #posições do zombie3
x_zombie3 = 1000
y_zombie3 = 200
velocidade_zombie3 = 10
andar_zombie3 = 0



                                             # imagens da  movimentção personagem

personagem = pygame.image.load("jhon_frente1.png")
personagem_direita = [pygame.image.load("jhon_Direita1.png"),
                      pygame.image.load("jhon_Direita2.png"),
                      pygame.image.load("jhon_Direita3.png"), ]


personagem_esquerda = [pygame.image.load("jhon_Esquerda1.png"),
                       pygame.image.load("jhon_Esquerda2.png"),
                       pygame.image.load("jhon_Esquerda3.png"), ]

personagem_frente = [pygame.image.load("jhon_frente1.png"),
                     pygame.image.load("jhon_frente2.png"),
                     pygame.image.load("john_frente3.png"), ]

personagem_costa = [pygame.image.load("jhon_Costa1.png"),
                    pygame.image.load("jhon_Costa2.png"),
                    pygame.image.load("jhon_Costa3.png"), ]

                                 # imagem da movimentação do zombie3
zombie3 = [pygame.image.load("zombie3_costa1.png"),
           pygame.image.load("zombie3_costa2.png"),
           pygame.image.load("zombie3_costa3.png"), ]







inicio = pygame.image.load("inicioo.jpg")
fundo = inicio
historia1 = pygame.image.load("fumaça_1.jpg")
historia2 = pygame.image.load("fumaça_2.jpg")
fundo1 = pygame.image.load('Cenario1.jpg')
fundo2 = pygame.image.load('Fundo2.jpg')
fundo3 = pygame.image.load("Fundo3.jpg")
fundo4 = pygame.image.load("Fundo4.jpg")



def desenhos():                              # # codigo da movimnetação do personagem
    global andar

    janela.blit(fundo, (0, 0))
    if andar + 1 >= 25:
        andar = 0
    if esquerda:
        janela.blit(personagem_esquerda[andar // 3], (x_personagem, y_personagem))
        andar += 1
    elif direita:
        janela.blit(personagem_direita[andar // 3], (x_personagem, y_personagem))
        andar += 1
    elif frente:
        janela.blit(personagem_frente[andar // 3], (x_personagem, y_personagem))
        andar += 1
    elif costa:
        janela.blit(personagem_costa[andar // 3], (x_personagem, y_personagem))
        andar += 1
    else:
        janela.blit(personagem, (x_personagem, y_personagem))
        andar = 0




janela = pygame.display.set_mode((772, 500))                    # temanho da janela
pygame.display.set_caption("JOGO PYTHON")
janela.blit(personagem, (x_personagem, y_personagem))      # exibir personagem na tela

pygame.display.update()




janela_aberta = True                                    # laço para manter a janela aberta


while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()             # Comando para o controle do persongem
    if comandos[pygame.K_UP]:
        y_personagem -= velocidade_personagem
        esquerda = True
        direita = False
        costa = False
        frente = False
    elif comandos[pygame.K_DOWN]:
        y_personagem += velocidade_personagem
        direita = True
        esquerda = False
        costa = False
        frente = False
    elif comandos[pygame.K_RIGHT]:
        x_personagem += velocidade_personagem
        direita = False
        esquerda = False
        frente = False
        costa = True
    elif comandos[pygame.K_LEFT]:
        x_personagem -= velocidade_personagem
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

    elif fundo == historia1 and comandos[pygame.K_RIGHT]:      #segunda tela das historias
        fundo = historia2
        x_personagem = 10000
        pygame.display.update()

    elif fundo == historia2 and comandos[pygame.K_RIGHT]:    #terçeira tela das historias

        fundo = fundo1
        x_personagem = 115
        y_personagem = 170
        pygame.display.update()

        #mudança de telas


                                             # troca de tela
    if fundo == fundo1:
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

        if x_personagem > 772:
            x_zombie3 = 120
            y_zombie3 = 100


    if fundo == fundo2:
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
        if x_personagem < 4:             # if para voltar a tela anterior
            fundo = fundo2
        if y_personagem < 118:          # if colisão tela 3
            y_personagem = 119



        if y_personagem > 500:               #troca fundo3 p/ fundo4
            fundo = fundo4
            x_personagem = 300
            y_personagem = 108


        pygame.display.update()





pygame.quit()
janela.blit()




