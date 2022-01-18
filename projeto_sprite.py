import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura_tela = 1000
altura_tela = 600

preto = 0, 0, 0
branco = 255, 255, 255
verde_matrix = 45, 255, 0

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("I Love my mother")


class Morte_atack(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites =  []
        self.sprites.append(pygame.image.load("ataque/ataque1.png"))
        self.sprites.append(pygame.image.load("ataque/ataque2.png"))
        self.sprites.append(pygame.image.load("ataque/ataque3.png"))
        self.sprites.append(pygame.image.load("ataque/ataque4.png"))
        self.sprites.append(pygame.image.load("ataque/ataque5.png"))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128 * 2, 128 * 2))

        self.rect = self.image.get_rect()
        self.rect.topleft = -10, 400
        self.animar = False

    def atack(self) -> object:
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual += 0.4
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False

            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128 * 2, 128 * 2))


sprite_atack = pygame.sprite.Group()
morte = Morte_atack()
sprite_atack.add(morte)


relogio = pygame.time.Clock()

imagem_fundo = pygame.image.load("foresta_terror.jpeg").convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela))

while True:
    relogio.tick(30)
    tela.fill((branco))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_SPACE]:
            morte.atack()


    tela.blit(imagem_fundo, (0, 0))

    sprite_atack.draw(tela)
    sprite_atack.update()

    pygame.display.flip()
