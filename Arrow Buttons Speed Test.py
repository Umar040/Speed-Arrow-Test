import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
arrowImagePath = "C:\\Users\\Muna2\\OneDrive\\Documents\\Python Projects\\Images\\Green Right Arrow.png"
rightArrow = pygame.image.load(arrowImagePath)
rightArrow = pygame.transform.scale(rightArrow,(100,100))
downArrow = pygame.transform.rotate(rightArrow, 270)
leftArrow = pygame.transform.rotate(rightArrow, 180)
upArrow = pygame.transform.rotate(rightArrow, 90)

rarrowImagePath = "C:\\Users\\Muna2\\OneDrive\\Documents\\Python Projects\\Images\\NBR Right Arrow.png"
rrightArrow = pygame.image.load(rarrowImagePath)
rrightArrow = pygame.transform.scale(rrightArrow,(100,100))
rdownArrow = pygame.transform.rotate(rrightArrow, 270)
rleftArrow = pygame.transform.rotate(rrightArrow, 180)
rupArrow = pygame.transform.rotate(rrightArrow, 90)

arrows = []

def wait(screen):
    if arrows[0] == 1:
        screen.blit(rrightArrow, rrightArrow.get_rect())
    elif arrows[0] == 2:
        screen.blit(rdownArrow, rdownArrow.get_rect().move(0,0))
    elif arrows[0] == 3:
        screen.blit(rleftArrow, rleftArrow.get_rect().move(0,0))
    elif arrows[0] == 4:
            screen.blit(rupArrow, rupArrow.get_rect().move(0,0))
    pygame.display.flip()
    time.sleep(3)
    

for x in range(20):
    arrows.append(random.randint(1,4))
print(arrows)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if arrows[0] == 1:
                    arrows.pop(0)
                else:
                    wait(screen)
            elif event.key == pygame.K_DOWN:
                if arrows[0] == 2:
                    arrows.pop(0)
                else:
                    wait(screen)
            elif event.key == pygame.K_LEFT:
                if arrows[0] == 3:
                    arrows.pop(0)
                else:
                    wait(screen)
            elif event.key == pygame.K_UP:
                if arrows[0] == 4:
                    arrows.pop(0)
                else:
                    wait(screen)
        
    screen.fill("black")
    for x in range(len(arrows)):
        if arrows[x] == 1:
            screen.blit(rightArrow, rightArrow.get_rect().move(101*x,0))
        elif arrows[x] == 2:
            screen.blit(downArrow, downArrow.get_rect().move(101*x,0))
        elif arrows[x] == 3:
            screen.blit(leftArrow, leftArrow.get_rect().move(101*x,0))
        elif arrows[x] == 4:
            screen.blit(upArrow, upArrow.get_rect().move(101*x,0))
    pygame.display.flip()

    clock.tick(60)
    
pygame.quit()
