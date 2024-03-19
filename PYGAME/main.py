import pygame

#initial config

pygame.init()

#create a player screen
WIDTH = 400
HEIGHT = 400

#background color
BG_COLOR = (133, 193, 233)
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #W,H
pygame.display.set_caption("My game")

#main loop

status =  True
while status:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        status= False  

    screen.fill(BG_COLOR)
    pygame.display.flip()
    
pygame.quit()
