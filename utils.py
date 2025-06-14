import pygame
from random import randint
import constants
from jogopython.zombie import Zombie


def desenhar_texto_digitando(tela, texto_completo, fonte, cor, pos, largura_max, texto_parcial):
    palavras = texto_completo.split(' ')
    linhas = []
    linha_atual = ""
    for palavra in palavras:
        teste_linha = linha_atual + palavra + " "
        if fonte.size(teste_linha)[0] < largura_max:
            linha_atual = teste_linha
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "
    linhas.append(linha_atual)

    # Renderizar até onde o texto foi digitado
    texto_junto = ''.join(texto_parcial)
    char_index = 0
    y_offset = 0
    for linha in linhas:
        render_linha = ""
        while char_index < len(texto_junto) and len(render_linha) < len(linha):
            render_linha += texto_junto[char_index]
            char_index += 1
        renderizada = fonte.render(render_linha, True, cor)
        tela.blit(renderizada, (pos[0], pos[1] + y_offset))
        y_offset += fonte.get_height()



def desenhar_tela_inicial(tela):
    fonte = pygame.font.SysFont("Arial", 30)
    texto = fonte.render("Pressione Enter para Iniciar", True, (255, 255, 255))
    tela.blit(texto, (250, 250))

def desenhar_interface(tela, vida):
    fonte = pygame.font.SysFont("Arial", 24)
    texto_vida = fonte.render(f"Vida: {vida}", True, (255, 255, 255))
    tela.blit(texto_vida, (10, 10))

def carregar_imagem(caminho):
    return pygame.image.load(caminho)

def carregar_lista_imagens(lista_caminhos):
    return [pygame.image.load(caminho) for caminho in lista_caminhos]

def carregar_imagens_personagem():
    return {
        "direita": [
            pygame.image.load("img/man/man_direita1.png"),
            pygame.image.load("img/man/man_direita2.png"),
            pygame.image.load("img/man/man_direita3.png"),
        ],
        "esquerda": [
            pygame.image.load("img/man/man_esquerda1.png"),
            pygame.image.load("img/man/man_esquerda2.png"),
            pygame.image.load("img/man/man_esquerda3.png"),
        ],
        "frente": [
            pygame.image.load("img/man/man_frente1.png"),
            pygame.image.load("img/man/man_frente2.png"),
            pygame.image.load("img/man/man_frente3.png"),
        ],
        "costa": [
            pygame.image.load("img/man/man_costa1.png"),
            pygame.image.load("img/man/man_costa2.png"),
            pygame.image.load("img/man/man_costa3.png"),
        ],
    }

def carregar_telas():
    
    return {
        "logo": pygame.transform.scale(pygame.image.load("img/logo/logo.jpg"), (constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL)),
        "fundoHitory": pygame.transform.scale(pygame.image.load("img/fundoHitory.png"), (constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL)),
        "fundo1": pygame.transform.scale(pygame.image.load("img/cenario/Cenario1.jpg"), (constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL)),
        "fundo2": pygame.transform.scale(pygame.image.load("img/cenario/Fundo2.jpg"),(constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL)),
        "fundo3": pygame.transform.scale(pygame.image.load("img/cenario/Fundo3.jpg"),(constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL)),
        "fundo4": pygame.transform.scale(pygame.image.load("img/cenario/Fundo4.jpg"),(constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL)),
        "final": pygame.transform.scale(pygame.image.load("img/logo/logo.jpg"),(constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL)),
        "gameover": pygame.transform.scale(pygame.image.load("img/Game_Over.jpg"),(constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL)),    
    }

def desenhar_personagem(janela, personagens, x, y, direcao, contador):
    if contador + 1 >= 25:
        contador = 0
    janela.blit(personagens[direcao][contador // 10], (x, y))
    contador += 1
    return contador


def carregar_imagem_esposa():
    return pygame.image.load("img/wife/esposa.png")



def atualizar_texto_vida(font, vida_personagem):
    return font.render(f"VIDA: {vida_personagem}", True, (255, 255, 255), (77, 121, 255))


def verificar_colisao_personagem_zombie(x_personagem, y_personagem, zombies, vida_personagem):
    for zombie in zombies:
        if y_personagem in range(zombie.vertical - 20, zombie.vertical) and \
           x_personagem in range(zombie.horizontal - 15, zombie.horizontal + 15):
            vida_personagem -= 1
            if vida_personagem == 0:
                return True, vida_personagem
    return False, vida_personagem


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


def verificar_colisoes_tela(fundo_atual, x_personagem, y_personagem):
    if fundo_atual == "fundo1":
        if x_personagem< 22:
            x_personagem = 23
        if y_personagem < 122:
            y_personagem = 123
        if y_personagem > 180:
            y_personagem = 181
        if x_personagem > 772:
            # Troca para fundo2 localização do personagem na tela
            return "fundo2", 90, 192

    elif fundo_atual == "fundo2":
        if x_personagem < 3:       
            x_personagem = 4
        if y_personagem < 193:               # colisão tela 2
            y_personagem = 194
        if y_personagem > 204:
            y_personagem = 205
        if x_personagem > 750:
            # Volta para fundo1
            return "fundo3", 0, 10

    elif fundo_atual == "fundo3":
        if x_personagem < 0:
            # Volta para fundo2
            return "fundo2", 750, 190
        if y_personagem < 118:                    # if colisão tela 3
            y_personagem = 119

        if x_personagem > 718:         #colisão tela 3 lado direito
            x_personagem = 717

        if y_personagem > 200 and not (410 < x_personagem < 500):
            y_personagem = 198

        if y_personagem > 500 and (410 < x_personagem < 500):        
            return "fundo4", 300,108

    elif fundo_atual == "fundo4":
        
        if y_personagem < 100:   # colisão top da tela
            y_personagem = 105

        if y_personagem > 430:   # Em baixo 
            y_personagem = 429

        if x_personagem < 220:    # lado esquerdo
            x_personagem = 221

        if x_personagem > 718:    # Dirteito
            x_personagem= 717


    return fundo_atual, x_personagem, y_personagem
