import pygame

screen = pygame.display.set_mode( (700, 500) )
pygame.display.set_caption("Laberinto")


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, img):
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        pass

class Enemy(GameSprite):
    def update(self):
        pass

class Wall():
    pass

prueba = GameSprite(0, 0, 100, 100, 0, "pac-1.png")
run = True

fondo = pygame.image.load("winner_1-1.jpg")
while run:
    
    screen.fill( (150, 0, 255) )
    screen.blit(fondo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    prueba.draw()

    pygame.display.update()