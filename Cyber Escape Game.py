# imports needed libraries
import pygame,os, random
from pygame import mixer

#initialise pygame
pygame.init()

# create screen and define width and height (s stands for screen)
screen_width = 1520
screen_height = 950
window = pygame.display.set_mode((screen_width, screen_height))

# creates framerates and sets variables for each screen in the fame
fps = 15
clock = pygame.time.Clock()
title_screen = True
main_game = False

#sets caption for game window
pygame.display.set_caption('Cyber Escape')

while title_screen == True:

    # loads all needed images and audio files for the title page
    titlepagebackground = pygame.image.load(os.path.join('images', 'titlepagebg.png')).convert_alpha()
    return_key = pygame.image.load(os.path.join('images', 'return_key.png')).convert_alpha()
    return_character_key = pygame.image.load(os.path.join('images', 'return_character.png')).convert_alpha()
    controls = pygame.image.load(os.path.join('images', 'controls_selected.png')).convert_alpha()
    begin = pygame.image.load(os.path.join('images', 'begin_selected.png')).convert_alpha()
    character = pygame.image.load(os.path.join('images', 'character_selected.png')).convert_alpha()
    exit = pygame.image.load(os.path.join('images', 'exit_selected.png')).convert_alpha()
    controlspagewindow = pygame.image.load(os.path.join('images', 'controlspage.png')).convert_alpha()
    ninja_selected = pygame.image.load(os.path.join('images', "ninja_selected.png")).convert_alpha()
    santa_selected = pygame.image.load(os.path.join('images', "santa_selected.png")).convert_alpha()
    robot_selected = pygame.image.load(os.path.join('images', "robot_selected.png")).convert_alpha()
    ninja_chosen = pygame.image.load(os.path.join('images', "ninja_chosen.png")).convert_alpha()
    santa_chosen = pygame.image.load(os.path.join('images', "santa_chosen.png")).convert_alpha()
    robot_chosen = pygame.image.load(os.path.join('images', "robot_chosen.png")).convert_alpha()
    lives_selected = pygame.image.load(os.path.join('images', "life_powerup_selected.png")).convert_alpha()
    gun_selected = pygame.image.load(os.path.join('images', "gun_powerup_selected.png")).convert_alpha()
    fuel_selected = pygame.image.load(os.path.join('images', "score_powerup_selected.png")).convert_alpha()
    lives_chosen = pygame.image.load(os.path.join('images', "lives_chosen.png")).convert_alpha()
    gun_chosen = pygame.image.load(os.path.join('images', "gun_chosen.png")).convert_alpha()
    fuel_chosen = pygame.image.load(os.path.join('images', "fuel_chosen.png")).convert_alpha()
    item_keys = pygame.image.load(os.path.join('images', "item_selection_keys.png")).convert_alpha()
    show_30_s = pygame.image.load(os.path.join('images', "show_30_s.png")).convert_alpha()
    loading = pygame.image.load(os.path.join('images', "loading_screen.png")).convert_alpha()
    escape_button = pygame.image.load(os.path.join('images', "escape_button.png")).convert_alpha()
    mixer.music.load('title_screen_music.wav')
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    menu_select = mixer.Sound('menu_select.wav')
    menu_move = mixer.Sound('menu_move.wav')


    # defines the values of needed integer variables for the title page
    user_selection = 1
    character_selection = 2
    character_selected = 2
    item_selection = 2
    item_selected = 2

    # Defines a function for the title page that is used to draw images to the screen
    def titlepage():
        window.blit(titlepagebackground, (0, 0))

        # shows what title page element is currently selected (1: Begin, 2: Characters, 3: Controls, 4: Exit)
        if user_selection == 1:
            window.blit(begin, (0, 0))
            window.blit(return_key, (0, 0))
        if user_selection == 2:
            window.blit(character, (0, 0))
            window.blit(return_key, (0, 0))
        if user_selection == 3:
            window.blit(controls, (0, 0))
            window.blit(return_key, (0, 0))
        if user_selection == 4:
            window.blit(exit, (0, 0))
            window.blit(return_key, (0, 0))

        # displays the characters screen when RETURN is pressed
        if user_selection == 5:
            if character_selection == 1:
                window.blit(robot_selected, (0, 0))
                window.blit(return_character_key, (0, 0))
            if character_selection == 2:
                window.blit(ninja_selected, (0, 0))
                window.blit(return_character_key, (0, 0))
            if character_selection == 3:
                window.blit(santa_selected, (0, 0))
                window.blit(return_character_key, (0, 0))

            if character_selected == 1:
                window.blit(robot_chosen, (0, 0))
            if character_selected == 2:
                window.blit(ninja_chosen, (0, 0))
            if character_selected == 3:
                window.blit(santa_chosen, (0, 0))

        # displays the contols screen when RETURN is pressed
        if user_selection == 6:
            window.blit(controlspagewindow, (0, 0))

        # displays the powerup selection screen when RETURN is pressed
        if user_selection == 7:
            window.blit(escape_button, (0, 0))
            if item_selection == 1:
                window.blit(gun_selected, (0, 0))
                window.blit(show_30_s, (0, 0))
                window.blit(item_keys, (0, 0))
            if item_selection == 2:
                window.blit(lives_selected, (0, 0))
                window.blit(show_30_s, (0, 0))
                window.blit(item_keys, (0, 0))
            if item_selection == 3:
                window.blit(fuel_selected, (0, 0))
                window.blit(show_30_s, (0, 0))
                window.blit(item_keys, (0, 0))

            if item_selected == 1:
                window.blit(gun_chosen, (0, 0))
            if item_selected == 2:
                window.blit(lives_chosen, (0, 0))
            if item_selected == 3:
                window.blit(fuel_chosen, (0, 0))
        if user_selection == 8:
            window.blit(loading, (0, 0))
        pygame.display.update()

    while title_screen == True:
        #sets fps to 15
        clock.tick(fps)

        # This is used to identify if keys are pressed
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

            #code for the down key in title screen
            if keys[pygame.K_DOWN]:
                if user_selection == 1 or user_selection == 2 or user_selection == 3:
                    menu_move.play()
                    user_selection += 1

            #code for the up key in title screen
            if keys[pygame.K_UP]:
                if user_selection == 2 or user_selection == 3 or user_selection == 4:
                    menu_move.play()
                    user_selection -= 1

            # code for RETURN in title screen
            if keys[pygame.K_RETURN]:
                if user_selection == 1:
                    user_selection += 6
                    menu_select.play()
                if user_selection == 2:
                    user_selection = 5
                    menu_select.play()
                if user_selection == 3:
                    user_selection = 6
                    menu_select.play()
                if user_selection == 4:
                    menu_select.play()
                    pygame.quit()
                    quit()
                if user_selection == 5:
                    if character_selection == 1:
                        character_selected = 1
                    if character_selection == 2:
                        character_selected = 2
                    if character_selection == 3:
                        character_selected = 3
                if user_selection == 7:
                    if item_selection == 1:
                        item_selected = 1
                    if item_selection == 2:
                        item_selected = 2
                    if item_selection == 3:
                        item_selected = 3

            #code for the spacebar in the powerup
            if keys[pygame.K_SPACE]:
                if user_selection == 7:
                    pygame.mixer.music.fadeout(2000)
                    user_selection = 8
                    title_screen = False
                    main_game = True
            if keys[pygame.K_LEFT]:
                if user_selection == 5:
                    if character_selection == 2 or character_selection == 3:
                        character_selection -= 1
                if user_selection == 7:
                    if item_selection == 2 or item_selection == 3:
                        item_selection -= 1

            if keys[pygame.K_RIGHT]:
                if user_selection == 5:
                     if character_selection == 1 or character_selection == 2:
                         character_selection += 1
                if user_selection == 7:
                    if item_selection == 1 or item_selection == 2:
                        item_selection += 1

            #code for the escape button in the controls, characters or powerup screen
            if keys[pygame.K_ESCAPE]:
                if user_selection == 6:
                    user_selection = 3
                if user_selection == 5:
                    user_selection = 2
                if user_selection == 7:
                    user_selection = 1
        titlepage()

    def draw_Main_Game():

        #globals the variables that need to be referenced in the drawring of the main game
        global walkcount
        global lives
        global zombiex
        global girlzombiex
        global batx
        global scorex
        global gun
        global character_powerup
        global down
        global vel
        global vel2
        global add_vel
        global hitbox_y
        global kunai_hitbox
        global fireball_hitbox
        global right
        global jump
        global itemjump
        global y

        # Makes an invisible screen to hide hitbox rectangles surrounding player and obstacles
        transparent_rectanlge = pygame.Surface((1520,950), pygame.SRCALPHA)

        # Displays the game background and floor
        window.blit(bg, (0, 0))
        window.blit(floor, (bgx,0))
        window.blit(floor, (bgx2, 0))

        # Draws obstacles walking animation
        window.blit(zombieWalk[walkcount // 3], (zombiex, 620))
        window.blit(batFly[walkcount // 3], (batx, 600))
        window.blit(girlzombieWalk[walkcount // 3], (girlzombiex, 610))

        # Creates obstacle hitboxes
        zombie_hitbox = pygame.draw.rect(transparent_rectanlge, (85, 38, 132,50), (zombiex, 628, 70, height - 20), 2)
        bat_hitbox = pygame.draw.rect(transparent_rectanlge, (85, 38, 132, 50), (batx+30, 625, 75, height - 135), 2)
        girlzombie_hitbox = pygame.draw.rect(transparent_rectanlge, (85, 38, 132, 50), (girlzombiex+10, 635, 70, height - 20), 2)

        if walkcount + 1 >= 27:
            walkcount = 0

        # code for player sliding
        if down:
            window.blit(slide, (x, slidey))

            # creates slide hitboxes for player
            if character_selected == 1:
                slide_hitbox = pygame.draw.rect(transparent_rectanlge, (85, 38, 132,50), (x+10, slidey+5, 115, 110), 2)
            if character_selected == 2:
                slide_hitbox = pygame.draw.rect(transparent_rectanlge, (85, 38, 132,50), (x, slidey, 120, 100), 2)
            if character_selected == 3:
                slide_hitbox = pygame.draw.rect(transparent_rectanlge, (85, 38, 132,50), (x, slidey, 130, 100), 2)

            # generates collision between sliding players and obstacles
            if slide_hitbox.colliderect(zombie_hitbox):
                window.blit(smoke, (zombiex - 80, 400))
                zombiex = -150
                lives -= 1
                if lives > 0:
                    life_lost_audio.play()
            if slide_hitbox.colliderect(girlzombie_hitbox):
                window.blit(smoke, (girlzombiex - 80, 400))
                girlzombiex = -150
                lives -= 1
                if lives > 0:
                    life_lost_audio.play()
            walkcount += 1

        # code for player running or jumping
        if right and itemjump == False:

            #shows player running animation
            if character_powerup == False:
                window.blit(character_animation[walkcount//3], (x,y))

            # draws player hitboxes
            if character_selected == 1:
                character_hitbox = pygame.draw.rect(transparent_rectanlge, (85, 38, 132,50), (x+20, y+hitbox_y, width-40, height), 2)
            if character_selected == 2:
                character_hitbox = pygame.draw.rect(transparent_rectanlge, (85, 38, 132, 50), (x+15, y+hitbox_y, width-12, height-12), 2)
            if character_selected == 3:
                character_hitbox = pygame.draw.rect(transparent_rectanlge, (85, 38, 132,50), (x+18, y+hitbox_y, width-22, height-5), 2)

            # Collision code between running/jumping player and obstacles
            if character_hitbox.colliderect(zombie_hitbox):
                if lives == 1:
                    y = charactery
                window.blit(smoke, (zombiex-80, 400))
                zombiex = -150
                if lives > 0:
                    life_lost_audio.play()
                lives -= 1
            if character_hitbox.colliderect(bat_hitbox):
                window.blit(smoke, (batx - 80, 300))
                batx = -150
                lives -= 1
                if lives > 0:
                    life_lost_audio.play()
            if character_hitbox.colliderect(girlzombie_hitbox):
                window.blit(smoke, (girlzombiex - 80, 400))
                girlzombiex = -150
                lives -= 2
                if lives > 0:
                    life_lost_audio.play()
            walkcount += 1

        # Shows powerups on the bottom left of the screen, changing their positions based on the first powerup chosen (extra life does not appear)
        if item_selected == 1:
            if superjump == True:
                window.blit(superjump_ready, (0, 0))
                window.blit(space_key_superjump, (0, 0))
            else:
                window.blit(superjump_unready, (0, 0))
                window.blit(space_key_superjump, (0, 0))

            if gun_used == False:
                window.blit(gun_ready, (0, 0))
            else:
                window.blit(gun_unready, (0, 0))
            if character_selected == 3:
                if character_powerup_ready == True:
                    window.blit(santa_powerup_ready, (45, 0))
                else:
                    window.blit(santa_powerup_unready, (45, 0))
            if character_selected == 2:
                if character_powerup_ready == True:
                    window.blit(ninja_powerup_ready, (45, 0))
                else:
                    window.blit(ninja_powerup_unready, (45, 0))
            if character_selected == 1:
                if character_powerup_ready == True:
                    window.blit(robot_powerup_ready, (45, 0))
                else:
                    window.blit(robot_powerup_unready, (45, 0))

        if item_selected == 2:
            if superjump == True:
                window.blit(superjump_ready, (-150, 0))
                window.blit(space_key_superjump, (-150, 0))
            else:
                window.blit(superjump_unready, (-150, 0))
                window.blit(space_key_superjump, (-150, 0))
            if character_selected == 3:
                if character_powerup_ready == True:
                    window.blit(santa_powerup_ready, (-100, 0))
                else:
                    window.blit(santa_powerup_unready, (-100, 0))
            if character_selected == 2:
                if character_powerup_ready == True:
                    window.blit(ninja_powerup_ready, (-100, 0))
                else:
                    window.blit(ninja_powerup_unready, (-100, 0))
            if character_selected == 1:
                if character_powerup_ready == True:
                    window.blit(robot_powerup_ready, (-100, 0))
                else:
                    window.blit(robot_powerup_unready, (-100, 0))

        if item_selected == 3:
            if superjump == True:
                window.blit(superjump_ready, (0, 0))
                window.blit(space_key_superjump, (0, 0))
            else:
                window.blit(superjump_unready, (0, 0))
                window.blit(space_key_superjump, (0, 0))
            if score_powerup_ready == True:
                window.blit(score_ready, (0, 0))
            else:
                window.blit(score_unready, (0, 0))
            if character_selected == 3:
                if character_powerup_ready == True:
                    window.blit(santa_powerup_ready, (45, 0))
                else:
                    window.blit(santa_powerup_unready, (45, 0))
            if character_selected == 2:
                if character_powerup_ready == True:
                    window.blit(ninja_powerup_ready, (45, 0))
                else:
                    window.blit(ninja_powerup_unready, (45, 0))
            if character_selected == 1:
                if character_powerup_ready == True:
                    window.blit(robot_powerup_ready, (45, 0))
                else:
                    window.blit(robot_powerup_unready, (45, 0))

        #shows hearts based on how many lives the player has
        if lives == 4:
            window.blit(fourlives, (0, 0))
        if lives == 3:
            window.blit(threelives, (0, 0))
        if lives == 2:
            window.blit(twolives, (0, 0))
        if lives == 1:
            window.blit(onelife, (0, 0))

        #shows player score on top left
        largeFont = pygame.font.SysFont('roboto', 70)  # Font object
        text = largeFont.render(str(score.__round__()), 1, (255, 255, 255))  # create our text
        window.blit(text, (scorex, 20))
        if score > 99:
            scorex = 1425
        if score > 999:
            scorex = 1400

        # Code for the gun powerup
        if gun == True:
            window.blit(targeting, (zombiex-15, 640))
            window.blit(targeting, (girlzombiex - 15, 640))
            window.blit(targeting, (batx+10, 585))
            zombiex = -200
            girlzombiex = -200
            batx = -200
            gun = False

        # Code for the character powerups (based on which character is chosen)
        if character_powerup == True:

                # Santa powerup
                if character_selected == 3:
                    score_audio.play()
                    window.blit(santa_fishing_pole[walkcount//3], (x+60, y-55))
                    window.blit(character_animation[walkcount // 3], (x, y))
                    if add_vel == True:
                        hitbox_y += 1000
                        vel += 70
                        vel2 += 70
                        add_vel = False

                # Ninja powerup
                if character_selected == 2:
                    if powerupx < (x+200):
                        knife_audio.play()
                        window.blit(ninja_throw, (x, y))
                    else:
                        window.blit(character_animation[walkcount // 3], (x, y))
                    kunai_hitbox = pygame.draw.rect(transparent_rectanlge, (85, 38, 132, 50), (powerupx + 30, 625, 75, y), 2)
                    window.blit(kunais, (powerupx, y))
                    if kunai_hitbox.colliderect(zombie_hitbox):
                        window.blit(smoke, (zombiex - 80, 400))
                        zombiex = -150
                    if kunai_hitbox.colliderect(bat_hitbox):
                        window.blit(smoke, (batx - 80, 300))
                        batx = -150
                    if kunai_hitbox.colliderect(girlzombie_hitbox):
                        window.blit(smoke, (girlzombiex - 80, 400))
                        girlzombiex = -150

                # Robot powerup
                if character_selected == 1:
                    if powerupx < (x+200):
                        fireball_audio.play()
                        window.blit(robot_shoot, (x, y))
                    else:
                        window.blit(character_animation[walkcount // 3], (x, y))
                    fireball_hitbox = pygame.draw.rect(transparent_rectanlge, (85, 38, 132, 50), (powerupx + 30, 625, 75, y), 2)
                    window.blit(fireball, (powerupx, y))
                    if fireball_hitbox.colliderect(zombie_hitbox):
                        window.blit(smoke, (zombiex - 80, 400))
                        zombiex = -150
                    if fireball_hitbox.colliderect(bat_hitbox):
                        window.blit(smoke, (batx - 80, 300))
                        batx = -150
                    if fireball_hitbox.colliderect(girlzombie_hitbox):
                        window.blit(smoke, (girlzombiex - 80, 400))
                        girlzombiex = -150

        # Death animation, when lives are 0
        if death == True:
            death_audio.play()
            right = False
            down = False
            jump = False
            itemjump = True
            window.blit(water_bucket, (item_x1, item_y1))
            window.blit(stone_sword, (item_x2, item_y2))
            window.blit(gold, (item_x3, item_y3))
            window.blit(diamond, (item_x4, item_y4))

        pygame.display.update()


    def pause_menu():

        # globals the variables that need to be referenced in the pause menu
        global pause
        global unpause
        global pause_menu_selection
        global lives
        global score
        global FPS

        # while loop pauses the main_game loop
        while pause:

            # changes fps to 15
            clock.tick(FPS)

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # shows game background in the back to create the illusion of the game still being loaded
            window.blit(bg, (0, 0))

            # generates font to show score and lives
            Font = pygame.font.SysFont('roboto', 70)
            lives_count = Font.render(str(lives), 1, (255, 255, 255))
            text2 = Font.render(str(score.__round__()), 1, (255, 255, 255))

            # code for the down key in the pause menu
            if keys[pygame.K_DOWN]:
                if pause_menu_selection == 1 or pause_menu_selection == 2:
                    pause_menu_selection += 1
                    menu_move.play()

            # code for the up key in the pause menu
            if keys[pygame.K_UP]:
                if pause_menu_selection == 2 or pause_menu_selection == 3:
                    pause_menu_selection -= 1
                    menu_move.play()

            # code for the RETURN key in the pause menu
            if keys[pygame.K_RETURN]:
                if pause_menu_selection == 1:
                    pygame.mixer.music.unpause()
                    pause = False
                    FPS = 30
                if pause_menu_selection == 2:
                    menu_select.play()
                    pause_menu_selection = 4
                if pause_menu_selection == 3:
                    pygame.quit()
                    quit()

            # code for the escape key to leave the controls page
            if keys[pygame.K_ESCAPE]:
                if pause_menu_selection == 4:
                    pause_menu_selection = 2

            # shows what is selected in the menu (1: resume, 2: controls, 3: exit)
            if pause_menu_selection == 1:
                window.blit(resume_selected, (0, 0))
                window.blit(lives_count, (425,780))
                window.blit(text2, (425, 715))
            if pause_menu_selection == 2:
                window.blit(pause_controls_selected, (0, 0))
                window.blit(lives_count, (425, 780))
                window.blit(text2, (425, 715))
            if pause_menu_selection == 3:
                window.blit(exit_game_selected, (0, 0))
                window.blit(lives_count, (425, 780))
                window.blit(text2, (425, 715))
            if pause_menu_selection == 4:
                window.blit(controlspagewindow, (0, 0))
            pygame.display.update()
        pygame.display.update()

    def ending_menu():

        # globals needed variables for the ending menu
        global show_score
        global ending_menu_selection
        global leaderboardx
        global leaderboardx2

        # pauses the main loop forever
        while ending:

            # sets fps to 15
            clock.tick(FPS)

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # creates font to show score after death
            Font = pygame.font.SysFont('roboto', 80)  # Font object
            show_score = Font.render(str(score.__round__()), 1, (255, 255, 255))

            # shows what is selected in the end_screen
            if ending_menu_selection == 1:
                window.blit(leaderboard_selected, (0, 0))
                # shows score
                window.blit(show_score, (790, 415))
            if ending_menu_selection == 2:
                window.blit(ending_exit_selected, (0, 0))
                # shows score
                window.blit(show_score, (790, 415))
            if ending_menu_selection == 3:
                # shows leaderboard, with moving elements at the top and bottom
                window.blit(leaderboard, (0, 0))
                window.blit(purple_escape_button, (0, 60))
                window.blit(top_leaderboard, (leaderboardx, 0))
                window.blit(bottom_leaderboard, (leaderboardx2, 0))
                leaderboardx -= 4
                leaderboardx2 += 4

                # resets the positions for the moving parts in the leaderboard
                if leaderboardx == -2000:
                    leaderboardx = 0
                    leaderboardx2 = -2480

            # code for the down button in the ending screen
            if keys[pygame.K_DOWN]:
                if ending_menu_selection == 1:
                    menu_move.play()
                    ending_menu_selection += 1

            # code for the up button in the ending screen
            if keys[pygame.K_UP]:
                if ending_menu_selection == 2:
                    menu_move.play()
                    ending_menu_selection -= 1

            # code for the RETURN key in the ending screen
            if keys[pygame.K_RETURN]:
                if ending_menu_selection == 1:
                    menu_select.play()
                    ending_menu_selection = 3
                if ending_menu_selection == 2:
                    pygame.quit()
                    quit()

            # code for the escape button in the leaderboard
            if keys[pygame.K_ESCAPE]:
                if ending_menu_selection == 3:
                    ending_menu_selection = 1
            pygame.display.update()

# the main game loop for the gameplay
while main_game == True:

    # initialises audio files needed for the main game and end screen
    mixer.music.load('main_game_music.wav')
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    superjump_audio = mixer.Sound('jump.wav')
    score_audio = mixer.Sound('whoosh.wav')
    gun_audio = mixer.Sound('gun.wav')
    death_audio = mixer.Sound('death.wav')
    life_lost_audio = mixer.Sound('life_lost.wav')
    knife_audio = mixer.Sound('knife.wav')
    fireball_audio = mixer.Sound('fireball.wav')
    running_audio = mixer.Sound('running.wav')
    sliding_audio = mixer.Sound('sliding.wav')

    # images needed for the pause menu
    resume_selected = pygame.image.load(os.path.join('images', 'resume_game_selected.png')).convert_alpha()
    pause_controls_selected = pygame.image.load(os.path.join('images', 'pause_controls_selected.png')).convert_alpha()
    exit_game_selected = pygame.image.load(os.path.join('images', 'exit_game_selected.png')).convert_alpha()

    # Initialises all assets needed for character 1 (Robot)
    if character_selected == 1:
        character_animation = [pygame.image.load(os.path.join('character sprites', 'robotrun1.png')), pygame.image.load(os.path.join('character sprites', 'robotrun2.png')),
                     pygame.image.load(os.path.join('character sprites', 'robotrun3.png')), pygame.image.load(os.path.join('character sprites', 'robotrun4.png')),
                     pygame.image.load(os.path.join('character sprites', 'robotrun5.png')), pygame.image.load(os.path.join('character sprites', 'robotrun6.png')),
                     pygame.image.load(os.path.join('character sprites', 'robotrun7.png')), pygame.image.load(os.path.join('character sprites', 'robotrun8.png')),
                     pygame.image.load(os.path.join('character sprites', 'robotrun1.png'))]
        slide = pygame.image.load(os.path.join('character sprites', 'robotslide.png')).convert_alpha()
        idle_character = pygame.image.load(os.path.join('character sprites', 'robot_idle.png')).convert_alpha()
        robot_shoot = pygame.image.load(os.path.join('character sprites', 'robot_shoot.png')).convert_alpha()
        fireball = pygame.image.load(os.path.join('character sprites', 'fireball.png')).convert_alpha()
        robot_powerup_unready = pygame.image.load(os.path.join('images', 'robot_powerup_unready.png')).convert_alpha()
        robot_powerup_ready = pygame.image.load(os.path.join('images', 'robot_powerup_ready.png')).convert_alpha()
        y = 615
        slidey = 670

    # Initialises all assets needed for character 2 (Ninja)
    if character_selected == 2:
        character_animation = [pygame.image.load(os.path.join('character sprites', 'ninjarun1.png')), pygame.image.load(os.path.join('character sprites', 'ninjarun2.png')),
                          pygame.image.load(os.path.join('character sprites', 'ninjarun3.png')), pygame.image.load(os.path.join('character sprites', 'ninjarun4.png')),
                          pygame.image.load(os.path.join('character sprites', 'ninjarun5.png')), pygame.image.load(os.path.join('character sprites', 'ninjarun6.png')),
                          pygame.image.load(os.path.join('character sprites', 'ninjarun7.png')), pygame.image.load(os.path.join('character sprites', 'ninjarun8.png')),
                          pygame.image.load(os.path.join('character sprites', 'ninjarun9.png'))]
        slide = pygame.image.load(os.path.join('character sprites', 'ninjaslide1.png')).convert_alpha()
        idle_character = pygame.image.load(os.path.join('character sprites', 'ninja_idle.png')).convert_alpha()
        ninja_throw = pygame.image.load(os.path.join('character sprites', 'ninja_throw.png')).convert_alpha()
        kunais = pygame.image.load(os.path.join('character sprites', 'kunais.png')).convert_alpha()
        ninja_powerup_unready = pygame.image.load(os.path.join('images', 'ninja_powerup_unready.png')).convert_alpha()
        ninja_powerup_ready = pygame.image.load(os.path.join('images', 'ninja_powerup_ready.png')).convert_alpha()

        y = 620
        slidey = 670

    # Initialises all assets needed for character 3 (Santa)
    if character_selected == 3:
        character_animation = [pygame.image.load(os.path.join('character sprites', 'santarun1.png')), pygame.image.load(os.path.join('character sprites', 'santarun2.png')),
                     pygame.image.load(os.path.join('character sprites', 'santarun3.png')), pygame.image.load(os.path.join('character sprites', 'santarun4.png')),
                     pygame.image.load(os.path.join('character sprites', 'santarun5.png')), pygame.image.load(os.path.join('character sprites', 'santarun6.png')),
                     pygame.image.load(os.path.join('character sprites', 'santarun7.png')), pygame.image.load(os.path.join('character sprites', 'santarun8.png')),
                     pygame.image.load(os.path.join('character sprites', 'santarun7.png'))]
        slide = pygame.image.load(os.path.join('character sprites', 'santaslide1.png')).convert_alpha()
        idle_character = pygame.image.load(os.path.join('character sprites', 'santa_idle.png')).convert_alpha()
        santa_fishing_pole = [pygame.image.load(os.path.join('character sprites', 'santa_fishing_pole.png')),
                     pygame.image.load(os.path.join('character sprites', 'santa_fishing_pole2.png')),
                     pygame.image.load(os.path.join('character sprites', 'santa_fishing_pole3.png')),
                     pygame.image.load(os.path.join('character sprites', 'santa_fishing_pole4.png')),
                     pygame.image.load(os.path.join('character sprites', 'santa_fishing_pole5.png')),
                     pygame.image.load(os.path.join('character sprites', 'santa_fishing_pole6.png')),
                     pygame.image.load(os.path.join('character sprites', 'santa_fishing_pole7.png')),
                     pygame.image.load(os.path.join('character sprites', 'santa_fishing_pole8.png')),
                     pygame.image.load(os.path.join('character sprites', 'santa_fishing_pole9.png'))]
        santa_powerup_unready = pygame.image.load(os.path.join('images', 'santa_powerup_unready.png')).convert_alpha()
        santa_powerup_ready = pygame.image.load(os.path.join('images', 'santa_powerup_ready.png')).convert_alpha()

        y = 615
        slidey = 670

    # Initialises all assets needed for the main game and the end screen
    bg = pygame.image.load(os.path.join('images','gamebg_and_floor.png')).convert_alpha()
    floor = pygame.image.load(os.path.join('images', 'game_floor.png')).convert_alpha()
    onelife = pygame.image.load(os.path.join('images', 'one_life.png')).convert_alpha()
    twolives = pygame.image.load(os.path.join('images', 'two_lives.png')).convert_alpha()
    threelives = pygame.image.load(os.path.join('images', 'three_lives.png')).convert_alpha()
    smoke = pygame.image.load(os.path.join('images', 'smoke.png')).convert_alpha()
    superjump_ready = pygame.image.load(os.path.join('images', 'superjump_ready.png')).convert_alpha()
    superjump_unready = pygame.image.load(os.path.join('images', 'superjump_unready.png')).convert_alpha()
    space_key_superjump = pygame.image.load(os.path.join('images', 'space_key_superjump.png')).convert_alpha()
    leaderboard_selected = pygame.image.load(os.path.join('images', 'leaderboard_selected.png')).convert_alpha()
    ending_exit_selected = pygame.image.load(os.path.join('images', 'ending_exit_selected.png')).convert_alpha()
    leaderboard = pygame.image.load(os.path.join('images', 'leaderboard.png')).convert_alpha()
    bottom_leaderboard = pygame.image.load(os.path.join('images', 'bottom_leaderboard.png')).convert_alpha()
    top_leaderboard = pygame.image.load(os.path.join('images', 'top_leaderboard.png')).convert_alpha()
    purple_escape_button = pygame.image.load(os.path.join('images', 'purple_escape_button.png')).convert_alpha()
    water_bucket = pygame.image.load(os.path.join('character sprites', 'water_bucket.png')).convert_alpha()
    stone_sword = pygame.image.load(os.path.join('character sprites', 'stone_sword.png')).convert_alpha()
    gold = pygame.image.load(os.path.join('character sprites', 'gold.png')).convert_alpha()
    diamond = pygame.image.load(os.path.join('character sprites', 'diamond.png')).convert_alpha()

    # Initialises all assets needed for powerups, based on selection in the title page
    if item_selected == 1:
        targeting = pygame.image.load(os.path.join('images', 'targeting.png')).convert_alpha()
        gun_ready = pygame.image.load(os.path.join('images', 'gun_ready.png')).convert_alpha()
        gun_unready = pygame.image.load(os.path.join('images', 'gun_unready.png')).convert_alpha()
    if item_selected == 2:
        fourlives = pygame.image.load(os.path.join('images', 'four_lives.png')).convert_alpha()
    if item_selected == 3:
        score_ready = pygame.image.load(os.path.join('images', 'score_powerup_ready.png')).convert_alpha()
        score_unready = pygame.image.load(os.path.join('images', 'score_powerup_unready.png')).convert_alpha()

    # Animates all obstacles
    zombieWalk = [pygame.image.load(os.path.join('obstacle sprites', 'zombiewalk1.png')), pygame.image.load(os.path.join('obstacle sprites', 'zombiewalk2.png')),
                 pygame.image.load(os.path.join('obstacle sprites', 'zombiewalk3.png')), pygame.image.load(os.path.join('obstacle sprites', 'zombiewalk4.png')),
                 pygame.image.load(os.path.join('obstacle sprites', 'zombiewalk5.png')), pygame.image.load(os.path.join('obstacle sprites', 'zombiewalk6.png')),
                 pygame.image.load(os.path.join('obstacle sprites', 'zombiewalk7.png')), pygame.image.load(os.path.join('obstacle sprites', 'zombiewalk8.png')),
                 pygame.image.load(os.path.join('obstacle sprites', 'zombiewalk9.png'))]
    batFly = [pygame.image.load(os.path.join('obstacle sprites', 'bat1.png')),pygame.image.load(os.path.join('obstacle sprites', 'bat2.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'bat3.png')),pygame.image.load(os.path.join('obstacle sprites', 'bat4.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'bat5.png')),pygame.image.load(os.path.join('obstacle sprites', 'bat6.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'bat7.png')),pygame.image.load(os.path.join('obstacle sprites', 'bat8.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'bat1.png'))]
    girlzombieWalk = [pygame.image.load(os.path.join('obstacle sprites', 'zombiegirlwalk1.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'zombiegirlwalk2.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'zombiegirlwalk3.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'zombiegirlwalk4.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'zombiegirlwalk5.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'zombiegirlwalk6.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'zombiegirlwalk7.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'zombiegirlwalk8.png')),
                  pygame.image.load(os.path.join('obstacle sprites', 'zombiegirlwalk9.png'))]

    x = 10  # Player x position
    zombiex = 1520  # Obstacle (zombie) x position
    batx = 2500  # Obstacle (bat) x position
    girlzombiex = 8000  # Obstacle (girl zombie) x position
    bgx = 0 # floor x position (changes through loops)
    charactery = y # checks to see if the player is on the ground
    bgx2 = bg.get_width()   # used to see the image width for the scrolling floor
    width = 110 # player and obstacle image width
    height = 150    # player and obstacle image height
    vel = 5     # player movement
    vel2 = 16   # floor and obstacle movement
    scorex = 1450   # x coordinate of score displayed on top right
    jump = False    # used to see if the player has jumped
    right = False   # is the normal animation of player running (checks if player is not jumping or sliding)
    down = False    # used to see if the player is sliding
    walkcount = 0   # used for character and obstacle animation
    jumpcount = 10  # used for character jumping movement
    FPS = 30    # sets the ticks per second for the main loop (set to 30)

    if item_selected == 2:
        lives = 4
    else:                   # checks if the second powerup is selected, if so then lives will be set to 4
        lives = 3

    pause = False   # checks if the game has been paused
    score = 0   # variable controlling the score
    pause_menu_selection = 1    # movement for pause selection
    jumpheight = 0.8    # height of player jumps
    superjump = True    # checks if the superjump powerup has been used
    ending = False      # checks if the game has ended
    gun = False         # checks if the gun powerup has been selected
    gun_used = False    # checks if the gun powerup has been used
    score_powerup = False   # checks if the score powerup has been used
    score_powerup_ready = True  # checks if the gun powerup is ready or on cooldown
    character_powerup = False   # checks if the individual character powerup has been used
    character_powerup_ready = True  # checks if the individual character powerup is ready or on cooldown
    add_vel = False     # used for Santa powerup, to change the velocity back to its original amount
    change_back = True  # used for Santa powerup, to unblit the finshing rod shown
    powerupx = x + 50   # sets the x for the powerup usage

    if character_selected == 1:     # changes the y of the hitbox based on the character chosen
        hitbox_y = 2
    if character_selected == 2 or character_selected == 3:
        hitbox_y = 0

    ending_menu_selection = 1   # movement for ending selection
    death = False       # checks if the player has died
    ending_screen = False     # checks if the ending screen should be shown
    itemjump = False     # checks if the death animation should be shown
    item_y1 = 700
    item_y2 = 700       # sets the y spawn position for the death animation, which will change with time
    item_y3 = 700
    item_y4 = 700
    item_x1 = x + 200
    item_x2 = x + 200       # sets the x spawn position for the death animation, which will change with time
    item_x3 = x + 200
    item_x4 = x + 200
    add_jump = True     # redefines the jumpcount so that the animation can work even when the character dies while jumping
    leaderboardx = 0        # top half of the leaderboard animation
    leaderboardx2 = -2480   # bottom half of the leaderboard animation

    while main_game == True:

        #sets fps to 30
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

            if event.type == pygame.USEREVENT+1:    # cooldown for the superjump powerup
                superjump = True

            if event.type == pygame.USEREVENT+2:    # cooldown for the gun powerup
                gun_used = False

            if event.type == pygame.USEREVENT+3:    # cooldown for the score powerup
                score_powerup_ready = True

            if event.type == pygame.USEREVENT+4:    # checks the amount of time the score powerup runs for
                score_powerup = False

            if event.type == pygame.USEREVENT+5:    # cooldown for the character powerup
                    character_powerup_ready = True

            if event.type == pygame.USEREVENT+6:    # checks the amount of time the character powerup runs for
                if character_selected == 3:
                    character_powerup = False
                    add_vel = False
                    if change_back == True:
                        hitbox_y -= 1000
                        vel -= 70
                        vel2 -= 70
                        change_back = False
                if character_selected == 2:
                    character_powerup = False
                if character_selected == 1:
                    character_powerup = False

        keys = pygame.key.get_pressed()

        # code for the pause menu during the game
        if keys[pygame.K_ESCAPE]:
            pygame.mixer.music.pause()
            pause = True
            FPS = 15
            pause_menu()

        # code for running the gun powerup once Z is pressed
        if item_selected == 1:
            if keys[pygame.K_z] and gun_used == False:
                gun_audio.play()
                gun = True
                pygame.time.set_timer(pygame.USEREVENT + 2, 30000)
                gun_used = True

        # code for running the score powerup once Z is pressed
        if item_selected == 3:
            if keys[pygame.K_z] and score_powerup_ready == True:
                score_audio.play()
                score_powerup = True
                score_powerup_ready = False
                pygame.time.set_timer(pygame.USEREVENT + 3, 30000)
                pygame.time.set_timer(pygame.USEREVENT + 4, 10000)

        # code for running the Santa character powerup once X is pressed
        if keys[pygame.K_x] and character_powerup_ready == True and character_selected == 3:
            character_powerup = True
            character_powerup_ready = False
            add_vel = True
            change_back = True
            pygame.time.set_timer(pygame.USEREVENT + 5, 30000)
            pygame.time.set_timer(pygame.USEREVENT + 6, 10000)

        # code for running the Ninja character powerup once X is pressed
        if keys[pygame.K_x] and character_powerup_ready == True and character_selected == 2 and charactery == y:
            character_powerup = True
            character_powerup_ready = False
            powerupx = x
            pygame.time.set_timer(pygame.USEREVENT + 5, 30000)
            pygame.time.set_timer(pygame.USEREVENT + 6, 10000)

        # code for running the Robot character powerup once X is pressed
        if keys[pygame.K_x] and character_powerup_ready == True and character_selected == 1 and charactery == y:
            character_powerup = True
            character_powerup_ready = False
            powerupx = x
            pygame.time.set_timer(pygame.USEREVENT + 5, 30000)
            pygame.time.set_timer(pygame.USEREVENT + 6, 10000)

        # causes a small delay when the game starts so that the player runs but the background stays still
        if x < 190:
            x += vel
            right = True
        else:
            right = True

        # code for the scrolling floor
        if x > 180:
            bgx -= vel
            bgx2 -= vel
            if bgx < bg.get_width() * -1:
                bgx = bg.get_width()
            if bgx2 < bg.get_width() * -1:
                bgx2 = bg.get_width()

            # makes obstacles go left on the screen
            zombiex -= vel2
            batx -= vel2
            girlzombiex -= vel2

        # makes the obstacles spawn at a random location off-screen
        if zombiex < -100:
            zombiex = random.randint(1520,2500)
        if batx < -100:
            batx = random.randint(3000, 8000)
        if girlzombiex < -100:
            girlzombiex = random.randint(8000, 12000)

        # code for the sliding of the character
        if keys[pygame.K_DOWN] and character_powerup == False:
            if jump == False:
                down = True
                right = False
                jump = False
        else:
            down = False

        # code for the character jumping
        if not(jump):
            if keys[pygame.K_UP] and y > (vel + 170):
                jump = True
                down = False
                walkcount = 0
                jumpheight = 0.6

            # code for the superjump powerup
            if keys[pygame.K_SPACE] and superjump == True:
                superjump_audio.play()
                pygame.time.set_timer(pygame.USEREVENT + 1, 15000)
                jump = True
                down = False
                walkcount = 0
                jumpheight = 1

        else:
            if jumpcount >= -10:
                neg = 1
                if jumpcount < 0:
                    neg = -1
                y -= (jumpcount ** 2) * jumpheight * neg
                if jumpheight == 1:
                    superjump = False
                if x < 500:
                    if jumpheight == 1:
                        x += 15
                jumpcount -= 1
                down = False
            else:
                jump = False
                jumpcount = 10
                down = False

        # makes the player move back to the default location after using the superjump
        if right:
            if x > 201:
                if y == charactery:
                    x -= vel2

        # changes powerup x coordinate once it is needed
        if character_powerup == True:
            powerupx += 50
            if powerupx > 2500:
                powerupx = x + 50

        # creates the death animation once the lives is equal to 0
        if lives == 0 or lives < 0:
            pygame.mixer.music.fadeout(1500)
            if add_jump == True:
                jumpcount = 10
            add_jump = False
            death = True
            down = False
            character_powerup = False
            jump = False
            vel2 = 0
            vel = 0
            if jumpcount >= -10:
                neg = 1
                if jumpcount < 0:
                    neg = -1
                item_y1 -= (jumpcount ** 2) * 0.8 * neg
                item_x1 += 5
                item_y2 -= (jumpcount ** 2) * 0.6 * neg
                item_x2 += 8                                #makes items jump after death (animation)
                item_y3 -= (jumpcount ** 2) * 0.8 * neg
                item_x3 -= 5
                item_y4 -= (jumpcount ** 2) * 0.6 * neg
                item_x4 -= 8
                jumpcount -= 1

            # opens the end screen after the death animation is completed
            if item_y1 > 724:
                pygame.time.delay(1000)
                mixer.music.load('ending_music.wav')
                mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.2)
                death = True
                ending_screen = True
                ending = True
                ending_menu()
            if item_y1 > 699:
                item_y1 = 725
                item_y2 = 725
                item_y3 = 725
                item_y4 = 725

        # runs the main game drawring after each loop
        draw_Main_Game()

        # increases the velocity and score after every loop where the player is not dead
        if death == False:
            vel2 += 0.02
            vel += 0.01
            if score_powerup == False:
                score += 0.20
            else:
                score += 0.40

pygame.quit()