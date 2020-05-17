import pygame as pg
import sys
import time
import random
pg.init()
screen_width=1000
screen_height=1000
screen=pg.display.set_mode((screen_width,screen_height)) #width,height
pg.display.set_caption('Iconic')

icon=pg.image.load('C:/Users/gauba/Desktop/appls.png')
pg.display.set_icon(icon)
FPS = 20
block_size=20
appleThickness=30
clock =pg.time.Clock()

smallfont=pg.font.SysFont("comicsansms",30)
medfont=pg.font.SysFont("comicsansms",50)
largefont=pg.font.SysFont("comicsansms",80)

snake_img=pg.image.load('snakehead.png') #C:/Users/gauba/Desktop/
apple_img=pg.image.load('appls.png')
direction="right"

def pause():
    paused=True
    while paused:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_c:
                    paused=False
                elif event.key==pg.K_q:
                    pg.quit()
                    quit()
        screen.fill((255,0,0))
        message_to_screen("Paused",(0,0,0),-100,"large")
        message_to_screen("Press C to continue or Q to quit",(0,0,0),25)
        pg.display.update()
        clock.tick(5)

def score(score):
    text=smallfont.render("Score: "+str(score),True, (0,0,0))
    screen.blit(text, [0,0])

def randApplegen():
    randAppleX = round(random.randrange(0, screen_width - appleThickness) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, screen_height - appleThickness) / 10.0) * 10.0
    return randAppleX, randAppleY

randAppleX, randAppleY = randApplegen()

def game_intro():
    intro=True
    while intro:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_c:
                    intro=False
                if event.key==pg.K_q:
                    pg.quit()
                    quit()
        screen.fill((255,0,0))
        message_to_screen("Welcome to Iconic", (0,0,0),-100,"large")
        message_to_screen("The objective of the game is toe eat the apples",(0,0,0),-30,"small")
        message_to_screen("The more apples you eat, the longer you get",(0,0,0),10,"small")
        message_to_screen("If you run into yourself or into the edge, you die",(0,0,0),50,"small")
        message_to_screen("Press C to pay or Q to quit", (0, 0, 0), 180, "small")
        pg.display.update()
        clock.tick(FPS/2)

def snake(block_size,snakelist):
    if direction=="right":
        head=pg.transform.rotate(snake_img,270)
    if direction == "left":
        head = pg.transform.rotate(snake_img, 90)
    if direction=="up":
        head=snake_img
    if direction=="down":
        head=pg.transform.rotate(snake_img,180)
    screen.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        screen.fill((0, 0, 0), rect=[XnY[0], XnY[1], int(block_size), int(block_size)])

def text_objects(text,color,size):
    if size=="small":
        textSurface=smallfont.render(text,True,color)
    if size=="med":
        textSurface=medfont.render(text,True,color)
    if size=="large":
        textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size="small"): #y_displace is displacement from the center of screen width
    #screen_text=font.render(msg,True,color)
    #screen.blit(screen_text,[int(screen_width/2),int(screen_height/2)])
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = int(screen_width/2), int(screen_height/2)+y_displace
    screen.blit(textSurf,textRect)

def game_loop():
    global direction
    direction="right"
    game_exit = False
    game_over=False
    dx = 10
    dy = 0
    move_x = screen_width / 2
    move_y = screen_height / 2
    randAppleX, randAppleY = randApplegen()
    snakelist = []
    snakelength=1
    while not game_exit:
        while game_over == True:
            screen.fill((255, 0, 0))
            message_to_screen("Game over", (0, 0, 0), -50,size="large")
            message_to_screen("Press C to continue playing or Q to Quit", (0,0,0),50,size="med")
            pg.display.update()
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    game_exit=True
                    game_over=False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pg.K_c:
                        game_loop()
        for event in pg.event.get():
            if event.type==pg.QUIT:
                game_exit=True
            if event.type==pg.KEYDOWN: #to check if key was pressed
                if event.key==pg.K_LEFT: #specifying which key was pressed
                    dx=-block_size
                    dy=0
                    direction="left"
                elif event.key==pg.K_RIGHT:
                    dx=block_size
                    dy=0
                    direction="right"
                elif event.key==pg.K_UP:
                    dy=-block_size
                    dx=0
                    direction="up"
                elif event.key==pg.K_DOWN:
                    dy=block_size
                    dx=0
                    direction="down"
                elif event.key==pg.K_p:
                    pause()
            #if event.type==pg.KEYUP:
             #   if event.key==pg.K_LEFT or event.key==pg.K_RIGHT:
              #     dx=0
            #if event.key == pg.K_UP or event.key == pg.K_RIGHT:
             #          dy = 0
        if move_x>=screen_width or move_x<0 or move_y>=screen_height or move_y<0:
            game_over=True
                   #someting is classified as event only if there is change in state
                    #that's why the snake does not continuously move while you keep holding arrow key
        move_x+=dx #updating x value after every frame
        move_y+=dy #updating y value after every frame
        screen.fill((255,0,0))
        #pg.draw.rect(screen,(0,0,0),[300,300,10,10]) #display area, color, first two coordinates for starting point, width and height
        #another way to draw rectangle is to pass 'rect' parameter to fill; faster for image processing
        #screen.fill((0,255,0), rect=[int(randAppleX), int(randAppleY),appleThickness, appleThickness])
        screen.blit((apple_img), (int(randAppleX),int(randAppleY)))
        snakehead=[]
        snakehead.append(move_x)
        snakehead.append(move_y)
        snakelist.append(snakehead)
        if len(snakelist)>snakelength:
            del snakelist[0]
        for body in snakelist[:-1]: #till last element
            if body==snakehead:
                game_over=True

        snake(int(block_size),snakelist)
        score(snakelength-1)
        pg.display.update()
        #if move_x==int(randAppleX) and move_y==int(randAppleY):
            #randAppleX = round(random.randrange(0, screen_width - block_size)) / 10.0) * 10.0
            #randAppleY = round(random.randrange(0, screen_height - block_size)) / 10.0) * 10.0
            #snakelength+=1

        if move_x > randAppleX and move_x < randAppleX + appleThickness or move_x + block_size > randAppleX and move_x + block_size < randAppleX + appleThickness:
            if move_y > randAppleY and move_y < randAppleY + appleThickness or move_y + block_size > randAppleY and move_y + block_size < randAppleY + appleThickness:
                randAppleX, randAppleY = randApplegen()
                snakelength+=1

        clock.tick(FPS) #defines the total number of times the frame (while loop) will run in a second
    pg.quit()
    quit()
game_intro()
game_loop()