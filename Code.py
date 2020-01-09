#!/usr/bin/env python3

# Created by: Joey Marcotte & Ben Whitten
# Created on: December 2019
# This file is the "Jungle Joe and Snakob" game
# for CircuitPython
import ugame
import stage
import board
# import neopixel
import time
import random
import constants

def blank_white_reset_scene():
    # this function is the splash scene game loop
    # do house keeping to ensure everythng is setup
    # set up the NeoPixels
    # pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    # pixels.deinit() # and turn them all off
    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        # Wait for 1/2 seconds
        time.sleep(0.5)
        mt_splash_scene()
        # redraw sprite list

def mt_splash_scene():
    # this function is the MT splash scene
    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white
    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white
    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white
    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        # Wait for 1/2 seconds
        time.sleep(1.0)
        game_splash_scene()
        # redraw sprite list

def game_splash_scene():
    # this function is the game scene
    text = []
    sprites = []
    image_bank_3 = stage.Bank.from_bmp16("jungle_joe.bmp")
    image_bank_4 = stage.Bank.from_bmp16("elemental_studios.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    text_1 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_1.move(13, 60)
    text_1.text("ELEMENTAL STUDIOS")
    text.append(text_1)
    fire_upper_right = stage.Sprite(image_bank_4, 0, 16, 0)
    sprites.append(fire_upper_right)
    fire_bottom_right = stage.Sprite(image_bank_4, 1, 16, 16)
    sprites.append(fire_bottom_right)
    fire_upper_left = stage.Sprite(image_bank_4, 2, 0, 0)
    sprites.append(fire_upper_left)
    fire_bottom_left = stage.Sprite(image_bank_4, 3, 0, 16)
    sprites.append(fire_bottom_left)
    water_upper_right = stage.Sprite(image_bank_4, 6, 144, 0)
    sprites.append(water_upper_right)
    water_bottom_right = stage.Sprite(image_bank_4, 7, 144, 16)
    sprites.append(water_bottom_right)
    water_upper_left = stage.Sprite(image_bank_4, 4, 128, 0)
    sprites.append(water_upper_left)
    water_bottom_left = stage.Sprite(image_bank_4, 5, 128, 16)
    sprites.append(water_bottom_left)
    earth_upper_right = stage.Sprite(image_bank_4, 10, 16, 98)
    sprites.append(earth_upper_right)
    earth_bottom_right = stage.Sprite(image_bank_4, 11, 16, 112)
    sprites.append(earth_bottom_right)
    earth_upper_left = stage.Sprite(image_bank_4, 8, 0, 98)
    sprites.append(earth_upper_left)
    earth_bottom_left = stage.Sprite(image_bank_4, 9, 0, 112)
    sprites.append(earth_bottom_left)
    wind_upper_right = stage.Sprite(image_bank_4, 14, 144, 98)
    sprites.append(wind_upper_right)
    wind_bottom_right = stage.Sprite(image_bank_4, 15, 144, 112)
    sprites.append(wind_bottom_right)
    wind_upper_left = stage.Sprite(image_bank_4, 12, 128, 98)
    sprites.append(wind_upper_left)
    wind_bottom_left = stage.Sprite(image_bank_4, 13, 128, 112)
    sprites.append(wind_bottom_left)
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    # wait until refresh rate finishes
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        time.sleep(1.0)
        main_menu_scene()
        # redraw sprite list
        pass # just a placeholder until you write the code

def main_menu_scene():
    # this function is the main menu scene
    text = []
    sprites = []
    sun = []

    image_bank_5 = stage.Bank.from_bmp16("Backgrounds.bmp")
    image_bank_5 = stage.Bank.from_bmp16("backgrounds.bmp")
    image_bank_3 = stage.Bank.from_bmp16("jungle_joe.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_5, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    background.tile(2, 8, 1)
    background.tile(2, 8, 2)
    background.tile(2, 8, 3)
    background.tile(2, 8, 4)
    background.tile(2, 8, 5)
    background.tile(2, 8, 6)
    background.tile(2, 8, 7)
    background.tile(2, 8, 8)
    background.tile(2, 8, 9)
    background.tile(2, 8, 10)

    text_1 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_1.move(40, 35)
    text_1.move(40, 48)
    text_1.text("JUNGLE JOE")
    text.append(text_1)

    text_2 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_2.move(40, 45)
    text_2.move(40, 58)
    text_2.text("& SNAKOB'S")
    text.append(text_2)

    text_3 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_3.move(25, 55)
    text_3.move(25, 68)
    text_3.text("BONGO BANANZA!")
    text.append(text_3)
    

    text_4 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text_4.move(35, 118)
    text_4.text("PRESS START!")
    text.append(text_4)

    # Displays the tree tops
    tree_top_1 = stage.Sprite(image_bank_5, 1, 0, 112)
    sprites.append(tree_top_1)
    tree_top_2 = stage.Sprite(image_bank_5, 1, 16, 112)
    sprites.append(tree_top_2)
    tree_top_3 = stage.Sprite(image_bank_5, 1, 32, 112)
    sprites.append(tree_top_3)
    tree_top_4 = stage.Sprite(image_bank_5, 1, 48, 112)
    sprites.append(tree_top_4)
    tree_top_5 = stage.Sprite(image_bank_5, 1, 64, 112)
    sprites.append(tree_top_5)
    tree_top_6 = stage.Sprite(image_bank_5, 1, 80, 112)
    sprites.append(tree_top_6)
    tree_top_7 = stage.Sprite(image_bank_5, 1, 96, 112)
    sprites.append(tree_top_7)
    tree_top_8 = stage.Sprite(image_bank_5, 1, 112, 112)
    sprites.append(tree_top_8)
    tree_top_9 = stage.Sprite(image_bank_5, 1, 128, 112)
    sprites.append(tree_top_9)
    tree_top_10 = stage.Sprite(image_bank_5, 1, 144, 112)
    sprites.append(tree_top_10)
    # Displays the sun
    sun_top_left = stage.Sprite(image_bank_5, 11, 128, 0)
    sun.append(sun_top_left)
    sun_top_right = stage.Sprite(image_bank_5, 10, 144, 0)
    sun.append(sun_top_right)
    sun_bottom_left = stage.Sprite(image_bank_5, 8, 128, 16)
    sun.append(sun_bottom_left)
    sun_bottom_right = stage.Sprite(image_bank_5, 9, 144, 16)
    sun.append(sun_bottom_right)
    # Displays Jungle Joe
    jungle_joe = stage.Sprite(image_bank_3, 15, 71, 98)
    sprites.append(jungle_joe)

    clouds = []
    for cloud_number in range(constants.TOTAL_CLOUDS):
        a_single_cloud = stage.Sprite(image_bank_5, 4, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        clouds.append(a_single_cloud)

    def Show_clouds():
        for cloud_number in range(len(clouds)):
            if clouds[cloud_number].y < 0:
                clouds[cloud_number].move(constants.OFF_LEFT_SCREEN, random.randint(0 - constants.SPRITE_SIZE, constants.SCREEN_Y - constants.SPRITE_SIZE))
                break

    cloud_count = 6
    Show_clouds()
    Show_clouds()

    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + clouds + [background]
    game.layers = text + sprites + clouds + sun + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    # wait until refresh rate finishes
    game.render_block()
    # repeat forever, game loop

    while True:
        # get user input

        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_START != 0:  # Start button
            game_scene()

        # update game logic
        for cloud_number in range (len(clouds)):
            if clouds[cloud_number].y > 0:
                clouds[cloud_number].move(clouds[cloud_number].x
                                          + constants.CLOUD_SPEED,
                                          clouds[cloud_number].y)
                if clouds[cloud_number].x > constants.SCREEN_X + constants.SPRITE_SIZE:
                    clouds[cloud_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    Show_clouds()
                if clouds[cloud_number].x > constants.SCREEN_X / 2:
                    Show_clouds()
        # redraw sprite list
        pass # just a placeholder until you write the code

        game.render_sprites(clouds)
        game.tick()

def game_scene():
    # this function is the game scene
    border = []
    sprites = []
    image_bank_5 = stage.Bank.from_bmp16("backgrounds.bmp")
    image_bank_3 = stage.Bank.from_bmp16("jungle_joe.bmp")

    background = stage.Grid(image_bank_5, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_2_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(2,3)
            background.tile(x_location, y_location, tile_picked)
    for x_location in range(constants.SCREEN_GRID_2_X, constants.SCREEN_GRID_Y):
        for y_location in range(constants.SCREEN_GRID_Y):
            background.tile(x_location, y_location, 5)

    # Displays the border.
    border_1 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 0)
    border.append(border_1)
    border_2 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 16)
    border.append(border_2)
    border_3 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 32)
    border.append(border_3)
    border_4 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 48)
    border.append(border_4)
    border_5 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 64)
    border.append(border_5)
    border_6 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 80)
    border.append(border_6)
    border_7 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 96)
    border.append(border_7)
    border_8 = stage.Sprite(image_bank_5, 6, constants.BORDER_LOCATION, 112)
    border.append(border_8)

    # Displays key sprites.
    a_button = stage.Sprite(image_bank_3, 12, constants.A_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(a_button)
    b_button = stage.Sprite(image_bank_3, 11, constants.B_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(b_button)
    left_arrow = stage.Sprite(image_bank_3, 8, constants.LEFT_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(left_arrow)
    right_arrow = stage.Sprite(image_bank_3, 7, constants.RIGHT_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(right_arrow)
    up_arrow = stage.Sprite(image_bank_3, 10, constants.UP_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(up_arrow)
    down_arrow = stage.Sprite(image_bank_3, 9, constants.DOWN_BUTTON, constants.BUTTON_HEIGHT)
    sprites.append(down_arrow)
    
    def show_abutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make a button show up on screen in the x-axis
        for a_button_number in range(len(abutton)):
            if abutton[a_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                abutton[a_button_number].move(constants.A_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    abutton = []
    for a_button_number in range(constants.TOTAL_NUMBER_OF_A_BUTTON):
        a_single_abutton = stage.Sprite(image_bank_3, 6, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        abutton.append(a_single_abutton)

    # current number of buttons that should be moving down screen, start with just 1
    abutton_count = 1
    show_abutton()

    def show_bbutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an button show up on screen in the x-axis
        for b_button_number in range(len(bbutton)):
            if bbutton[b_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                bbutton[b_button_number].move(constants.B_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    bbutton = []
    for b_button_number in range(constants.TOTAL_NUMBER_OF_B_BUTTON):
        a_single_bbutton = stage.Sprite(image_bank_3, 5, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        bbutton.append(a_single_bbutton)

    # current number of buttons that should be moving down screen, start with just 1
    bbutton_count = 1
    show_bbutton()

    def show_upbutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an button show up on screen in the x-axis
        for up_button_number in range(len(upbutton)):
            if upbutton[up_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                upbutton[up_button_number].move(constants.UP_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    upbutton = []
    for up_button_number in range(constants.TOTAL_NUMBER_OF_UP_BUTTON):
        a_single_upbutton = stage.Sprite(image_bank_3, 4, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        upbutton.append(a_single_upbutton)

    # current number of buttons that should be moving down screen, start with just 1
    upbutton_count = 1
    show_upbutton()

    def show_downbutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an button show up on screen in the x-axis
        for down_button_number in range(len(downbutton)):
            if downbutton[down_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                downbutton[down_button_number].move(constants.DOWN_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    downbutton = []
    for down_button_number in range(constants.TOTAL_NUMBER_OF_DOWN_BUTTON):
        a_single_downbutton = stage.Sprite(image_bank_3, 3, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        downbutton.append(a_single_downbutton)

    # current number of buttons that should be moving down screen, start with just 1
    downbutton_count = 1
    show_downbutton()

    def show_leftbutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an button show up on screen in the x-axis
        for left_button_number in range(len(leftbutton)):
            if leftbutton[left_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                leftbutton[left_button_number].move(constants.LEFT_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    leftbutton = []
    for left_button_number in range(constants.TOTAL_NUMBER_OF_LEFT_BUTTON):
        a_single_leftbutton = stage.Sprite(image_bank_3, 2, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        leftbutton.append(a_single_leftbutton)

    # current number of buttons that should be moving down screen, start with just 1
    leftbutton_count = 1
    show_leftbutton()

    def show_rightbutton():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an button show up on screen in the x-axis
        for right_button_number in range(len(rightbutton)):
            if rightbutton[right_button_number].x < 0: # meaning it is off the screen, so available to move on the screen
                rightbutton[right_button_number].move(constants.RIGHT_BUTTON, random.randint(constants.OFF_SCREEN_Y, 0 - constants.SPRITE_SIZE))
                break

    # create buttons
    rightbutton = []
    for right_button_number in range(constants.TOTAL_NUMBER_OF_RIGHT_BUTTON):
        a_single_rightbutton = stage.Sprite(image_bank_3, 1, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        rightbutton.append(a_single_rightbutton)

    # current number of button that should be moving down screen, start with just 1
    rightbutton_count = 1
    show_rightbutton()

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = sprites + abutton + bbutton + upbutton + downbutton + leftbutton + rightbutton + [background]

    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # update game logic
        rand_number = random.randint(0, 6+1)

        if rand_number == 1:    
            for a_button_number in range(len(abutton)):
                if abutton[a_button_number].x > 0: # meaning it is on the screen
                    abutton[a_button_number].move(abutton[a_button_number].x, abutton[a_button_number].y + constants.BUTTON_SPEED)
                    if abutton[a_button_number].y > constants.SCREEN_Y:
                        abutton[a_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_abutton() # make it randomly show up at top again

        if rand_number == 2:    
            for b_button_number in range(len(bbutton)):
                if bbutton[b_button_number].x > 0: # meaning it is on the screen
                    bbutton[b_button_number].move(bbutton[b_button_number].x, bbutton[b_button_number].y + constants.BUTTON_SPEED)
                    if bbutton[b_button_number].y > constants.SCREEN_Y:
                        bbutton[b_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_bbutton() # make it randomly show up at top again

        if rand_number == 3:    
            for up_button_number in range(len(upbutton)):
                if upbutton[up_button_number].x > 0: # meaning it is on the screen
                    upbutton[up_button_number].move(upbutton[up_button_number].x, upbutton[up_button_number].y + constants.BUTTON_SPEED)
                    if upbutton[up_button_number].y > constants.SCREEN_Y:
                        upbutton[up_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_upbutton() # make it randomly show up at top again

        if rand_number == 4:    
            for down_button_number in range(len(downbutton)):
                if downbutton[down_button_number].x > 0: # meaning it is on the screen
                    downbutton[down_button_number].move(downbutton[down_button_number].x, downbutton[down_button_number].y + constants.BUTTON_SPEED)
                    if downbutton[down_button_number].y > constants.SCREEN_Y:
                        downbutton[down_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_downbutton() # make it randomly show up at top again

        if rand_number == 5:    
            for left_button_number in range(len(leftbutton)):
                if leftbutton[left_button_number].x > 0: # meaning it is on the screen
                    leftbutton[left_button_number].move(leftbutton[left_button_number].x, leftbutton[left_button_number].y + constants.BUTTON_SPEED)
                    if leftbutton[left_button_number].y > constants.SCREEN_Y:
                        leftbutton[left_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_leftbutton() # make it randomly show up at top again

        if rand_number == 6:    
            for right_button_number in range(len(rightbutton)):
                if rightbutton[right_button_number].x > 0: # meaning it is on the screen
                    rightbutton[right_button_number].move(rightbutton[right_button_number].x, rightbutton[right_button_number].y + constants.BUTTON_SPEED)
                    if rightbutton[right_button_number].y > constants.SCREEN_Y:
                        rightbutton[right_button_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        show_rightbutton() # make it randomly show up at top again
        # redraw sprite list
        game.render_sprites(sprites + abutton + bbutton + upbutton + downbutton + leftbutton + rightbutton)
        game.tick()  # wait until refresh rate finishes

def game_over_scene(final_score):
   # this function is the game over scene
    # an image bank for CircuitPython
    image_bank_3 = stage.Bank.from_bmp16("jungle_joe.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text0 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text0.move(22, 20)
    text0.text("Final Score: {:0>2d}".format(final_score))
    text.append(text0)

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text1.move(43, 60)
    text1.text("GAME OVER")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    text2.move(32, 110)
    text2.text("PRESS SELECT")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic
        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_SELECT != 0:  # Start button
            keys = 0
            main_menu_scene()
            #break

if __name__ == "__main__":
    blank_white_reset_scene()