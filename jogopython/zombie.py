from constants import TAMANHO_VERTICAL
import random
import pygame



def carregar_zombies_fundo2():
    return [
        Zombie(570, 300, 9, pygame.image.load("img/zombie/zombie1_costa1.png")),
        Zombie(300, 380, 6, pygame.image.load("img/zombie/zombie2_costa1.png")),
        Zombie(300, 495, 6, pygame.image.load("img/zombie/zombie3_costa1.png")),
        Zombie(570, 495, 9, pygame.image.load("img/zombie/zombie4_costa1.png")),
        Zombie(500, 600, random.randint(5, 10), pygame.image.load("img/zombie/zombie5_costa1.png")),
        Zombie(430, 700, random.randint(3, 7), pygame.image.load("img/zombie/zombie6_costa.png")),
        Zombie(470, 700, random.randint(5, 10), pygame.image.load("img/zombie/zombie7_costa.png")),
    ]





class Zombie:
    def __init__(self, horizontal, vertical, velocidade, imagem):
        self.horizontal = horizontal
        self.vertical = vertical
        self.velocidade = velocidade
        self.imagem = imagem
        self.largura = 20
        self.altura = 54

    def andarVertical(self, janela, limit, inicio=TAMANHO_VERTICAL):
        if self.vertical >= limit:
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
