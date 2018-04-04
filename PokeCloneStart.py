import pygame

x = pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

displayH = 1080
displayW = 1920

print(x)

gameDisplay = pygame.display.set_mode((displayW, displayH))

pygame.display.set_caption('PokeClone V_0.0.1')

pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        print(event)

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [displayW/2, displayH/2, 100, 100])
    pygame.display.update()

pygame.quit()
quit()