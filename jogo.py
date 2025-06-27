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
    carregar_imagem_esposa,
    mostrar_tela_final
)

from jogopython.zombie import (
    Zombie, 
    carregar_zombies_fundo2, 
    desenhar_zombies_fundo2,
    carregar_zombies_fundo3, 
    desenhar_zombies_fundo3
)

pygame.init()

# Música de fundo
pygame.mixer.music.load("musics/Call of Duty 4 Modern Warfare OST - All In.mp3")
pygame.mixer.music.play(-1)

# Tela
janela = pygame.display.set_mode((constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL))
pygame.display.set_caption("Taking the Cure")
font = pygame.font.SysFont("arial black", 18)

# Carregamento
telas = carregar_telas()
personagem_sprites = carregar_imagens_personagem()
zombies_fundo2 = carregar_zombies_fundo2()
zombies_fundo3 = carregar_zombies_fundo3()
zombies_fundo2 = carregar_zombies_fundo2()
image_esposa = carregar_imagem_esposa()
imagens_personagem = carregar_imagens_personagem()

fundo = telas["logo"]

# Carregar e redimensionar logo
logo_original = pygame.image.load("img/logo/logo.png")
logo_redimensionada = pygame.transform.scale(logo_original, (constants.TAMANHO_HORIZONTAL, constants.TAMANHO_VERTICAL))
janela.blit(logo_redimensionada, (0, 0))
pygame.display.update()
time.sleep(3)

fundo = telas["fundoHitory"]
texto_intro = constants.TEXTO_INTRO
fonte_intro = pygame.font.SysFont("arial", 28)
texto_parcial = []
indice_letra = 0
tempo_anterior = pygame.time.get_ticks()
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

# Estados iniciais para a fase principal
x_personagem, y_personagem = 300, 200
direcao = "frente"
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial black", 32)

##fundo_atual = "fundo1"
fundo_atual = "fundo1"
contador = 0
rodando = True
vida_personagem = 4
contador = 0

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

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

    fundo_atual, x_personagem, y_personagem = verificar_colisoes_tela(fundo_atual, x_personagem, y_personagem)
    janela.blit(telas[fundo_atual], (0, 0))

    if fundo_atual == "fundo2":
        desenhar_zombies_fundo2(janela, zombies_fundo2)
        vida_personagem = verificar_colisao_personagem_zombie(x_personagem, y_personagem, constants.LARGURA_PERSONAGEM, constants.ALTURA_PERSONAGEM, zombies_fundo2, vida_personagem)

    if fundo_atual == "fundo3":
        desenhar_zombies_fundo3(janela, zombies_fundo3)
        vida_personagem = verificar_colisao_personagem_zombie(x_personagem, y_personagem, constants.LARGURA_PERSONAGEM, constants.ALTURA_PERSONAGEM, zombies_fundo3, vida_personagem)

    if vida_personagem <= 0:
        janela.blit(telas["gameover"], (0,0))
        pygame.display.update()

        pygame.time.delay(4000) # esperar 4 segundos
        rodando = False

    if fundo_atual == "fundo4":
        janela.blit(image_esposa, (500,350))

        # Verifica se chegou até a esposa
        if 480 < x_personagem < 540 and 330 < y_personagem < 390:
            mostrar_tela_final(janela, font, constants.TEXTO_FINAL, telas["fundoHitory"])
            rodando = False

    if movendo:
        contador = desenhar_personagem(janela, imagens_personagem, x_personagem, y_personagem, direcao, contador)
    else:
        janela.blit(imagens_personagem[direcao][0], (x_personagem, y_personagem))

    texto_vida = atualizar_texto_vida(font, vida_personagem)
    janela.blit(texto_vida, (10, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
exit()





