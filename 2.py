import pygame
pygame.init()
screen = pygame.display.set_mode((743,400))
base = pygame.image.load("images/base.jpg")
line = pygame.image.load("images/line.png")
pause = pygame.image.load("images/pause.png")
play = pygame.image.load("images/play.png")
skip = pygame.image.load("images/skip.png")
song = pygame.mixer.music.load("images/song.mp3")
notskip = pygame.image.load("images/skip-1.png")
pause = pygame.transform.scale(pause,(80,80))
play = pygame.transform.scale(play,(80,80))
skip = pygame.transform.scale(skip,(80,80))
notskip = pygame.transform.scale(notskip,(80,80))
line.set_colorkey((255,255,255))
pause.set_colorkey((255,255,255))
play.set_colorkey((255,255,255))
skip.set_colorkey((255,255,255))
pygame.mixer.music.load("images/song.mp3")
pygame.mixer.music.play(-1)
play_rect = play.get_rect(topleft=(280, 230))
pause_rect = pause.get_rect(topleft=(380, 230))
skip_rect = skip.get_rect(topleft=(480, 230))
rewind_rect = notskip.get_rect(topleft=(180, 230))
running = True
paused = False
while running:
    screen.fill((255, 255, 255))
    screen.blit(base, (0, 0))
    screen.blit(line, (72, -90))
    screen.blit(play, play_rect.topleft)
    screen.blit(pause, pause_rect.topleft)
    screen.blit(skip, skip_rect.topleft)
    screen.blit(notskip, rewind_rect.topleft)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_rect.collidepoint(mouse_pos):
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False  
            elif pause_rect.collidepoint(mouse_pos):
                pygame.mixer.music.pause()
                paused = True  
            elif skip_rect.collidepoint(mouse_pos):
                current_time = pygame.mixer.music.get_pos() / 1000  
                pygame.mixer.music.set_pos(current_time + 10)  
            elif rewind_rect.collidepoint(mouse_pos):
                pygame.mixer.music.stop()
                pygame.mixer.music.play()

    pygame.display.flip()

pygame.quit()