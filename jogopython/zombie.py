from constants import TAMANHO_VERTICAL
import random
import pygame
import constants



def carregar_zombies_fundo2():
    return [
        Zombie(570, 300, constants.ZOMBIE1_FUNDO2_VELOCIDADE, pygame.image.load("img/zombie/zombie1_costa1.png")),
        Zombie(300, 380, constants.ZOMBIE2_FUNDO2_VELOCIDADE, pygame.image.load("img/zombie/zombie2_costa1.png")),
        Zombie(300, 495, constants.ZOMBIE3_FUNDO2_VELOCIDADE, pygame.image.load("img/zombie/zombie3_costa1.png")),
        Zombie(570, 495, constants.ZOMBIE4_FUNDO2_VELOCIDADE, pygame.image.load("img/zombie/zombie4_costa1.png")),
    ]
def desenhar_zombies_fundo2(janela, zombies):
    for zombie in zombies:
        zombie.andarVertical(janela, -2, constants.TAMANHO_VERTICAL)

def carregar_zombies_fundo3():
    return [
        Zombie(510, 500, random.randint(*constants.ZOMBIE5_FUNDO3_VELOCIDADE), pygame.image.load("img/zombie/zombie5_costa1.png")),
        Zombie(425, 800, random.randint(*constants.ZOMBIE6_FUNDO3_VELOCIDADE), pygame.image.load("img/zombie/zombie6_costa.png")),
        #Zombie(470, 800, random.randint(*constants.ZOMBIE7_FUNDO3_VELOCIDADE), pygame.image.load("img/zombie/zombie7_costa.png")),
        Zombie(290, -8, constants.ZOMBIE1_FRENTE_FUNDO3_VELOCIDADE, pygame.image.load("img/zombie/zombie3_frente1.png")),   # Contrário
        Zombie(255, -15, constants.ZOMBIE2_FRENTE_FUNDO3_VELOCIDADE, pygame.image.load("img/zombie/zombie2_frente1.png"))   # Contrário
    ]

def desenhar_zombies_fundo3(janela, zombies):
    for i, zombie in enumerate(zombies):
        if i < 2:  # Os 3 primeiros vão com andarVertical
            zombie.andarVertical(janela, 150)
        else:      # Os 2 últimos vão com andarVerticalContrario
            zombie.andarVerticalContrario(janela, 200, -20)


class Zombie:
    def __init__(self, horizontal, vertical, velocidade, imagem):
        self.horizontal = horizontal
        self.vertical = vertical
        self.velocidade = velocidade
        self.imagem = imagem
        self.largura = 20
        self.altura = 54
        self.direcao = 1  #1 = direita, -1= esquereda

    def mover(self):
        self.horizontal += self.velocidade * self.direcao
        # Faz o zumbi ir de um lado pro outro e inverter nas bordas
        if self.horizontal < 0 or self.horizontal > 750:
            self.direcao *= -1

    def desenhar(self, janela):
        janela.blit(self.imagem, (self.horizontal, self.vertical))
   

    def andarVertical(self, janela, limit=None, inicio=constants.TAMANHO_VERTICAL):
        if limit is None:
            limit = -self.imagem.get_height()
        if self.vertical > limit:
            self.vertical -= self.velocidade
        else:
            self.vertical = inicio
        janela.blit(self.imagem, (self.horizontal, self.vertical))


    def andarVerticalContrario(self, janela, limit, inicio=TAMANHO_VERTICAL):
        if self.vertical <= limit:
            self.vertical -= self.velocidade
        else:
            self.vertical = inicio
        janela.blit(self.imagem, (self.horizontal, self.vertical))

