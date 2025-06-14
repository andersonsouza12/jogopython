import pygame
import time
import random
import constants
import utils

from utils import (
    carregar_imagens_personagem,
    desenhar_personagem,
    carregar_telas,
    desenhar_interface,
    atualizar_texto_vida,
    verificar_colisao_personagem_zombie,
    verificar_colisoes_tela,
    carregar_imagem_esposa
)

from jogopython.zombie import Zombie, carregar_zombies_fundo2



pygame.init()

# Música de fundo
pygame.mixer.music.load("musics/Call of Duty 4 Modern Warfare OST - All In.mp3")
pygame.mixer.music.play(-1)

# Tela
janela = pygame.display.set_mode((constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL))
pygame.display.set_caption("Taking the Cure")

# Carregamento
telas = carregar_telas()
personagem_sprites = carregar_imagens_personagem()
zombies_fundo2 = carregar_zombies_fundo2()

# Estados iniciais

direcao = "frente"

fundo = telas["logo"]


font = pygame.font.SysFont("arial black", 18)
zombies_fundo2 = carregar_zombies_fundo2()

# Carregar e redimensionar logo
logo_original = pygame.image.load("img/logo/logo.png")
logo_redimensionada = pygame.transform.scale(logo_original, (constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL))
janela.blit(logo_redimensionada, (0, 0))
pygame.display.update()
time.sleep(3)



# ---------------------------
# FASE 2: Texto sendo digitado
# ---------------------------
fundo = telas["fundoHitory"]
texto_intro = constants.TEXTO_INTRO
fonte_intro = pygame.font.SysFont("arial", 28)
texto_parcial = []
indice_letra = 0
tempo_anterior = pygame.time.get_ticks()
image_esposa = carregar_imagem_esposa()

digitando = True
esperando_enter = False


while digitando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.KEYDOWN and esperando_enter:
            if evento.key == pygame.K_RETURN:
                digitando = False  # Sai do loop, mas NÃO fecha a janela aqui

    agora = pygame.time.get_ticks()
    if indice_letra < len(texto_intro) and agora - tempo_anterior > 30:
        texto_parcial.append(texto_intro[indice_letra])
        indice_letra += 1
        tempo_anterior = agora
    elif indice_letra == len(texto_intro):
        esperando_enter = True

    janela.blit(fundo, (0, 0))
    utils.desenhar_texto_digitando(
        janela,
        texto_intro,
        fonte_intro,
        (255, 255, 255),
        (40, 50),
        constants.TAMANHO_HORIZONTAL - 80,
        texto_parcial
    )
    if esperando_enter:
        aviso = pygame.font.SysFont("arial", 20).render("Pressione ENTER para continuar...", True, (255, 255, 255))
        janela.blit(aviso, (40, 460))
    pygame.display.update()

# Continuação do jogo depois do loop...
# Estados iniciais para a fase principal
x_personagem, y_personagem = 300, 200
vida_personagem = 4
direcao = "frente"
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial black", 32)

fundo_atual = "fundo1"  # por exemplo, antes do loop principal

contador = 0
movendo = False
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do personagem
    teclas = pygame.key.get_pressed()
    movendo = False
    if teclas[pygame.K_LEFT]:
        x_personagem -= constants.VELOCIDADE_PERSONAGEM
        direcao = "esquerda"
        movendo = True
    elif teclas[pygame.K_RIGHT]:
        x_personagem += constants.VELOCIDADE_PERSONAGEM
        direcao = "direita"
        movendo = True
    elif teclas[pygame.K_UP]:
        y_personagem -= constants.VELOCIDADE_PERSONAGEM
        direcao = "costa"
        movendo = True
    elif teclas[pygame.K_DOWN]:
        y_personagem += constants.VELOCIDADE_PERSONAGEM
        direcao = "frente"
        movendo = True


    # Verifica colisões com bordas da tela e troca de fundo
    fundo_atual, x_personagem, y_personagem = verificar_colisoes_tela(fundo_atual, x_personagem, y_personagem)
    # Redesenhar tudo
    janela.blit(telas[fundo_atual], (0, 0))
    # Se estiver no fundo4, desenha a esposa
    if fundo_atual == "fundo4":     #x   y
        janela.blit(image_esposa, (500,350))

     # Desenhar personagem com fundo e contador
    if movendo:
        contador = desenhar_personagem(janela, personagem_sprites, x_personagem, y_personagem, direcao, contador)
    else:
        janela.blit(personagem_sprites[direcao][0], (x_personagem, y_personagem))
        
    texto_vida = atualizar_texto_vida(font, vida_personagem)
    janela.blit(texto_vida, (10, 10))

    # Atualizar a tela
    pygame.display.update()
    clock.tick(30)

pygame.quit()
exit()



