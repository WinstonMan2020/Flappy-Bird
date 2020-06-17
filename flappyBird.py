import pygame
import os
import random
import time

# Initilize
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Window width and height
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 800

# Bird width and height
BIRD_WIDTH, BIRD_HEIGHT = 80, 80

# Window title
WINDOW_TITLE = 'Flappy Bird'

# Theme song
pygame.mixer.music.load('themeSong.mp3')
pygame.mixer.music.play(-1)

# Load images
BACKGROUND = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/flappyBirdBG.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
BIRD = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/bird.png'), (BIRD_WIDTH, BIRD_HEIGHT))
GAME_OVER_SCREEN = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/gameoverScreen.png'), (500, 300))

wn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

def main():
    FPS = 65
    clock = pygame.time.Clock()
    running = True
    background_x = 0
    background_x2 = SCREEN_WIDTH
    
    bird_x = SCREEN_WIDTH / 2 - 20
    bird_y = 300
    bird_grav = 0
    title_screen = True

    score = 0

    gave_score_1 = False
    gave_score_2 = False
    gave_score_3 = False

    pipe_1_x = SCREEN_WIDTH
    pipe_11_y = random.randint(-350, 0)
    pipe_11_height = 400
    pipe_12_y = pipe_11_y + pipe_11_height + 150
    pipe_12_height = SCREEN_HEIGHT - 200 - pipe_12_y

    pipe_2_x = SCREEN_WIDTH + 200
    pipe_21_y = random.randint(-350, 0)
    pipe_21_height = 400
    pipe_22_y = pipe_21_y + pipe_21_height + 150
    pipe_22_height = SCREEN_HEIGHT - 200 - pipe_22_y

    pipe_3_x = SCREEN_WIDTH + 400
    pipe_31_y = random.randint(-350, 0)
    pipe_31_height = 400
    pipe_32_y = pipe_31_y + pipe_31_height + 150
    pipe_32_height = SCREEN_HEIGHT - 200 - pipe_32_y

    pipe_11_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_top.png'), (BIRD_WIDTH + 25, pipe_11_height))
    pipe_12_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_bottom.png'), (BIRD_WIDTH + 25, pipe_12_height))

    pipe_21_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_top.png'), (BIRD_WIDTH + 25, pipe_21_height))
    pipe_22_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_bottom.png'), (BIRD_WIDTH + 25, pipe_22_height))

    pipe_31_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_top.png'), (BIRD_WIDTH + 25, pipe_31_height))
    pipe_32_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_bottom.png'), (BIRD_WIDTH + 25, pipe_32_height))

    font = pygame.font.Font('flappyBirdFont.ttf', 50)
    score_font = pygame.font.Font('flappyBird2.ttf', 50)

    def redrawWindow():
        wn.blit(BACKGROUND, (background_x, 0))
        wn.blit(BACKGROUND, (background_x2, 0))

        wn.blit(pipe_11_img, (pipe_1_x, pipe_11_y))
        wn.blit(pipe_12_img, (pipe_1_x, pipe_12_y))

        wn.blit(pipe_21_img, (pipe_2_x, pipe_21_y))
        wn.blit(pipe_22_img, (pipe_2_x, pipe_22_y))

        wn.blit(pipe_31_img, (pipe_3_x, pipe_31_y))
        wn.blit(pipe_32_img, (pipe_3_x, pipe_32_y))

        if not title_screen:
            wn.blit(score_text, (round(SCREEN_WIDTH / 2), 100))
        
        wn.blit(BIRD, (round(bird_x), round(bird_y)))

        if title_screen:
            wn.blit(title_text, (round(SCREEN_WIDTH / 2 - 130), 100))

        pygame.display.update()
    
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if title_screen:
            if keys[pygame.K_RETURN]:
                title_screen = False
            
            title_text = font.render('Press Enter To Start', True, (0, 0, 0), None)

        if not title_screen:
            bird_y += bird_grav
            bird_grav += 0.4
            if keys[pygame.K_SPACE]:
                bird_grav = -4
            
            score_text = score_font.render(f'{score}', True, (0, 0, 0), None)
        
        if bird_y >= SCREEN_HEIGHT - 200:
            bird_y = SCREEN_HEIGHT - 200
            running = False
            print(f'You\'re final score was {score}.')
        
        if bird_y <= 0 - BIRD_HEIGHT:
            bird_y = 0 - BIRD_HEIGHT
            running = False
            print(f'You\'re final score was {score}.')

        # Move the background
        background_x -= 1
        background_x2 -= 1
        if background_x <= 0 - SCREEN_WIDTH:
            background_x = SCREEN_WIDTH
        
        if background_x2 <= 0 - SCREEN_WIDTH:
            background_x2 = SCREEN_WIDTH
        
        # Move the pipes IF not titlescreen
        if not title_screen:
            pipe_1_x -= 1
            pipe_2_x -= 1
            pipe_3_x -= 1

        # Check if pipe 1 is offscreen
        if pipe_1_x + BIRD_WIDTH + 25 <= 0:
            pipe_1_x = SCREEN_WIDTH + 200
            pipe_11_y = random.randint(-350, 0)
            pipe_11_height = 400
            pipe_12_y = pipe_11_y + pipe_11_height + 150
            pipe_12_height = SCREEN_HEIGHT - 200 - pipe_12_y + 25

            pipe_11_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_top.png'), (BIRD_WIDTH + 25, pipe_11_height))
            pipe_12_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_bottom.png'), (BIRD_WIDTH + 25, pipe_12_height))

            gave_score_1 = False
        
        # Check if pipe 2 is offscreen
        if pipe_2_x + BIRD_WIDTH + 25 <= 0:
            pipe_2_x = SCREEN_WIDTH + 200
            pipe_21_y = random.randint(-350, 0)
            pipe_21_height = 400
            pipe_22_y = pipe_21_y + pipe_21_height + 150
            pipe_22_height = SCREEN_HEIGHT - 200 - pipe_22_y + 25

            pipe_21_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_top.png'), (BIRD_WIDTH + 25, pipe_21_height))
            pipe_22_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_bottom.png'), (BIRD_WIDTH + 25, pipe_22_height))

            gave_score_2 = False

        # Check if pipe 3 is offscreen
        if pipe_3_x + BIRD_WIDTH + 25 <= 0:
            pipe_3_x = SCREEN_WIDTH + 200
            pipe_31_y = random.randint(-350, 0)
            pipe_31_height = 400
            pipe_32_y = pipe_31_y + pipe_31_height + 150
            pipe_32_height = SCREEN_HEIGHT - 200 - pipe_32_y + 25

            pipe_31_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_top.png'), (BIRD_WIDTH + 25, pipe_31_height))
            pipe_32_img = pygame.transform.scale(pygame.image.load(r'C:/Users/Joshua/OneDrive/VscodePrograms/MyPythonFolder/flappyBird/pipe_bottom.png'), (BIRD_WIDTH + 25, pipe_32_height))

            gave_score_3 = False

        # Check if colliding with pipe 1
        if bird_x + BIRD_WIDTH - 20 >= pipe_1_x and bird_x <= pipe_1_x + BIRD_WIDTH:
            if bird_y + BIRD_HEIGHT >= pipe_12_y + 20:
                running = False
                print(f'You\'re final score was {score}.')
                bird_y = pipe_12_y - BIRD_HEIGHT + 20
            elif bird_y <= pipe_11_y + pipe_11_height - 20:
                running = False
                print(f'You\'re final score was {score}.')
                bird_y = pipe_11_y + pipe_11_height - 20
            elif bird_x >= pipe_1_x + BIRD_WIDTH:
                if not gave_score_1:
                    score += 1
                    gave_score_1 = True
        
        # Check if colliding with pipe 2
        if bird_x + BIRD_WIDTH >= pipe_2_x and bird_x <= pipe_2_x + BIRD_WIDTH:
            if bird_y + BIRD_HEIGHT >= pipe_22_y + 20:
                running = False
                print(f'You\'re final score was {score}.')
                bird_y = pipe_22_y + 20
            elif bird_y <= pipe_21_y + pipe_21_height - 20:
                running = False
                print(f"You're final score was {score}.")
                bird_y = pipe_21_y + pipe_21_height - 20
            elif bird_x >= pipe_2_x + BIRD_WIDTH:
                if not gave_score_2:
                    score += 1
                    gave_score_2 = True
        
        # Check if colliding with pipe 3
        if bird_x + BIRD_WIDTH >= pipe_3_x and bird_x <= pipe_3_x + BIRD_WIDTH:
            if bird_y + BIRD_HEIGHT >= pipe_32_y + 20:
                running = False
                print(f'You\'re final score was {score}.')
                bird_y = pipe_32_y + 20
            elif bird_y <= pipe_31_y + pipe_31_height - 20:
                running = False
                print(f"You're final score was {score}.")
                bird_y = pipe_31_y + pipe_31_height - 20
            elif bird_x >= pipe_3_x + BIRD_WIDTH:
                if not gave_score_3:
                    score += 1
                    gave_score_3 = True

        redrawWindow()

main() #* An astonishing 237 lines of code!
# TODO Make more cool comments (this is one)
#? Cool comments
#! Cool comments
#* Cool comments
