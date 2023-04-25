import pygame
pygame.init()
background=pygame.display.set_mode((480, 360))
pygame.display.set_caption("머드락")

image_bg=pygame.image.load("./image/1.png")
image_banana=pygame.image.load("./image/2.png")
image_monkey=pygame.image.load("./image/3.png")
size_bg_width=background.get_size()[0]
size_bg_height=background.get_size()[1]
size_banana_width=image_banana.get_size()[0]
size_banana_height=image_banana.get_size()[1]
size_monkey_width=image_monkey.get_rect().size[0]
size_monkey_height=image_monkey.get_rect().size[1]
x_pos_banana=size_bg_width/2-size_banana_width/2
y_pos_banana=0
x_pos_monkey=size_bg_width/2-size_monkey_width/2
y_pos_monkey=size_bg_height-size_monkey_height
x_speed_banana=1
y_speed_banana=1
to_x=0
point=0
font_point=pygame.font.SysFont("notosanskrthin", 30)
font_gameover=pygame.font.SysFont("notosanskrregular", 80)
text_gameover=font_gameover.render('GAME OVER', True,(255,43,0))
size_text_width=text_gameover.get_rect().size[0]
size_text_height=text_gameover.get_rect().size[1]
x_pos_text=size_bg_width/2-size_text_width/2
y_pos_text=size_bg_height/2-size_text_height/2
play=True
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                to_x=3
            if event.key==pygame.K_LEFT:
                to_x=-3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                to_x=0
    if x_pos_monkey<0:
        x_pos_monkey=0
    elif x_pos_monkey>size_bg_width-size_monkey_width:
        x_pos_monkey=size_bg_width-size_monkey_width
    else:
        x_pos_monkey+=to_x
    x_pos_banana+=x_speed_banana
    y_pos_banana+=y_speed_banana

    y_speed_banana += 0.02
    if x_pos_banana <= 0:
        x_speed_banana *= -1
        x_pos_banana=0
    elif x_pos_banana>=size_bg_width-size_banana_width:
        x_speed_banana*=-1
        x_pos_banana=size_bg_width-size_banana_width
    if y_pos_banana <= 0:
        y_speed_banana *= -1
        y_pos_banana=0
    elif y_pos_banana>=size_bg_height-size_banana_height:
        background.blit(text_gameover,(x_pos_text,y_pos_text))
        pygame.display.update()
        pygame.time.delay(2000)
        play=False
    
    rect_banana=image_banana.get_rect()
    rect_banana.left=x_pos_banana
    rect_banana.top=y_pos_banana

    rect_monkey=image_monkey.get_rect()
    rect_monkey.left=x_pos_monkey
    rect_monkey.top=y_pos_monkey

    if rect_monkey.colliderect(rect_banana):
        x_speed_banana*=-1
        y_speed_banana*=-1
        point+=1

    background.blit(image_bg, (0,0))
    background.blit(image_banana,(x_pos_banana, y_pos_banana))
    background.blit(image_monkey,(x_pos_monkey, y_pos_monkey))
    text_point=font_point.render(str(point),True,(80,120,200))
    background.blit(text_point,(10,10))
    pygame.display.update()
pygame.quit()
