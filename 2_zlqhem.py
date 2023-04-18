import pygame

pygame.init()

background=pygame.display.set_mode((480,360))
pygame.display.set_caption("머드락")

fps=pygame.time.Clock()

x_pos=background.get_size()[0]//2
y_pos=background.get_size()[1]//2

to_x=0
to_y=0

play=True
while play:
    deltaTime=fps.tick(300)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                to_y=-2
            elif event.key==pygame.K_DOWN:
                to_y=2
            elif event.key==pygame.K_RIGHT:
                to_x=2
            elif event.key==pygame.K_LEFT:
                to_x=-2
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                to_y=0
            elif event.key==pygame.K_DOWN:
                to_y=0
            elif event.key==pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_LEFT:
                to_x=0
    x_pos+=to_x
    y_pos+=to_y

    background.fill((80,200,120)) #Paris Green
    pygame.draw.circle(background, (0,52,88), (x_pos,y_pos), 10) #Prussian Blue
    pygame.display.update()
pygame.quit()
