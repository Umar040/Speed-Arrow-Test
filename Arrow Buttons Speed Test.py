import pygame
import random
import time

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280,720))
font = pygame.font.SysFont('Calibri',40)
clock = pygame.time.Clock()
running = True
#Image path for green arrow pointing right
arrowImagePath = ".\\Images\\Green Right Arrow.png"
rightArrow = pygame.image.load(arrowImagePath)
rightArrow = pygame.transform.scale(rightArrow,(100,100)) #Scaling image to always have consistant size
downArrow = pygame.transform.rotate(rightArrow, 270) #Rotating image to get the other directions for the arrow (Needs changing if the arrow is not pointing right
leftArrow = pygame.transform.rotate(rightArrow, 180)
upArrow = pygame.transform.rotate(rightArrow, 90)

#Image path for red arrow which is for when a wrong arrow is pressed
rarrowImagePath = ".\\Images\\NBR Right Arrow.png"
rrightArrow = pygame.image.load(rarrowImagePath)
rrightArrow = pygame.transform.scale(rrightArrow,(100,100))
rdownArrow = pygame.transform.rotate(rrightArrow, 270)
rleftArrow = pygame.transform.rotate(rrightArrow, 180)
rupArrow = pygame.transform.rotate(rrightArrow, 90)

arrows = []

#If a wrong button is pressed add the red arrow to the current arrow position and then wait for 3 seconds (Time to wait can be altered by changing time.sleep value)
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
    pygame.event.clear()
    

#Generate 20 random arrows
for x in range(20):
    arrows.append(random.randint(1,4))

startTime = time.time()
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
        #If the arrow goes off screen then stop drawing otherwise draw the correct arrow to the screen with x position
        if 101*x > 1280:
            break
        if arrows[x] == 1:
            screen.blit(rightArrow, rightArrow.get_rect().move(101*x,0))
        elif arrows[x] == 2:
            screen.blit(downArrow, downArrow.get_rect().move(101*x,0))
        elif arrows[x] == 3:
            screen.blit(leftArrow, leftArrow.get_rect().move(101*x,0))
        elif arrows[x] == 4:
            screen.blit(upArrow, upArrow.get_rect().move(101*x,0))
    pygame.display.flip()

    if len(arrows) == 0:
        endTime = time.time() - startTime
        winText = "Congratulations you finished 20 arrows in "+str(endTime)+"!"
        print(winText)
        text = font.render(winText,True,(255,255,255))
        screen.blit(text,(0,0))
        pygame.display.flip()
        time.sleep(5)
        running = False
        
    clock.tick(60)
    
pygame.quit()
