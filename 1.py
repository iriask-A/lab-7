import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock_img = pygame.image.load("clock.jpg.webp").convert() 
clock_arrow1 = pygame.image.load("arrow1.jpg").convert() 
clock_arrow2 = pygame.image.load("arrow2.jpg").convert() 
clock_arrow1.set_colorkey((255, 255, 255))
clock_arrow2.set_colorkey((255, 255, 255))
a=pygame.transform.scale(clock_arrow1,(100,150))
b=pygame.transform.scale(clock_arrow2,(100,120))


running = True 

while running: 
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))
    screen.blit(a, (275, 130))
    screen.blit(b, (255, 180))
    pygame.display.flip()

pygame.quit()
