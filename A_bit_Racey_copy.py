import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("Crash.wav")
pygame.mixer.music.load("Jazz_In_Paris.wav")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

bloack_color = (52,115,225)

background = pygame.image.load("Bakcground.png")
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carimg = pygame.image.load('Car.png')
enemyimg = pygame.image.load('Enemy.png')

pygame.display.set_icon(carimg)
pause = False
crash = True
def thing_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render('Dodged: '+str(count), True,black)
    gameDisplay.blit(text, (0, 0))


def thing(thingx, thingy):
    gameDisplay.blit(enemyimg, (thingx, thingy))
    


def car(x,y):
    gameDisplay.blit(carimg,(x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def message_display(text):
    largeText = pygame.font.SysFont('comicsansms', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    

    time.sleep(2)

    game_loop()
    

def quitgame():
    pygame.quit()
    quit()


def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects('You Crashed', largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("QUIT",550,450,100,50,red, bright_red,quitgame)
         




        pygame.display.update()
        clock.tick(19)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
        

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
            
##            if(action == "Play"):
##                game_loop()
##            elif(action == "Quit"):
##                pygame.quit()
##                quit()
        
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    
    smallText = pygame.font.SysFont('comicsansms',20)
    textSurf,textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), y+(h/2))
    gameDisplay.blit(textSurf,textRect)
        
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    
    
    

def paused():
    
    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects('Paused ', largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("QUIT",550,450,100,50,red, bright_red,quitgame)
         




        pygame.display.update()
        clock.tick(19)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects('A bit Racey', largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("QUIT",550,450,100,50,red, bright_red,quit)
        




        pygame.display.update()
        clock.tick(19)
        
        
        
    




        


    
def game_loop():
    
    global pause
    pygame.mixer.music.play(-1)
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    car_width = 100
    dodged = 0
    thing_startx=random.randrange(0, display_width)-100
    thing_starty=-6
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    
        
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused() 

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    

        x += x_change
        gameDisplay.fill(white)
        gameDisplay.blit(background, (0,0))
        




        thing(thing_startx,thing_starty)
        thing_starty += thing_speed
        
        car(x,y)
        thing_dodged(dodged)

        if x > display_width-car_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0+thing_width, display_width-thing_width)
            dodged += 1
            thing_speed += 1
            

            
        if y < thing_starty+thing_height:          
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width  < thing_startx + thing_width:                
                crash()
                
        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
