import pygame
import random


pygame.init()

win_height = 750
win_width = 1300
win = pygame.display.set_mode((win_width,win_height))#создание дисплея определенной ширины и длины
pygame.display.set_caption("Swowmen Fight")


#def start_game() должен быть написан цикл который запускает игру засунуть вместо None эту функцию

pygame.mixer.music.load("music/Dean Martin - Let It Snow (minus).mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


clock = pygame.time.Clock()
current_time = 0
sock_getted_time = 0
show_bonus_time = 0
take_snowflake_time = 0

bonus = 0
score = 0
final_score = 1000
bad_snowman_score = 50
speed = 1.5
speed_flag = 1.5#возращаем скорость снеговика после сбора носка

run = True
show_bonus = False
bad_end_eaten = False
bad_end_melted = False
good_end = False
show = True

bad_end_eaten_message = 'You was eaten'
bad_end_melted = 'You was melted'
good_end_message = 'You win'

width = 145
height = 158
bad_snowman_width = 140
bad_snowman_height = 150
#width1=150
#height=150
snowflake_height = 65
snowflake_width = 65
booster_width = 110
booster_height = 110

x = random.randrange(0,win_width - width,1)#создание рандомной координаты x для снеговика(начало,конец,ширина(диапазон))
y=random.randrange(0,win_height - height,1)
snowflake_x = random.randrange(0,win_width - snowflake_width,1)
snowflake_y=random.randrange(0,win_height - snowflake_height,1)
snowflake_x1 = random.randrange(0,win_width - snowflake_width,1)
snowflake_y1=random.randrange(0,win_height - snowflake_height,1)
snowflake_x2 = random.randrange(0,win_width - snowflake_width,1)
snowflake_y2=random.randrange(0,win_height - snowflake_height,1)
sock_x = random.randrange(0,win_width - booster_width,1)
sock_y=random.randrange(0,win_height - booster_height,1)
candy_x = random.randrange(0,win_width - booster_width,1)
candy_y=random.randrange(0,win_height - booster_height,1)
gift_x = random.randrange(0,win_width - booster_width,1)
gift_y=random.randrange(0,win_height - booster_height,1)
bad_snowman_x = random.randrange(0,win_width - bad_snowman_width,1)
bad_snowman_y = random.randrange(0,win_height - bad_snowman_height,1)
#bad_snowman_x = random.randrange(0,win_width - width1,1)
#bad_snowman_y = random.randrange(0,win_height - height1,1)


font_name = pygame.font.match_font('intro')



bg = pygame.image.load('images/фон.jpg')
snowman = pygame.image.load('images/снеговик175.png')
snowflake = pygame.image.load('images/снежинка65.png')
snowflake1 = pygame.image.load('images/снежинка65.png')
snowflake2 = pygame.image.load('images/снежинка65.png')
sock = pygame.image.load('images/носок110.png')
gift = pygame.image.load('images/подарок110.png')
candy = pygame.image.load('images/леденец110.png')
bad_snowman = pygame.image.load('images/снеговикплохой180.png')

def draw_text(surf, text, size, x, y):#отрисовка текста счетчиков
    font = pygame.font.Font(font_name, 23)
    text_surface = font.render(text, True,(0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x+10, y)
    surf.blit(text_surface, text_rect)

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
    win.blit(snowflake,(snowflake_x,snowflake_y))
    win.blit(snowflake1,(snowflake_x1,snowflake_y1))
    win.blit(snowflake2,(snowflake_x2,snowflake_y2))
    win.blit(bad_snowman,(bad_snowman_x,bad_snowman_y))
    draw_text(win, str(bad_snowman_score), 14, bad_snowman_x+width/2, bad_snowman_y+height)
    pygame.display.update()





def start_game():
    global run,x,y,width,height,snowflake_x,snowflake_y,snowflake_widthsnowflake_height, bad_snowman_width
    global score,sock_x,sock_y,booster_width,booster_height,sock_getted_time, bad_snowman_height, bad_end_eaten, bad_end_melted, good_end
    global speed,gift_y,gift_x,show_bonus_time,current_time, take_snowflake_time, show
    global bonus,show_bonus,bad_snowman_x,bad_snowman_y,bad_snowman_score,snowflake_x1,snowflake_y1,snowflake_x2,snowflake_y2
    while run:

        pygame.time.delay(10)


        current_time = pygame.time.get_ticks()
        if final_score < score:
            good_end = True
            show = False
            run = False
        if is_taken(x,y,width,height,snowflake_x,snowflake_y,snowflake_width,snowflake_height) == True:
            take_snowflake_time = pygame.time.get_ticks()
            score = score +1
            snowflake_x = random.randrange(0,win_width - snowflake_width,1)
            snowflake_y = random.randrange(0,win_height - snowflake_height,1)
        if is_taken(x,y,width,height,snowflake_x1,snowflake_y1,snowflake_width,snowflake_height) == True:
            take_snowflake_time = pygame.time.get_ticks()
            score = score +1
            snowflake_x1 = random.randrange(0,win_width - snowflake_width,1)
            snowflake_y1 = random.randrange(0,win_height - snowflake_height,1)
        if is_taken(x,y,width,height,snowflake_x2,snowflake_y2,snowflake_width,snowflake_height) == True:
            take_snowflake_time = pygame.time.get_ticks()
            score = score +1
            snowflake_x2 = random.randrange(0,win_width - snowflake_width,1)
            snowflake_y2 = random.randrange(0,win_height - snowflake_height,1)

        if is_taken(x,y,width,height,sock_x,sock_y,booster_width,booster_height) == True:
            sock_getted_time = pygame.time.get_ticks()
            speed = 4
            sock_x = random.randrange(0,win_width - booster_width,1)
            sock_y = random.randrange(0,win_height - booster_height,1)

        if is_taken(x,y,width,height,gift_x,gift_y,booster_width,booster_height) == True:
            show_bonus_time = pygame.time.get_ticks()
            bonus = random.randrange(1,10,1)
            show_bonus = True
            score = score + bonus
            gift_x = random.randrange(0,win_width - booster_width,1)
            gift_y = random.randrange(0,win_height - booster_height,1)

        if is_taken(x,y,width,height,bad_snowman_x,bad_snowman_y,bad_snowman_width,bad_snowman_height) == True:
            if bad_snowman_score >= score:
                bad_end_eaten = True
                show = False
                run = False
            elif bad_snowman_score < score:
                score += bad_snowman_score
                bad_snowman_x = random.randrange(0,win_width - bad_snowman_width,1)
                bad_snowman_y = random.randrange(0,win_height - bad_snowman_height,1)
                bad_snowman_score *=3

        if current_time - sock_getted_time >3000:
            speed = speed_flag
        if current_time - take_snowflake_time >15000:
            bad_end_melted = True
            show = False
            run = False


        if show_bonus == True:
            draw_text(win, str(bonus), 80, 700, 300)
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

def show_rules():
    show_rules_time = True
    rools_back = pygame.image.load('images/menu.jpg')
    back_but=Button(210,90)

    while show_rules_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(rools_back,(0,0))
        back_but.draw_but(100,100,'Back',show_menu,50)
        pygame.display.update()
        clock.tick(50)
def restart():
        score = 0
        bad_snowman_score = 50
        bad_end_eaten = False
        bad_end_melted = False
        good_end = False
        take_snowflake_time = 0
        x = random.randrange(0,win_width - width,1)
        y=random.randrange(0,win_height - height,1)
        bad_snowman_x = random.randrange(0,win_width - bad_snowman_width,1)
        bad_snowman_y = random.randrange(0,win_height - bad_snowman_height,1)

def end_of_the_game():
    back = pygame.image.load('images/menu.jpg')
    show_end = True
    restart_but = Button(210,90)
    quit_but=Button(210,90)

    while show_end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(back,(0,0))
        restart_but.draw_but(100,100,'Restart',restart,50)
        quit_but.draw_but(520, 520, 'Quit', quit, 50)
        if bad_end_eaten:
            draw_text(win, bad_end_eaten_message, 20, 50,50)
        elif bad_end_melted:
            draw_text(win, bad_end_melted_message, 20, 50,50)
        elif good_end:
            draw_text(win, good_end_message, 20, 50,50)
        
        pygame.display.update()
        clock.tick(50)

def show_menu():
    menu_back=pygame.image.load('images/menu.jpg')
    start_but = Button(370,90)
    quit_but=Button(210,90)
    rules_but = Button(210,90)

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(menu_back,(0,0))
        start_but.draw_but(450,310,'Start game!',start_game,50)
        quit_but.draw_but(520, 520, 'Quit', quit, 50)
        rules_but.draw_but(520, 415, 'Rules', show_rules,50)

        pygame.display.update()
        clock.tick(50)

def print_menu(message,x,y, font_color=(255,255,255), font_type='nexa-script-heavy.ttf',font_size=30):
    font_type=pygame.font.Font(font_type,font_size)
    text=font_type.render(message,True,font_color)
    win.blit(text,(x,y))


class Button:
    def __init__(self,width,heigth):
        self.width=width
        self.heigth = heigth
        self.interactive_color = (255,146,1)
        self.active_color = (0, 47, 56)

    def draw_but(self,x,y,message,action=None,font_size=30):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        if x<mouse[0]<x+self.width and y < mouse[1] < y + self.heigth:
            pygame.draw.rect(win,self.interactive_color,(x,y,self.width,self.heigth))

            if click[0]==1:
                if action==quit:
                    pygame.quit()
                    quit()
                if action ==start_game:
                    start_game()
                if action == show_rules:
                    show_rules()
                if action == show_menu:
                    show_rules_time = False
                    show_menu()
                if action == restart:
                    restart()
                    start_game()

        else:
            pygame.draw.rect(win, self.active_color, (x, y, self.width, self.heigth))
        print_menu(message=message,x=x+40,y=y+10,font_size=font_size)


show_menu()
show = False
end_of_the_game()
pygame.quit()
