
import pygame 



class GameSprite(pygame.sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.transform.scale(pygame.image.load(player_image), (80, 80))
        self.speed = player_speed


        # cada objeto debe almacenar la propiedad rect (rectángulo) en donde es ingresado
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    #método de dibujo del personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#clase de jugador principal
class Player(GameSprite):


    #método que implementa el control de objetos utilizando los botones de flechas del teclado
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


#clase de objeto enemigo
class Enemy(GameSprite):
    side = "left"


    #movimiento del enemigo
    def update(self):
        if self.rect.x <= 410:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


#clase de elemento de la pared
class Wall(pygame.sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.width = wall_width
        self.height = wall_height

        # imagen de la pared – un rectángulo de tamaño y color deseado
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)


        # cada objeto debe almacenar la propiedad rect (rectángulo)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def draw_wall(self):
        pygame.draw.rect(window, self.color, (self.rect.x, self.rect.y, self.width, self.height))


#Crea una ventana
win_width = 700
win_height = 500


#crea paredes

walls = pygame.sprite.Group()
w1 = Wall((255, 0, 0), win_width / 2 - win_width / 3, win_height / 2, 300, 10)
w2 = Wall((0, 0, 255), 410, win_height / 2 - win_height / 4, 10, 350)
w3 = Wall((0, 255, 0), 200, win_height / 2 - win_height / 4, 10, 350)
walls.add(w1)
walls.add(w2)
walls.add(w3)
print(walls)

#crea objetos
packman = Player('hero.png', 5, win_height - 80, 5)
monster = Enemy('cyborg.png', win_width - 80, 200, 5)
final_sprite = GameSprite('pac-1.png', win_width - 85, win_height - 100, 0)


# pygame setup
pygame.init()
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Labyrinth")
clock = pygame.time.Clock()


#variable responsable por cómo termina el juego
finish = False
#ciclo de juego
run = True
paused = False

while run:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused


    # RENDER YOUR GAME HERE
    #comprueba que el juego no ha terminado todavía
    if not finish and not paused:
        #actualiza el fondo con cada iteración
        window.fill((150, 0, 255))
        #dibuja las paredes


        #ejecuta el movimiento del objeto
        # w1.draw_wall()
        # w2.draw_wall()
        # w3.draw_wall()

        walls.draw(window)

        packman.update()
        monster.update()


        #los actualiza en una nueva ubicación con cada iteración del ciclo
        packman.reset()
        monster.reset()
        final_sprite.reset()


        #comprueba la colisión entre el personaje y el enemigo o las paredes
        # pygame.sprite.Group()

        # pygame.sprite.groupcollide()
        # pygame.sprite.spritecollide()


        if pygame.sprite.collide_rect(packman, monster) or pygame.sprite.spritecollide(packman, walls, True):
            finish = True

            #calcula la tasa
            img = pygame.image.load('game-over_1.png')
            window.fill((255, 255, 255))
            window.blit(pygame.transform.scale(img, (win_height , win_height )), (90, 0))


        if pygame.sprite.collide_rect(packman, final_sprite):
            finish = True
            img = pygame.image.load('thumb.jpg')
            window.fill((255, 255, 255))
            window.blit(pygame.transform.scale(img, (win_width, win_height)), (0, 0))


    # flip() the display to put your work on screen
    pygame.display.flip()


    clock.tick(60)  # limits FPS to 60


pygame.quit()