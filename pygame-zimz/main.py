import pygame
import os
    # helps define the path the the images and assets
import random
from zimz_class import Zim

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
    # Sets a title for the game window
WHITE = (255, 255, 255)
    # RGB VALUE (RBG goes to 256)
FPS = 1
    # Ensures that your game is running, or refreshing a set number of times instead of running each loop at thousands of times per second
ZIM_WIDTH, ZIM_HEIGTH = 30, 65

PETER_IMAGE = pygame.image.load(os.path.join('Assets', 'Peter.png'))
    # os.path.join takes care of the file path, instead of slashes. Takes the file path Assets, to the desipeter file
PETER = pygame.transform.scale(PETER_IMAGE, (ZIM_WIDTH, ZIM_HEIGTH))
    # Transforms the image to a desipeter size, pass image and then size
    # Scale is then wrapped in the ROTATE, given the 90 degree command at the end. Things rotate COUNTERCLOCKWISE
AMY_IMAGE = pygame.image.load(os.path.join('Assets', 'Amy.png'))
AMY = pygame.transform.scale(AMY_IMAGE, (ZIM_WIDTH, ZIM_HEIGTH))

TOILET_IMAGE = pygame.image.load(os.path.join('Assets', 'toilet.png'))
TOILET_W_H = (30, 35)
TOILET_POS = (900, 500)
TOILET = pygame.transform.scale(TOILET_IMAGE, TOILET_W_H)

#Initializes and displays font/text at the top corner
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)

################## READOUT DISPLAY ##############
def display_readout(text_str):
    """"Calculates infomation to display"""

    text_surface = my_font.render(f"{text_str}", False, (0, 0, 0))

    return WIN.blit(text_surface, (0,0))


################## MOVES ZIM RANDOMLY ########################
def random_move(zimz):
    """"Moves each zim a small amount randomly each second
    WIDTH, HEIGHT = 1200, 700
    Drawing in pygame starts coordinates from the TOP LEFT at (0, 0)"""
    for zim in zimz:
        direction = random.choice(["x", "y"])
        up_down = random.choice(["-", "+"])

        if direction == "x" and up_down == "-":
            if zim.x > 0:
                zim.x = zim.x - random.randint(0,30)
        elif direction == "y" and up_down == "-":
            if zim.y > 0:
                zim.y = zim.y - random.randint(0,30)
        elif direction == "x" and up_down == "+":
            if zim.x < 1200:
                zim.x = zim.x + random.randint(0,30)
        elif direction == "y" and up_down == "+":
            if zim.y < 700:
                zim.y = zim.y + random.randint(0,30)
        else:
            pass

############## DRAW WINDOW DISPLAY FUNCTIONALITY #####################
def draw_window(peter, amy, toilet, TIME):
    # This allows all the "drawing" on the screen to be done outside of the main game loop
    # Defined parameters for what will be drawn on top of the screen
    WIN.fill(WHITE)
    WIN.blit(TOILET, (toilet.x, toilet.y))
    WIN.blit(PETER, (peter.x, peter.y))
    # blit it used to draw a 'surfaces', texts and images are surfaces
    # Drawing in pygame starts coordinates from the TOP LEFT at (0, 0)
    # The arguments passed within will now update to wherever the amy rectangle/zim is
    WIN.blit(AMY, (amy.x, amy.y))

    display_readout(TIME)

    pygame.display.update()
    # After things are changed, you must update the display to reflect changes 



############ MAIN ###############
def main():
    peter = pygame.Rect(700, 300, ZIM_HEIGTH, ZIM_WIDTH)
    # parameters are x, y coordinates and height and width
    amy = pygame.Rect(100, 300, ZIM_HEIGTH, ZIM_WIDTH)
    toilet = pygame.Rect(TOILET_POS, TOILET_W_H)
    TIME = 0


    clock = pygame.time.Clock()
    run = True
    while run:
        # Runs the while loop at the inputted frames persecond
        clock.tick(FPS)
        TIME += 1
        for event in pygame.event.get():
            # Inside here is where you check for the different events happening in pygame
            if event.type == pygame.QUIT:
                # This ensures that when you close the window, if closes the game instead of having to force-quit
                run = False

        random_move([peter, amy])
        # random_move(amy)

        draw_window(peter, amy, toilet, TIME)
        

    
    pygame.quit()


#############################################
if __name__ == "__main__":
    main()
    # Only runs the game if this file is run directly, not just if the file is imported 
