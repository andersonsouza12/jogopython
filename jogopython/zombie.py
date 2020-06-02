from jogopython.constants import TAMANHO_VERTICAL


class Zombie:
    horizontal = 0
    vertical = 0
    velocidade = 0
    imagem = ''
    largura = 20
    largura2 = 20
    altura = 54

    def __init__(self, horizontal, vertical, velocidade, imagem):
        self.horizontal = horizontal
        self.vertical = vertical
        self.velocidade = velocidade
        self.imagem = imagem

    def andarVertical(self, janela, limit, inicio =TAMANHO_VERTICAL):
        if(self.vertical >= limit):
            self.vertical -= self.velocidade
        else:
            self.vertical = inicio
        janela.blit(self.imagem, (self.horizontal, self.vertical))

    def andarVerticalContratio(self, janela, limit, inicio =TAMANHO_VERTICAL):
        if(self.vertical <= limit):
            self.vertical -= self.velocidade
        else:
            self.vertical = inicio
        janela.blit(self.imagem, (self.horizontal, self.vertical))




