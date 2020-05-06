import pygame
pygame.init ()
     # variaveis do personagem
x_personagem = 120
y_personagem = 200
velocidade_personagem = 10
esquerda = False
direita = False
costas = False
frente = False
andar = 0
fundo = pygame.image.load('cidade1.png')  # adicionei o fundo

personagem = pygame.image.load('lara.central.1.png')
personagem_direita = [pygame.image.load("lara_direita1.png"),   # teste para movimentação do personagem não esta dadando certo
                      pygame.image.load("lara_direita.2.png"),
                      pygame.image.load("lara_direita.3.png"),
                      pygame.image.load("lara_direita.4.png"),
                      pygame.image.load("lara_direita.5.png"),
                      pygame.image.load("lara_direita.6.png"),
                      pygame.image.load("lara_direita.7.png"),
                      pygame.image.load("lara.central.2.png"),]

personagem_esquerda = [pygame.image.load("lara.cento.esquerda.png"),
                       pygame.image.load("lara.esquerda.1.png"),
                       pygame.image.load("lara.esquerda.2.png"),
                       pygame.image.load("lara.esquerda.3.png"),
                       pygame.image.load("lara.esquerda.4.png"),
                       pygame.image.load("lara.esquerda.5.png"),
                       pygame.image.load("lara.esquerda.6.png"),
                       pygame.image.load("lara.esquerda.7.png"),
                       pygame.image.load("lara.esquerda.8.png"),]

personagem_frente = [pygame.image.load("lara.frente.1.png"),
                     pygame.image.load("lara.frente.2.png"),
                     pygame.image.load("lara.frente.3.png"),
                     pygame.image.load("lara.frente.4.png"),
                     pygame.image.load("lara.frente.5.png"),
                     pygame.image.load("lara.frente.6.png"),
                     pygame.image.load("lara.frente.7.png"),
                     pygame.image.load("lara.frente.8.png"),
                     pygame.image.load("lara.frente.9.png"),]

personagem_costa = [pygame.image.load("lara.costa.1.png"),
                    pygame.image.load("lara.costa.2.png"),
                    pygame.image.load("lara.costa.3.png"),
                    pygame.image.load("lara.costa.4.png"),
                    pygame.image.load("lara.costa.5.png"),
                    pygame.image.load("lara.costa.6.png"),
                    pygame.image.load("lara.costa.7.png"),
                    pygame.image.load("lara.costa.8.png"),
                    pygame.image.load("lara.costa.9.png"),]

def desenhos():
    global andar

    janela.blit(fundo,(0,0))        # codigo da movimnetação do personagem
    if andar + 1 >= 25:
        andar = 0
    if esquerda:
        janela.blit(personagem_esquerda[andar // 3],  (x_personagem, y_personagem))
        andar += 1
    elif direita:
        janela.blit(personagem_direita[andar // 3], (x_personagem, y_personagem))
    elif costas:
        janela.blit(personagem_costa[andar // 3], (x_personagem, y_personagem))
        andar += 1
    elif frente:
        janela.blit(personagem_frente[andar // 3], (x_personagem, y_personagem))
        andar += 1
    else:
        janela.blit(personagem, (x_personagem, y_personagem))
        andar = 0



janela = pygame.display.set_mode((800,500))        # temanho da janela
pygame.display.set_caption("JOGO PYTHON")

janela_aberta = True     # laço para manter a janela aberta
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()    # Comando para o controle do persongem
    if comandos[pygame.K_a]:
        y_personagem -= velocidade_personagem
        esquerda = True
        direita = False
        costa = False
        frente = False
    elif comandos[pygame.K_w]:
        y_personagem += velocidade_personagem
        direita = True
        esquerda = False
        costa = False
        frente = False
    elif comandos[pygame.K_d]:
        x_personagem += velocidade_personagem
        direita = False
        esquerda = False
        frente = False
        costa = True
    elif comandos[pygame.K_x]:
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
    desenhos()

janela.blit()

janela.blit(personagem,(x_personagem,y_personagem)) # exibir personagem na tela
pygame.display.update()

pygame.quit()



