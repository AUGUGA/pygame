import pygame
pygame.init()
background=pygame.display.set_mode((800,600))
pygame.display.set_caption("머드락")

x_pos=background.get_size()[0]//2
y_pos=background.get_size()[1]//2

play=True
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
        if event.type==pygame.MOUSEMOTION:
            x_pos, y_pos = pygame.mouse.get_pos()
            pygame.draw.circle(background,(80,200,120),(x_pos,y_pos), 10)
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                background.fill((20,135,200)) #KAIST Medium Blue
    pygame.display.update()
    background.fill((0,52,88))
    pygame.draw.circle(background, (80,200,120), (x_pos, y_pos), 10)
pygame.quit()

    
