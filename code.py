import pygame
import random


pygame.init()

win_height = 750
win_width = 1300
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Swowmen Fight")

pygame.mixer.music.load("music/Dean Martin - Let It Snow (minus).mp3")
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play(-1)

text = "Rools of game"

clock = pygame.time.Clock()
current_time = 0
sock_getted_time = 0
show_bonus_time = 0
game_start_time = 0
time_of_take_gift = 0
time_of_take_sock = 0

time_for_random_gift = 0
time_for_random_sock = 0

bonus = 0
score = 0
bad_snowman_score = 150
speed = 1.5
speed_flag = 1.5

run = True
show_bonus = False

width = 145
height = 158
snowflake_height = 100
snowflake_width = 100
booster_width = 110
booster_height = 110

x = random.randrange(0,win_width - width,1)
y=random.randrange(0,win_height - height,1)
snowflake_x = random.randrange(0,win_width - snowflake_width,1)
snowflake_y=random.randrange(0,win_height - snowflake_height,1)
sock_x = random.randrange(0,win_width - booster_width,1)
sock_y=random.randrange(0,win_height - booster_height,1)
candy_x = random.randrange(0,win_width - booster_width,1)
candy_y=random.randrange(0,win_height - booster_height,1)
gift_x = random.randrange(0,win_width - booster_width,1)
gift_y=random.randrange(0,win_height - booster_height,1)
bad_snowman_x = random.randrange(0,win_width - width,1)
bad_snowman_y = random.randrange(0,win_height - height,1)


font_name = pygame.font.match_font('arial')





bg = pygame.image.load('images/фон.jpg')
snowman = pygame.image.load('images/снеговик175.png')
snowflake = pygame.image.load('images/снежинка100.png')
sock = pygame.image.load('images/носок110.png')
gift = pygame.image.load('images/подарок110.png')
candy = pygame.image.load('images/леденец110.png')
bad_snowman = pygame.image.load('images/снеговикплохой180.png')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True,(0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_snowflake():
    pygame.time.set_timer(event,150000)
    win.blit(snowflake,(random.randrange(0,win_width - width,1),random.randrange(0,win_height - height,1)))

def is_taken(x,y,w,h,x1,y1,w1,h1):

    if x<x1<x+w or x<x1+w1<x+w:
        if y<y1<y+h or y<y1+h1<y+h:
            return True
    else:
        return False

def drawWindow():
    win.blit(bg, (0,0))
    win.blit(snowman, (x,y))
    draw_text(win, str(score), 14, x+width/2, y+height)
    win.blit(sock,(sock_x,sock_y))
    win.blit(gift,(gift_x,gift_y))
    win.blit(candy,(candy_x,candy_y))
    win.blit(snowflake,(snowflake_x,snowflake_y))
    win.blit(bad_snowman,(bad_snowman_x,bad_snowman_y))
    draw_text(win, str(bad_snowman_score), 14, bad_snowman_x+width/2, bad_snowman_y+height)
    pygame.display.update()

pygame.mixer.music.play(-1)
while run:
    pygame.time.delay(10)


    current_time = pygame.time.get_ticks()

    if is_taken(x,y,width,height,snowflake_x,snowflake_y,snowflake_width,snowflake_height) == True:
        score = score +1
        snowflake_x = random.randrange(0,win_width - snowflake_width,1)
        snowflake_y = random.randrange(0,win_height - snowflake_height,1)

    if is_taken(x,y,width,height,sock_x,sock_y,booster_width,booster_height) == True:
        sock_getted_time = pygame.time.get_ticks()
        time_of_take_sock = pygame.time.get_ticks()
        time_for_random_sock = random.randrange(5000,150000,500)
        speed = 4
        sock_x = -200
        sock_y = -200

    if is_taken(x,y,width,height,candy_x,candy_y,booster_width,booster_height) == True:
        candy_x = random.randrange(0,win_width - booster_width,1)
        candy_y = random.randrange(0,win_height - booster_height,1)

    if is_taken(x,y,width,height,gift_x,gift_y,booster_width,booster_height) == True:
        show_bonus_time = pygame.time.get_ticks()
        time_of_take_gift = pygame.time.get_ticks()
        time_for_random_gift = random.randrange(5000,150000,500)
        bonus = random.randrange(1,10,1)
        show_bonus = True
        score = score + bonus
        gift_x = -200
        gift_y = -200

    if is_taken(x,y,width,height,bad_snowman_x,bad_snowman_y,width,height) == True:
        if bad_snowman_score > score:
            run = False

    if current_time - sock_getted_time >5000:
        speed = speed_flag

    if current_time - show_bonus_time > 2000:
        show_bonus = False

    if show_bonus == True:
        draw_text(win, str(bonus), 80, 700, 300)

    if current_time - time_of_take_gift > time_for_random_gift:
        gift_x = random.randrange(0,win_width - booster_width,1)
        gift_y = random.randrange(0,win_height - booster_height,1)

    if current_time - time_of_take_sock > time_for_random_sock:
        sock_x = random.randrange(0,win_width - booster_width,1)
        sock_y = random.randrange(0,win_height - booster_height,1)


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
