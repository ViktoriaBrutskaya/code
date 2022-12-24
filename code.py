import pygame
import random
pygame.init()
win_height = 750
win_width = 1300
win = pygame.display.set_mode((win_width,win_height))#создание дисплея определенной ширины и длины
pygame.display.set_caption("Swowman Fight")

pygame.mixer.music.load("music/Dean Martin - Let It Snow (minus).mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


clock = pygame.time.Clock()#для отслеживания времени
current_time = 0
sock_getted_time = 0
show_bonus_time = 0
take_snowflake_time = 0

bonus = 0
score = 0
final_score = 500
bad_snowman_score = 50
speed = 1.5
speed_flag = 1.5#возращаем скорость снеговика после сбора носка

run = True
show_bonus = False
bad_end_eaten = False
bad_end_melted = False
good_end = False
show = True
set_restart = False
show_rules_time = True

width = 145
height = 158
bad_snowman_width = 140
bad_snowman_height = 150
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


bg = pygame.image.load('images/фон3.jpg')
snowman = pygame.image.load('images/снеговик175.png')
snowflake = pygame.image.load('images/снежинка65.png')
snowflake1 = pygame.image.load('images/снежинка65.png')
snowflake2 = pygame.image.load('images/снежинка65.png')
sock = pygame.image.load('images/носок110.png')
gift = pygame.image.load('images/подарок110.png')
candy = pygame.image.load('images/леденец110.png')
bad_snowman = pygame.image.load('images/снеговикплохой180.png')


def draw_counter(surf, text,size, x, y,font_type='nexa-script-heavy.ttf'):#отрисовка текста счетчиков
    font = pygame.font.Font(font_type,20)
    text_surface = font.render(text, True,(0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x+10, y)
    surf.blit(text_surface, text_rect)


def is_taken(x,y,w,h,x1,y1,w1,h1):

    if x<x1<x+w or x<x1+w1<x+w: #берется если находиться в следующем диапазоне
        if y<y1<y+h or y<y1+h1<y+h:
            return True
    else:
        return False


def drawWindow():
    win.blit(bg, (0,0))#наложение на основной дисплей фона(коордтнаты от угла 0,0)
    win.blit(snowman, (x,y))
    draw_counter(win, str(score),14, x+width/2, y+height)
    win.blit(sock,(sock_x,sock_y))
    win.blit(gift,(gift_x,gift_y))
    win.blit(snowflake,(snowflake_x,snowflake_y))
    win.blit(snowflake1,(snowflake_x1,snowflake_y1))
    win.blit(snowflake2,(snowflake_x2,snowflake_y2))
    win.blit(bad_snowman,(bad_snowman_x,bad_snowman_y))
    draw_counter(win, str(bad_snowman_score), 14, bad_snowman_x+width/2, bad_snowman_y+height)
    pygame.display.update()#обновление, перерисовка цвета пикселей


def start_game():#запуск игры
    #переменные значение которых можно отределить из любого места в коде
    global run,x,y,width,height,snowflake_x,snowflake_y,snowflake_widthsnowflake_height, bad_snowman_width
    global score,sock_x,sock_y,booster_width,booster_height,sock_getted_time, bad_snowman_height, bad_end_eaten, bad_end_melted, good_end
    global speed,gift_y,gift_x,show_bonus_time,current_time, take_snowflake_time, show, set_restart, show_rules_time
    global bonus,show_bonus,bad_snowman_x,bad_snowman_y,bad_snowman_score,snowflake_x1,snowflake_y1,snowflake_x2,snowflake_y2
    if set_restart:
        run = True
        show_end = False
        show_rules_time = False
        score = 0
        bad_snowman_score = 50
        bad_end_eaten = False
        bad_end_melted = False
        good_end = False
        take_snowflake_time = pygame.time.get_ticks()
        x = random.randrange(0,win_width - width,1)#создание рандомной координаты x для снеговика(начало,конец,ширина(диапазон))
        y=random.randrange(0,win_height - height,1)
        bad_snowman_x = random.randrange(0,win_width - bad_snowman_width,1)
        bad_snowman_y = random.randrange(0,win_height - bad_snowman_height,1)

    while run:

        pygame.time.delay(10)

        current_time = pygame.time.get_ticks()#сколько прошло миллисек с начала
        if final_score == score:
            show_rules_time = False
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
            if bad_snowman_score > score:
                show_rules_time = False
                bad_end_eaten = True
                show = False
                run = False
            elif bad_snowman_score <= score:
                score += bad_snowman_score
                bad_snowman_x = random.randrange(0,win_width - bad_snowman_width,1)
                bad_snowman_y = random.randrange(0,win_height - bad_snowman_height,1)
                bad_snowman_score *=3

        if current_time - sock_getted_time >3000:
            speed = speed_flag
        if current_time - take_snowflake_time >15000:
            show_rules_time = False
            bad_end_melted = True
            show = False
            run = False

        if show_bonus == True:
            draw_counter(win, str(bonus), 80, 700, 300)

        for event in pygame.event.get():#выход из игры
            if event.type == pygame.QUIT:
                show_end = False
                show = False
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

def restart():
    global set_restart
    set_restart = True
    start_game()

def show_rules():
    global show_rules_time
    rools_back = pygame.image.load('images/rules.jpg')
    back_but=Button(182,70)

    while show_rules_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(rools_back,(0,0))
        back_but.draw_but(90,100,'Back',show_menu,50)
        pygame.display.update()
        clock.tick(50)


font_name = pygame.font.match_font('nexa-script-heavy.ttf')
def print_the_bad_end(message,x,y, font_color=(255,255,255), font_type='nexa-script-heavy.ttf',font_size=75):#отрисовка плохого конца
    font_type = pygame.font.Font(font_type,font_size)
    text = font_type.render(message, True, font_color, (159,1,52))
    win.blit(text, (x, y))
def print_the_good_end(message,x,y, font_color=(255,255,255), font_type='nexa-script-heavy.ttf',font_size=85):#отрисовка хорошего конца
    font_type = pygame.font.Font(font_type,font_size)
    text = font_type.render(message, True, font_color, (254,144,0))
    win.blit(text, (x, y))
def end_of_the_game():
    global show_rules_time
    show_rules_time = False
    back = pygame.image.load('images/menu.jpg')
    show_end = True
    restart_but = Button(250,90)
    quit_but=Button(200,80)

    while show_end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(back,(0,0))
        restart_but.draw_but(526,430,'Restart',restart,50)
        quit_but.draw_but(80, 80, 'Quit', quit, 50)
        if bad_end_eaten:
            back = pygame.image.load('images/badend.jpg')
            print_the_bad_end('You was eaten!', 375, 320)
        elif bad_end_melted:
            print_the_bad_end('You was melted!',355, 330)
            back = pygame.image.load('images/badend.jpg')
        elif good_end:
            print_the_good_end('You win!',455, 320)
        else:
            pygame.quit()
            quit()
        pygame.display.update()
        clock.tick(50)

def show_menu():
    menu_back=pygame.image.load('images/menu.jpg')
    start_but = Button(385,90)
    quit_but=Button(160,90)
    rules_but = Button(200,90)

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(menu_back,(0,0))
        start_but.draw_but(450,360,'Start game!',start_game,60)
        quit_but.draw_but(562, 460, 'Quit', quit, 50)
        rules_but.draw_but(545, 260, 'Rules', show_rules,50)

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

        else:
            pygame.draw.rect(win, self.active_color, (x, y, self.width, self.heigth))#верхний левый угол, ширина и высота
        print_menu(message=message,x=x+20,y=y+10,font_size=font_size)


show_menu()
show = False
print(show_rules_time)
show_rules_time = False
end_of_the_game()
show_end = False
pygame.quit()
