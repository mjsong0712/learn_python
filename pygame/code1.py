import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREED = (0, 255, 0)
RED = (255, 0, 0)

size = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("pygame")

done = False
clock = pygame.time.Clock()

roofx, roofy = 0, 0
gx, gy = 0,0

while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        roofx += -5
    if key_event[pygame.K_RIGHT]:
        roofx += 5
    if key_event[pygame.K_UP]:
        roofy += -5
    if key_event[pygame.K_DOWN]:
        roofy += 5
    if key_event[pygame.K_w]:
        gy += -5
    if key_event[pygame.K_a]:
        gx += -5
    if key_event[pygame.K_s]:
        gy += 5
    if key_event[pygame.K_d]:
        gx += 5
    screen.fill(WHITE)
    pygame.draw.polygon(screen, GREED, [[roofx + 600, roofy + 400], [roofx + 300, roofy + 400], [roofx + 450, roofy + 200]], 5)
    pygame.draw.polygon(screen, GREED, [[roofx + 600, roofy + 400], [roofx + 300, roofy + 400], [roofx + 450, roofy + 200]], 0)
    pygame.draw.lines(screen, RED, False, [[roofx + 325, roofy + 400],[325,600],[575,600],[roofx + 575, roofy + 400]], 5)
    pygame.draw.rect(screen, BLACK, [gx+ 375,gy +475, 100, 50], 5)
    pygame.draw.rect(screen, BLUE, [gx+375,gy +475, 100, 50], 0)
    pygame.draw.line(screen, BLACK, [gx+425,gy +475], [gx+425,gy +525], 5)
    pygame.draw.line(screen, BLACK, [gx+375,gy +500], [gx+475,gy +500], 5)
    pygame.display.flip()


pygame.quit()