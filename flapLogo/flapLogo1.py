import pygame
import random
import os

# Inicializando o Pygame
pygame.init()

# Definindo cores
WHITE = (255, 255, 255)

# Configurações da tela
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Customizado")

# Carregando a imagem de fundo
background = pygame.image.load('background.png')

# Função para carregar a imagem do pássaro
def load_bird_image(image_path):
    bird_img = pygame.image.load(image_path)
    bird_img = pygame.transform.scale(bird_img, (50, 35))  # Redimensionando
    return bird_img

# Função para o jogo principal
def game_loop(bird_image_path):
    # Variáveis do pássaro
    bird_img = load_bird_image(bird_image_path)
    bird_x = 50
    bird_y = HEIGHT // 2
    bird_y_change = 0

    # Variáveis dos tubos
    tube_width = 70
    tube_gap = 200
    tube_x = WIDTH
    tube_height = random.randint(100, 400)

    # Gravidade e Velocidade
    gravity = 1
    bird_speed = 0

    # Relógio para controlar a velocidade do jogo
    clock = pygame.time.Clock()

    # Loop principal do jogo
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_speed = -10

        # Aplicando gravidade
        bird_speed += gravity
        bird_y += bird_speed

        # Movendo os tubos
        tube_x -= 5
        if tube_x < -tube_width:
            tube_x = WIDTH
            tube_height = random.randint(100, 400)

        # Desenhando os elementos na tela
        screen.blit(background, (0, 0))
        screen.blit(bird_img, (bird_x, bird_y))

        # Desenhando os tubos
        pygame.draw.rect(screen, WHITE, (tube_x, 0, tube_width, tube_height))
        pygame.draw.rect(screen, WHITE, (tube_x, tube_height + tube_gap, tube_width, HEIGHT - tube_height - tube_gap))

        # Verificando colisão
        if (bird_y < tube_height or bird_y > tube_height + tube_gap) and (bird_x + 50 > tube_x and bird_x < tube_x + tube_width):
            running = False

        # Verificando se o pássaro tocou o chão ou saiu da tela
        if bird_y > HEIGHT - 50 or bird_y < 0:
            running = False

        # Atualizando a tela
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

# Caminho da imagem do pássaro
bird_image_path = os.path.join('images', 'your_bird_image.png')  # Substitua pelo caminho da imagem que você quer usar

# Inicia o jogo
game_loop(bird_image_path)
