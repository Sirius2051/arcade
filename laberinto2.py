import pygame

window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Laberinto")

clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,  speed, img):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.rect.y -= self.speed
        if key[pygame.K_s]:
            self.rect.y += self.speed
        if key[pygame.K_a]:
            self.rect.x -= self.speed
        if key[pygame.K_d]:
            self.rect.x += self.speed

class Enemy(GameSprite):
    side = "left"
    def update(self):

        if self.rect.x <= 410:
            self.side = "right"
        if self.rect.x >= 800 - 80:
            self.side = "left"

        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        # self.color = color
        # self.width = width
        # self.height = height

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_img = pygame.transform.scale(pygame.image.load("winner_1-1.jpg"), (800, 500))
lost_img = pygame.transform.scale(pygame.image.load("game-over-3.jpg"), (800, 500))

hero = Player(100, 100, 80, 80, 10, "hero.png")
enemy = Enemy(720, 200, 80, 80, 10, "cyborg.png")
final = GameSprite(700, 400, 80, 80, 0, "pac-1.png")

wall1 = Wall(100, 0, 10, 400, (0, 0, 0))

running = True
playing = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if playing:
        window.fill((255, 255, 255))

        hero.update()
        hero.draw()

        enemy.update()
        enemy.draw()

        final.draw()
        wall1.draw()

        if pygame.sprite.collide_rect(hero, final):
            window.blit(win_img, (0, 0))
            playing = False

        if pygame.sprite.collide_rect(hero, enemy):
            window.blit(lost_img, (0, 0))
            playing = False



    pygame.display.update()
    clock.tick(40)
    