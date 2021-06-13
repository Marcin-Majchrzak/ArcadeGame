# importing modules
import pygame
import sys
import time
import random
import os

# Initialized resource path
BASE_DIR = os.path.dirname(__file__)
RESOURCE_PATH = os.path.join(BASE_DIR, 'ResourceFiles')
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

# Instructions window
    if instruction_clicked:
        instruction_window = pygame.display.set_mode((display_width, display_height))

        pygame.display.set_caption('Instructions')

        instruction_clock = pygame.time.Clock()

        instruction_window.blit(backgroundImage, (0, 0))

        setText("Instructions", 120, (display_width / 2 - 360, 50), (180, 180, 180,), None, "Cooper Black")

        setText("1. Select a game mode- 'Bomb' or 'NO Bomb'", 45, (40, 220), (255, 255, 255))

        setText("2. Use left and right arrow keys to move the Einstein.", 45, (40, 290), (255, 255, 255))

        setText("3. Teach Einstein  as many math symbol as you can.", 45, (40, 360), (255, 255, 255))

        setText("4. Don't let the symbols touch the ground", 45, (40, 430), (255, 255, 255))

        setText("5. Watch out for bombs (division by zero)", 45, (40, 500),
                (255, 255, 255))

        pygame.draw.rect(instruction_window, (51, 51, 51), (display_width / 2 - 120, 560, 160, 80))

        setText("Back", 50, (display_width / 2 - 100, 570), (255, 255, 255), None, "Cooper Black")
    while instruction_clicked:

        for event in pygame.event.get():

            mouse = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if display_width / 2 + 45 > mouse[0] > display_width / 2 - 120 and 640 > mouse[1] > 560:

                pygame.draw.rect(instruction_window, (100, 100, 100), (display_width / 2 - 120, 560, 160, 80))

                setText("Back", 50, (display_width / 2 - 100, 570), (255, 255, 255), None, "Cooper Black")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    instruction_clicked = False
                    game_play()


            else:

                pygame.draw.rect(instruction_window, (70, 70, 70), (display_width / 2 - 120, 560, 160, 80))

                setText("Back", 50, (display_width / 2 - 100, 570), (255, 255, 255), None, "Cooper Black")

        pygame.display.update()

        instruction_clock.tick(30)

    # High Score window
    if best_scores_clicked:
        score_window = pygame.display.set_mode((display_width, display_height))

        pygame.display.set_caption('High Score')

        score_clock = pygame.time.Clock()

        score_window.blit(backgroundImage, (0, 0))

        setText("High Score", 120, (display_width / 2 - 300, 50), (180, 180, 180), None, "Cooper Black")

        file_object, high_score = file_open_read()

        setText(high_score, 150, (display_width / 2 - 30, display_height / 2 - 70), (255, 255, 255))

        pygame.draw.rect(score_window, (50, 50, 50), (display_width / 2 - 130, display_height / 2 + 160, 300, 130))

        setText("Go Back", 70, (display_width / 2 - 130, display_height / 2 + 180), (255, 255, 255), None,
                "Cooper Black")

        file_close(file_object)
    while best_scores_clicked:

        for event in pygame.event.get():

            mouse_position = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if display_width / 2 + 170 > mouse_position[0] > display_width / 2 - 130 and display_height / 2 + 290 > \
                    mouse_position[1] > display_height / 2 + 160:

                pygame.draw.rect(score_window, (100, 100, 100),
                                 (display_width / 2 - 130, display_height / 2 + 160, 300, 130))

                setText("Go Back", 70, (display_width / 2 - 130, display_height / 2 + 180), (255, 255, 255), None,
                        "Cooper Black")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    best_scores_clicked = False
                    game_play()

            else:

                pygame.draw.rect(score_window, (50, 50, 50),
                                 (display_width / 2 - 130, display_height / 2 + 160, 300, 130))

                setText("Go Back", 70, (display_width / 2 - 130, display_height / 2 + 180), (255, 255, 255), None,
                        "Cooper Black")

        pygame.display.update()

        score_clock.tick(30)

    # X and Y co-ordinates of the basket.
    basket_x = display_width / 2 - 200
    basket_y = display_height - 270

    # For changing the X co-ordinate of the basket.
    x_change = 0

    # Random positions for eggs
    x = random.randint(0, display_width - 250)
    y = -150

    # Randomly loading egg images
    random_images = egg_images[random.randint(0, bombs)]
    random_eggs = pygame.image.load(random_images).convert_alpha()

    # Game in action !!!
    while play_clicked:

        # Exit to main menu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                play_clicked = False
                game_play()

        # New game window is created on clicking the play button with the same dimensions.
        play_window = pygame.display.set_mode((1250, 680))
        pygame.display.set_caption('Play')
        play_window.blit(backgroundImage, (0, 0))
        play_clock = pygame.time.Clock()
        play_window.blit(random_eggs, (x, y))

        # Horizontal line carrying the basket.
        pygame.draw.line(play_window, (0, 0, 0), (0, display_height - 20), (display_width, display_height - 20))

        # Color beneath the line.
        pygame.draw.rect(play_window, (0, 0, 0), (0, display_height - 18, display_width, display_height))

        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    x_change = unit
                    basket = pygame.image.load(os.path.join(IMAGE_PATH, 'albert2.png')).convert_alpha()


                elif event.key == pygame.K_LEFT:
                    x_change = -unit
                    basket = pygame.image.load(os.path.join(IMAGE_PATH, 'albert.png')).convert_alpha()

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT:
                    x_change = 0


                elif event.key == pygame.K_LEFT:
                    x_change = 0

        basket_x += x_change
        y += image_speed

        # Placing the Basket in position
        play_window.blit(basket, (basket_x, basket_y))

        # Placing score and lives on the game window.
        setText("Your Score:" + str(score), 40, (0, 0), (255, 255, 255), (50, 50, 50))
        setText("Lives:" + str(lives), 40, (1130, 0), (255, 255, 255), (50, 50, 50))

        # Checking egg and basket crossover.
        if y + 80 >= basket_y and y + 80 <= basket_y + 15:

            if x >= basket_x - 80 and x + 80 <= basket_x + display_width / 2 - 300:

                if (random_images == egg_images[9] or random_images == egg_images[8]):
                    lives -= 1

                    pygame.mixer.music.load(os.path.join(RESOURCE_PATH, 'Songs', 'fail.mp3'))
                    pygame.mixer.music.play()

                    x = random.randint(0, display_width - 250)
                    y = -150
                    random_images = egg_images[random.randint(0, bombs)]
                    random_eggs = pygame.image.load(random_images).convert_alpha()



                elif (random_images != egg_images[9] and random_images != egg_images[8]):
                    # Incrementing the score appropriately.
                    score += 1

                    pygame.mixer.music.load(os.path.join(RESOURCE_PATH, 'Songs', 'ok.mp3'))
                    pygame.mixer.music.play()

                    x = random.randint(0, display_width - 250)
                    y = -150
                    random_images = egg_images[random.randint(0, bombs)]
                    random_eggs = pygame.image.load(random_images).convert_alpha()

                # Increasing the speed in which the basket moves both the directions.
                if unit != 20:
                    unit += 0.25

                # Increasing the speed in which the images moves down.
                if image_speed != 20:
                    image_speed += 0.2

        # Checking whether the egg image had crossed the floor.
        if y >= display_height + 50:
            if (random_images != egg_images[9] and random_images != egg_images[8]):
                lives -= 1

                pygame.mixer.music.load(os.path.join(RESOURCE_PATH, 'Songs', 'fail.mp3'))
                pygame.mixer.music.play()

            # Random positions for eggs
            x = random.randint(0, display_width - 250)
            y = -150

            # Randomly loading Egg images
            random_images = egg_images[random.randint(0, bombs)]
            random_eggs = pygame.image.load(random_images).convert_alpha()

        # Restricting the basket within the width of the Game window
        if basket_x <= 0:
            basket_x = 0

        elif basket_x >= display_width - 300:
            basket_x = display_width - 300

        pygame.display.update()
        play_clock.tick(60)

        # If all lives are lost
        if lives == 0:

            setText("Lives:" + str(lives), 40, (1130, 0), (255, 255, 255), (50, 50, 50))

            # Checking whether the current score is greater than the best score.
            file, current_best_score = file_open_read()
            file_close(file)
            if score > int(current_best_score):
                file = file_open_write(str(score))
                file_close(file)

            pygame.display.update()
            time.sleep(1)

            game_over = True
            play_clicked = False

    # Game Over window
    if game_over:
        game_over_window = pygame.display.set_mode((display_width, display_height))

        pygame.display.set_caption("Game Over!")
        game_over_clock = pygame.time.Clock()
        game_over_window.blit(backgroundImage, (0, 0))

        pygame.mixer.music.load(os.path.join(RESOURCE_PATH, 'Songs', 'gameOver.wav'))
        pygame.mixer.music.play()

        setText("G", 90, (180, 250), (255, 255, 255), None, "Elephant")
        pygame.time.wait(100)
        setText("A", 90, (270, 250), (255, 255, 255), None, "Elephant")
        pygame.time.wait(100)
        setText("M", 90, (360, 250), (255, 255, 255), None, "Elephant")
        pygame.time.wait(100)
        setText("E", 90, (460, 250), (255, 255, 255), None, "Elephant")
        pygame.time.wait(100)
        setText("O", 90, (630, 250), (255, 255, 255), None, "Elephant")
        pygame.time.wait(100)
        setText("V", 90, (720, 250), (255, 255, 255), None, "Elephant")
        pygame.time.wait(100)
        setText("E", 90, (810, 250), (255, 255, 255), None, "Elephant")
        pygame.time.wait(100)
        setText("R", 90, (900, 250), (255, 255, 255), None, "Elephant")
        pygame.time.wait(100)

        setText("Your Score:" + str(score), 100, (display_width / 2 - 280, 120), (180, 180, 180), None)
        pygame.draw.rect(game_over_window, (70, 70, 70), (display_width / 2 - 200, 420, 420, 90))
        setText("Back to Main Menu", 40, (display_width / 2 - 190, 430), (255, 255, 255), None, "Cooper Black")
        pygame.draw.rect(game_over_window, (70, 70, 70), (display_width / 2 - 110, 540, 180, 95))
        setText("Credits", 45, (display_width / 2 - 110, 550), (255, 255, 255), None, "Cooper Black")

    while game_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            mouse = pygame.mouse.get_pos()

            if display_width / 2 + 220 > mouse[0] > display_width / 2 - 200 and 510 > mouse[1] > 420:
                pygame.draw.rect(game_over_window, (100, 100, 100), (display_width / 2 - 200, 420, 420, 90))
                setText("Back to Main Menu", 40, (display_width / 2 - 180, 440), (255, 255, 255), None, "Cooper Black")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_over = False
                    game_play()

            else:
                pygame.draw.rect(game_over_window, (70, 70, 70), (display_width / 2 - 200, 420, 420, 90))
                setText("Back to Main Menu", 40, (display_width / 2 - 180, 440), (255, 255, 255), None, "Cooper Black")

            if display_width / 2 + 70 > mouse[0] > display_width / 2 - 110 and 635 > mouse[1] > 540:
                pygame.draw.rect(game_over_window, (100, 100, 100), (display_width / 2 - 110, 540, 180, 95))
                setText("Credits", 45, (display_width / 2 - 105, 560), (255, 255, 255), None, "Cooper Black")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    credit_clicked = True
                    game_over = False

            else:
                pygame.draw.rect(game_over_window, (70, 70, 70), (display_width / 2 - 110, 540, 180, 95))
                setText("Credits", 45, (display_width / 2 - 105, 560), (255, 255, 255), None, "Cooper Black")

        pygame.display.update()
        game_over_clock.tick(60)

    if credit_clicked:
        credits_window = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("CREDITS")
        credits_clock = pygame.time.Clock()
        credits_window.blit(backgroundImage, (0, 0))
        setText("CREDITS", 120, (display_width / 2 - 300, 20), (180, 180, 180), None, "Cooper Black")
        setText("Developer:", 80, (display_width / 2 - 235, display_height / 2 - 170), (255, 255, 255), None,
                "Cooper Black")
        setText("Marcin", 60, (display_width / 2 - 130, display_height / 2 - 50), (255, 255, 255), None, "Cooper Black")
        setText("Majchrzak", 60, (display_height / 2 + 110, display_height / 2 + 30), (255, 255, 255), None,
                "Cooper Black")

        pygame.draw.rect(credits_window, (70, 70, 70), (display_width / 2 - 230, display_height / 2 + 200, 410, 120))
        setText("Play Again!", 60, (display_width / 2 - 205, display_height / 2 + 210), (0, 160, 0), None,
                "Cooper Black")

    while credit_clicked:

        for event in pygame.event.get():

            mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if display_width / 2 + 190 > mouse_pos[0] > display_width / 2 - 230 and display_height / 2 + 300 > \
                    mouse_pos[1] > display_height / 2 + 200:

                pygame.draw.rect(credits_window, (100, 100, 100),
                                 (display_width / 2 - 230, display_height / 2 + 200, 410, 120))

                setText("Play Again!", 60, (display_width / 2 - 195, display_height / 2 + 220), (255, 255, 255), None,
                        "Cooper Black")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    credit_clicked = False
                    game_play()

            else:

                pygame.draw.rect(credits_window, (70, 70, 70),
                                 (display_width / 2 - 230, display_height / 2 + 200, 410, 120))

                setText("Play Again!", 60, (display_width / 2 - 195, display_height / 2 + 220), (255, 255, 255), None,
                        "Cooper Black")

        pygame.display.update()

        credits_clock.tick(30)





if __name__ == '__main__':
    game_play()