import pygame

pygame.init()

win_length = 501
win_height = 501

gwin = pygame.display.set_mode((win_length, win_height))

pygame.display.set_caption('Stupid GRID')

run = True

white = 255, 255, 255

def drawgrid(window, x, y, dis, color):

    global win_length
    global win_height

    for i in range(int(win_length/dis)+1):
        point1 = x,0
        point2 = x,500
        pygame.draw.line(window, color, point1, point2)
        pygame.display.update()
        x+=dis
        

    for i in range(int(win_height/dis)+1):
        point1 = 0,y
        point2 = 500,y
        pygame.draw.line(window, color, point1, point2)
        pygame.display.update()
        y+=dis

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    drawgrid(gwin, 0, 0, 10, white)

pygame.quit()
