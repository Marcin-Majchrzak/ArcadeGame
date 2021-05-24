# importing modules
import pygame
import sys
import time
import random
import os

# Initialized resource path
BASE_DIR = os.path.dirname(__file__)
RESOURCE_PATH = os.path.join(BASE_DIR, '..', 'res')
IMAGE_PATH = os.path.join(RESOURCE_PATH, 'Images')

# Initializing pygame
pygame.init()

# Initializing the width and height of the window
display_height = 680
display_width = 1250

# Setting the title and dimensions of the window
pygame.display.set_caption('TEACH ENSTEIN!')
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Defining the clock to set the FPS rates
clock = pygame.time.Clock()


# Defining setText() function to display text to the screen which requires six parameters:
def setText(text, font_size, position, foreground_color, background_color=None, font_family="Times New Roman"):
    # Setting the font and related font features as per the parameters supplied.
    font = pygame.font.SysFont(font_family, font_size)
    text_to_display = font.render(text, 1, foreground_color, background_color)
    gameDisplay.blit(text_to_display, position)
    pygame.display.update()


# Defining functions for file operations.
def file_open_write(high_score):
    f = open(os.path.join(RESOURCE_PATH, 'File', 'high_score.txt'), 'w')
    f.write(high_score)
    return f


def file_open_read():
    f = open(os.path.join(RESOURCE_PATH, 'File', 'high_score.txt'), 'r')
    best_score = f.read()
    return f, best_score


def file_close(file):
    file.close()


# START GAME

def game_play():
    pygame.display.set_caption('TEACH EINSTEIN!')
    # Images section
    egg_images_raw = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', 'bomb.png']
    egg_images = [os.path.join(IMAGE_PATH, i) for i in egg_images_raw]
    basket = pygame.image.load(os.path.join(IMAGE_PATH, 'albert.png')).convert_alpha()

    # Initializing the speed variable which denotes the speed with which the images move.
    image_speed = 3

    # Intialiaing the score variable.
    score = 0

    # Pixels being moved by the basket under keystrokes (10 px)
    unit = 7

    # Initalizing lives
    lives = 3

    # Initalizing bombs
    bombs = 0

    # Initialising a boolean variable user_click to False to keep track of the user clicking any button in the main menu
    user_clicked = False

    # 1. Play now button
    play_clicked = False

    # 2. Instructions button
    instruction_clicked = False

    # 3. Best Scores button
    best_scores_clicked = False

    # Intialising game over variable.
    game_over = False

    # Main Menu with 3 Buttons

    # Setting background to the game window
    backgroundImage = pygame.image.load(os.path.join(IMAGE_PATH, 'background.jpg'))
    gameDisplay.blit(backgroundImage, (0, 0))

    # The Title
    setText("TEACH EINSTEIN!", 100, (175, 0), (180, 180, 180,), None, "Cooper Black")

    start = display_height + 40
    end = 299
    value = 0

    # Play Button
    pygame.draw.rect(gameDisplay, (51, 51, 51), (display_width / 2 - 300, 260, 230, 100))
    setText("Play !", 50, (330, 260), (255, 255, 255), None, "Cooper Black")
    setText("Bombs", 30, (450, 320), (170, 0, 0), None, "Cooper Black")

    # Play2 Button
    pygame.draw.rect(gameDisplay, (51, 51, 51), (display_width / 2 +100 , 260, 230, 100))
    setText("Play !", 50, (730, 260), (255, 255, 255), None, "Cooper Black")
    setText("NO Bombs", 30, (795, 320), (170, 0, 0), None, "Cooper Black")

    # Instructions Button
    pygame.draw.rect(gameDisplay, (51, 51, 51), (display_width / 2 - 200, 400, 440, 100))
    setText("Instructions", 65, (440, 410), (255, 255, 255), None, "Cooper Black")

    # Best Scores Button
    pygame.draw.rect(gameDisplay, (51, 51, 51), (display_width / 2 - 200, 540, 440, 100))
    setText("Best Scores", 70, (450, 540), (255, 255, 255), None, "Cooper Black")

    pygame.display.update()

    while not user_clicked:

        # (Event Loop) Keyboard and Mouse events (Checking whether the user had clicked any button)

        for event in pygame.event.get():

            # Retrieving the mouse co-ordinates (Returns a list with 2 elements i,e X and Y co-ordinates)

            mouse_cord = pygame.mouse.get_pos()

            # Checking whether the close button was tapped and if so terminate the program!
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Checking  the mouse is within  button 'PLAY'
            if display_width / 2 - 300 + 260 > mouse_cord[0] > display_width / 2 - 300 and 360 > mouse_cord[1] > 260:

                pygame.draw.rect(gameDisplay, (100, 100, 100), (display_width / 2 - 300, 260, 230, 100))
                setText("Play !", 60, (330, 260), (255, 255, 255), None, "Cooper Black")
                setText("Bombs", 30, (450, 320), (170, 0, 0), None, "Cooper Black")

                # Checking whether the user has clicked the play button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    user_clicked = True
                    play_clicked = True
                    bombs = 9

            else:

                pygame.draw.rect(gameDisplay, (51, 51, 51), (display_width / 2 - 300, 260, 230, 100))
                setText("Play !", 60, (330, 260), (255, 255, 255), None, "Cooper Black")
                setText("Bombs", 30, (450, 320), (170, 0, 0), None, "Cooper Black")


            # Checking  the mouse is within  button 'PLAY2'
            if display_width / 2 + 100 + 260 > mouse_cord[0] > display_width / 2 + 100 and 360 > mouse_cord[
                    1] > 260:

                pygame.draw.rect(gameDisplay, (100, 100, 100), (display_width / 2 + 100, 260, 230, 100))
                setText("Play !", 60, (730, 260), (255, 255, 255), None, "Cooper Black")
                setText("NO Bombs", 30, (795, 320), (170, 0, 0), None, "Cooper Black")

                #Checking whether the user has clicked the play button
                if event.type == pygame.MOUSEBUTTONDOWN:
                        user_clicked = True
                        play_clicked = True
                        bombs = 7

            else:

                pygame.draw.rect(gameDisplay, (51, 51, 51), (display_width / 2 + 100, 260, 230, 100))
                setText("Play !", 60, (730, 260), (255, 255, 255), None, "Cooper Black")
                setText("NO Bombs", 30, (795, 320), (170, 0, 0), None, "Cooper Black")

            # Checking  the mouse is within  button 'INSTRUCTIONS'
            if display_width / 2 - 200 + 440 > mouse_cord[0] > display_width / 2 - 200 and 500 > mouse_cord[1] > 400:

                pygame.draw.rect(gameDisplay, (100, 100, 100), (display_width / 2 - 200, 400, 440, 100))
                setText("Instructions", 65, (440, 410), (255, 255, 255), None, "Cooper Black")

                # Checking whether the user has clicked the Instructions button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    user_clicked = True
                    instruction_clicked = True
            else:

                pygame.draw.rect(gameDisplay, (51, 51, 51), (display_width / 2 - 200, 400, 440, 100))
                setText("Instructions", 65, (440, 410), (255, 255, 255), None, "Cooper Black")

            # Checking  the mouse is within  button 'BEST SCORES'
            if display_width / 2 - 200 + 440 > mouse_cord[0] > display_width / 2 - 200 and 640 > mouse_cord[1] > 540:

                pygame.draw.rect(gameDisplay, (100, 100, 100), (display_width / 2 - 200, 540, 440, 100))
                setText("Best Scores", 70, (450, 540), (255, 255, 255), None, "Cooper Black")

                # Checking whether the user has clicked the Best scores button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    user_clicked = True
                    best_scores_clicked = True

            else:

                pygame.draw.rect(gameDisplay, (51, 51, 51), (display_width / 2 - 200, 540, 440, 100))
                setText("Best Scores", 70, (450, 540), (255, 255, 255), None, "Cooper Black")

        clock.tick(60)






if __name__ == '__main__':
    game_play()