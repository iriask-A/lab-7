import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock_img = pygame.image.load("images/clock.png").convert()
min_hand = pygame.image.load("images/min_hand.png").convert()
sec_hand = pygame.image.load("images/sec_hand.png").convert()
min_hand.set_colorkey((0, 0, 0))
sec_hand.set_colorkey((0, 0, 0))
min_hand = pygame.transform.scale(min_hand, (600, 600))  
sec_hand = pygame.transform.scale(sec_hand, (600, 600))  
min_angle = 0  
sec_angle = 0  
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rotated_min_hand = pygame.transform.rotate(min_hand, min_angle)
    rotated_sec_hand = pygame.transform.rotate(sec_hand, sec_angle)
    min_rect = rotated_min_hand.get_rect(center=(400, 300))
    sec_rect = rotated_sec_hand.get_rect(center=(400, 300))
    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))
    screen.blit(rotated_min_hand, min_rect.topleft)
    screen.blit(rotated_sec_hand, sec_rect.topleft)

    pygame.display.flip()

    min_angle -= 1 
    sec_angle -= 6 

    clock.tick(60)

pygame.quit()
