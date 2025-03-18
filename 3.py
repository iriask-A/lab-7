import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
x_coordinate = 100
y_coordinate = 100
circle_radius = 25
circle_speed = 20
running = True

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_coordinate -= circle_speed
            elif event.key == pygame.K_DOWN:
                y_coordinate += circle_speed
            elif event.key == pygame.K_LEFT:
                x_coordinate -= circle_speed
            elif event.key == pygame.K_RIGHT:
                x_coordinate += circle_speed
    x_coordinate = max(circle_radius, min(x_coordinate, 500 - circle_radius))
    y_coordinate = max(circle_radius, min(y_coordinate, 500 - circle_radius))
    pygame.draw.circle(screen, (255, 0, 0), (x_coordinate, y_coordinate), circle_radius)
    pygame.display.flip()

pygame.quit()