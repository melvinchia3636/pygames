#import library
import pygame
import random

pygame.init() #initialize game

#set window length and width
win_length = 500
win_width = 500

#set the random pipe initial coordinate
ranbeamdown = [[[490, 500]]]
ranbeamup = [[[500, -10]]]
beamx = 500

charpos = [20, 240] #set the character initial coordinate
mark = 0 #set the initial mark

gwin = pygame.display.set_mode((win_length, win_width)) #open a game window called 'gwin' 
clock = pygame.time.Clock() #get the game tick

def game(): #game main code

    global mark #globalize player mar

    #get random height of bith up and down beam
    ranheightup = random.randint(1,20)
    ranheightdown = random.randint(1,20)
    
    #append the coordinates list of lower beams
    for height in range(1, ranheightdown+1):
        for beamdown in ranbeamdown:
            beamdown.append([beamx, beamdown[0][1]-(height*10)])

    #append the coordinates list of the upper beams
    for height in range(1, ranheightup+1):
        for beamup in ranbeamup:
            beamup.append([beamx, beamup[0][1]+(height*10)])

    for x in range(10): #set the distance between beams
        #check if player touch the beams
        colorup = str(gwin.get_at((22, charpos[1])))
        colordown = str(gwin.get_at((22, charpos[1]-11)))
        shitup = colorup.split()[2]
        shitdown = colordown.split()[2]

        if shitup == '255,' or shitdown == '255,':
            pygame.quit()
            quit() #LOSE

        #mark counter
        dmark = str(gwin.get_at((20, 1)))
        dmark = dmark.split()[2]
        if dmark == '255,':
            mark += 1

        gwin.fill((0,0,0)) #refresh the screen

        pygame.draw.rect(gwin, (0,255,0), (charpos[0], charpos[1], 10, 10)) #show the character

        charpos[1] += 5 #simulate the gravity

        #check if space key got pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            charpos[1] -= 10 #move character up

        #show the lower beams
        for beamdown in ranbeamdown:
            for beamnumdown in beamdown:
                pygame.draw.rect(gwin, (255,255,255), (beamnumdown[0],beamnumdown[1], 10, 10))

        #change the x_coordinates of the lower beams
        for beamdown in ranbeamdown:
            for beamblockdown in beamdown:
                beamblockdown[0]-=10

        #show the upper beams
        for beamup in ranbeamup:
            for beamnumup in beamup:
                pygame.draw.rect(gwin, (255,255,255), (beamnumup[0],beamnumup[1], 10, 10))

        #chahnge the coordinates of the upper beams
        for beamup in ranbeamup:
            for beamblockup in beamup:
                beamblockup[0]-=10  

        pygame.display.update() #update the screen
        clock.tick(20)#set the fps

#main loop
while True:
    #checked if the close window button get pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #quit the game
    #checked if the character too low of too high
    if charpos[1] == 490:
        charpos[1] -= 10
    if charpos[1] == 0:
        charpos[1] += 10

    game() #called the main game
    pygame.display.set_caption(str(mark))#set the title of the window to player's marks