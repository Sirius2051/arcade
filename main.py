import pygame

window = pygame.display.set_mode((850, 650))
window.fill((200, 0, 120))


running = True

bg = pygame.image.load("cave.png")
hero = pygame.image.load("enemy.png")

hero_rect = hero.get_rect()
while running:

    window.blit( pygame.transform.scale(bg, (850, 650)) , (0, 0))
    window.blit(hero, (hero_rect.x, hero_rect.y))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero_rect.y -= 20
            if event.key == pygame.K_DOWN:
                hero_rect.y += 20
            if event.key == pygame.K_LEFT:
                hero_rect.x -= 20
            if event.key == pygame.K_RIGHT:
                hero_rect.x += 20




    pygame.display.update()