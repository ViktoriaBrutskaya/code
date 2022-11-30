import pygame
import random


pygame.init()

win_height = 750
win_width = 1300
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Swowmen Fight")

pygame.mixer.music.load("music/Dean Martin - Let It Snow (minus).mp3")
pygame.mixer.music.set_volume(0.4)

score = 0
width = 145
height = 158
x = random.randrange(0,win_width - width,1)
y=random.randrange(0,win_height - height,1)
speed = 2
run = True



bg = pygame.image.load('images/фон.jpg')
snowman = pygame.image.load('images/снеговик175.png')



def drawWindow():
    win.blit(bg, (0,0))
    win.blit(snowman, (x,y))
    pygame.display.update()


while run:
    pygame.time.delay(10)
    pygame.mixer.music.play(-1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0-25:
        x -=speed
    if keys[pygame.K_RIGHT]and x<1300 - width:
        x +=speed
    if keys[pygame.K_UP] and y>0-22:
        y =y -speed
    if keys[pygame.K_DOWN] and y<750 - height:
        y +=speed
    drawWindow()

pygame.quit()


