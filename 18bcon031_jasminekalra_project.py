# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:13:45 2020

@author: HP
"""

        
        # import random module and pygame
import pygame      
import numpy as np 
from time import sleep 
import random 
print("welcome to Jasmine's gaming hub,we have 3 games for you ")
kk=input("what is your name")
print(" press 1 for rock paper scissor \n 2 for Hangman game \n 3 for snake game")
choice1=input("okay so "+kk+" please enter choice")

if(choice1=="1"):
    print("rock blunts scissor") 
    print("paper cover rock\n scissor cut paper")
    while True: 
    	print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 
    	
    	# take the input 
    	choice = int(input("User turn: ")) 
    
    	
    	while choice > 3 or choice < 1: 
    		choice = int(input("enter valid input: ")) 
    		
    
    	# initialize value  
    
    	if choice == 1: 
    		choice_name = 'Rock'
    	elif choice == 2: 
    		choice_name = 'paper'
    	else: 
    		choice_name = 'scissor'
    		
    	# print user choice 
    	print("user choice is: " + choice_name) 
    	print("\n its computer turn") 
    
    	# Computer chooses randomly any number 
   
    	comp_choice = random.randint(1, 3) 
    	
    	# looping until comp_choice value  is equal to the choice value 
    	while comp_choice == choice: 
    		comp_choice = random.randint(1, 3) 
    
    	
    	if comp_choice == 1: 
    		comp_choice_name = 'Rock'
    	elif comp_choice == 2: 
    		comp_choice_name = 'paper'
    	else: 
    		comp_choice_name = 'scissor'
    		
    	print("Computer choice is: " + comp_choice_name) 
    
    	print(choice_name + " V/s " + comp_choice_name) 
    
    	# condition for winning 
    	if((choice == 1 and comp_choice == 2) or
    	(choice == 2 and comp_choice ==1 )): 
    		print("paper wins ", end = "") 
    		result = "paper"
    		
    	elif((choice == 1 and comp_choice == 3) or
    		(choice == 3 and comp_choice == 1)): 
    		print("Rock wins", end = "") 
    		result = "Rock"
    	else: 
    		print("scissor wins", end = "") 
    		result = "scissor"
    
    	# Printing either user or computer wins 
    	if result == choice_name: 
    		print("User wins\n ") 
    	else: 
    		print(" Computer wins") 
    		
    	print("Do you want to play again? (Y/N)") 
    	answer = input() 
    
    
    	# if user input n or N then condition is True 
    	if answer == 'n' or answer == 'N': 
    		break
    	
    
    print("\nThanks for playing") 

elif(choice1=="2"):
      
    print("Good Luck ! ", kk) 
      
    word = ['CAR', 'world', 'science', 'programming',  
             'python', 'mathematics', 'player', 'condition',  
             'happy', 'water', 'board', 'Food']  
      
    print("Guess the characters") 
      
    guesses = '' 
      
    # any number of turns can be used here 
    turns = 12
      
      
    while turns > 0: 
          
        # counts the number of times a user fails 
        failed = 0
          
        # all characters from the input 
        # word taking one at a time. 
        for char in word:
            
              
            # comparing that character with 
            # the character in guesses 
            if char in guesses:  
                print(char) 
                  
            else:  
                print("_") 
                  
                # for every failure 1 will be 
                # incremented in failure 
                failed += 1
                  
      
        if failed == 0: 
            
            print("You Win")  
            print("The word is: ", word)  
            break
          
        #
        # it will ask user to enter another alphabet 
        guess = input("guess a character:") 
          
        # every input character will be stored in guesses  
        guesses += guess  
          
        # check input with the character in word 
        if guess not in word: 
              
            turns -= 1
              
            print("Wrong") 
              
           
            print("You have", + turns, 'more guesses') 
              
              
            if turns == 0: 
                print("You Loose") 
   
elif(choice1=="3"):


#initialize all imported pygame modules

    pygame.init()
    
    #rgb format of colors 
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 155, 0)
    RED = (255, 0, 0)
    CYAN = (0, 255, 255)
    DARK_CYAN = (123, 104, 238)
    YELLOW = (247, 255, 0)
    
    #giving game titles  
    game_title = 'game'
    display_width = 800#deciding width and height of display
    display_height = 600
    background_color = BLACK
    snake_color = DARK_CYAN#declaring colour of snake 
    energy_color = DARK_CYAN#declaring colour of engery or fruit 
    polygon_powerup_color = (random.randrange(255), random.randrange(255), random.randrange(255))#after eating energy colour of display changes
    
    game_display = pygame.display.set_mode((display_width, display_height)) #setting up
    pygame.display.set_caption(game_title)
    
    global block_size #decarling block size
    block_size = 10
    
    clock = pygame.time.Clock()#create an object to help track time
    
    font = pygame.font.SysFont(None, 25)#create a Font object from the system fonts
    
    #defining a function for collision when i get hits by walls of the block
    def get_collision(p_x, p_y, target_x, target_y, width, height):
        if p_x >= target_x and p_x <= target_x + width:
            if p_y >= target_y and p_y <= target_y + height:
                return True
        return False
    
    #defining function for drawing shape of bombs 
    def draw_bombs(b_x, b_y, bw, bh):
        pygame.draw.rect(game_display, YELLOW, [b_x[0], b_y[0], bw, bh])
        pygame.draw.rect(game_display, YELLOW, [b_x[1], b_y[1], bw, bh])
        pygame.draw.rect(game_display, YELLOW, [b_x[2], b_y[2], bw, bh])
        pygame.draw.rect(game_display, YELLOW, [b_x[3], b_y[3], bw, bh])
    
    #
    def set_by_bounds(item_x, item_y, width, height):
        if item_x >= display_height or item_y <= 0:
            item_x = [random.randrange(0, display_width - block_size),
                      random.randrange(0, display_width - block_size),
                      random.randrange(0, display_width - block_size),
                      random.randrange(0, display_width - block_size),
                      random.randrange(0, display_width - block_size)]
            item_y = [0, 0, 0, 0]
        return item_x, item_y
    
    #defining colour of snake and its shape and height
    def snake(width, height, snakelist):
        for x_and_y in snakelist:
            pygame.draw.rect(game_display, snake_color, [x_and_y[0], x_and_y[1], width, height])
            pygame.draw.rect(game_display, WHITE, [x_and_y[0] + 2, x_and_y[1] + 2, width, height])
    
    #creating bomb
    def create_bombs(amount):
        bomb_x = list()
        bomb_y = list()
        for am in range(amount):
            bomb_x.append(random.randrange((display_width - block_size) - 30))
            bomb_y.append(30)
    
    #defining message that appears on the screen
    def message_to_screen(msg, color):
        screen_text = font.render(msg, True, color)
        game_display.blit(screen_text, [200, 300])
    
    #function to display score
    def display_score(score):
        screen_text = font.render(score, True, YELLOW)
        game_display.blit(screen_text, [50, 50])
    
    #game_loop for working og game
    def game_loop():
        
        fps = 30
    
        block_size = 10#size of block 
    
        running = True
        game_over = False
    
        lead_x = display_width / 2
        lead_y = display_height / 2
        lead_x_change = 0
        lead_y_change = 0
    
        powerup_x = 0
        powerup_y = 0
    
        snake_list = list()
        snake_length = 1
    
        rand_apple_x = round(random.randrange(0, display_width - block_size) / float(block_size)) * block_size + block_size
        rand_apple_y = round(random.randrange(0, display_height - block_size) / float(block_size)) * block_size + block_size
    
        score = 0
        score_add = 10
    
        # BOMBS
    
        # UP BOMBS
        up_bombs_x = [random.randrange(0, display_width - block_size),
                      random.randrange(0, display_width - block_size),
                      random.randrange(0, display_width - block_size),
                      random.randrange(0, display_width - block_size)]
    
        up_bombs_y = [0,
                      0,
                      0,
                      0]
    
        # DOWN BOMBS
        down_bombs_x = [random.randrange(0, display_width - block_size),
                        random.randrange(0, display_width - block_size),
                        random.randrange(0, display_width - block_size),
                        random.randrange(0, display_width - block_size)]
    
        down_bombs_y = [display_height,
                        display_height,
                        display_height,
                        display_height]
    
        # LEFT BOMBS
        left_bombs_x = [0,
                        0,
                        0,
                        0]
    
        left_bombs_y = [random.randrange(0, display_height - block_size),
                        random.randrange(0, display_height - block_size),
                        random.randrange(0, display_height - block_size),
                        random.randrange(0, display_height - block_size)]
    
        # RIGHT BOMBS
        right_bombs_x = [display_width,
                         display_width,
                         display_width,
                         display_width]
    
        right_bombs_y = [random.randrange(0, display_height - block_size),
                         random.randrange(0, display_height - block_size),
                         random.randrange(0, display_height - block_size),
                         random.randrange(0, display_height - block_size)]
    
        background_color = (random.randrange(255), random.randrange(255), random.randrange(255))
    
        while running:
            while game_over:
                game_display.fill(background_color)
                message_to_screen('Game over. Press R to restart or Q to quit.', DARK_CYAN)
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            running = False
                            game_over = False
                        if event.key == pygame.K_r:
                            game_loop()
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # Key handling
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        lead_x_change = block_size
                        lead_y_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        lead_y_change = -block_size
                        lead_x_change = 0
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        lead_y_change = block_size
                        lead_x_change = 0
                    elif event.key == pygame.K_f:
                        block_size += 10
                    elif event.key == pygame.K_e:
                        block_size -= 10
            # Map limits
            if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                game_over = True
    
            lead_x += lead_x_change
            lead_y += lead_y_change
    
            up_bombs_y[0] += block_size
            up_bombs_y[1] += block_size
            up_bombs_y[2] += block_size
            up_bombs_y[3] += block_size
    
            left_bombs_x[0] += block_size
            left_bombs_x[1] += block_size
            left_bombs_x[2] += block_size
            left_bombs_x[3] += block_size
    
            down_bombs_y[0] -= block_size
            down_bombs_y[1] -= block_size
            down_bombs_y[2] -= block_size
            down_bombs_y[3] -= block_size
    
            right_bombs_x[0] += block_size
            right_bombs_x[1] += block_size
            right_bombs_x[2] += block_size
            right_bombs_x[3] += block_size
    
            powerup_x += 5
            powerup_y += 5
    
            # Clean state
            game_display.fill(background_color)
            
            
            # Draw
     
            pygame.draw.rect(game_display, energy_color, [rand_apple_x, rand_apple_y, block_size, block_size])
            draw_bombs(up_bombs_x, up_bombs_y, block_size, block_size);
    
            if 200:
                pygame.draw.rect(game_display, YELLOW, [left_bombs_x[0], left_bombs_y[0], block_size, block_size])
                pygame.draw.rect(game_display, YELLOW, [left_bombs_x[1], left_bombs_y[1], block_size, block_size])
                pygame.draw.rect(game_display, YELLOW, [left_bombs_x[2], left_bombs_y[2], block_size, block_size])
                pygame.draw.rect(game_display, YELLOW, [left_bombs_x[3], left_bombs_y[3], block_size, block_size])
                if score >= 300:
                    pygame.draw.rect(game_display, YELLOW, [down_bombs_x[0], down_bombs_y[0], block_size, block_size])
                    pygame.draw.rect(game_display, YELLOW, [down_bombs_x[1], down_bombs_y[1], block_size, block_size])
                    pygame.draw.rect(game_display, YELLOW, [down_bombs_x[2], down_bombs_y[2], block_size, block_size])
                    pygame.draw.rect(game_display, YELLOW, [down_bombs_x[3], down_bombs_y[3], block_size, block_size])
                    if score >= 500:
                        pygame.draw.rect(game_display, YELLOW, [right_bombs_x[0], right_bombs_y[0], block_size, block_size])
                        pygame.draw.rect(game_display, YELLOW, [right_bombs_x[1], right_bombs_y[1], block_size, block_size])
                        pygame.draw.rect(game_display, YELLOW, [right_bombs_x[2], right_bombs_y[2], block_size, block_size])
                        pygame.draw.rect(game_display, YELLOW, [right_bombs_x[3], right_bombs_y[3], block_size, block_size])
    
            pygame.draw.circle(game_display, DARK_CYAN, [powerup_x, powerup_x], 10)
    
            while len(snake_list) > 2:
                del snake_list[0]
    
            snake_head = list()
            snake_head.append(lead_x)
            snake_head.append(lead_y)
            snake_list.append(snake_head)
    
            if len(snake_list) > snake_length:
                del snake_list[0]
    
            snake(block_size, block_size, snake_list)
            display_score('Score: ' + str(score))
            pygame.display.update()
    
            # --------------- COLLISION -----------------------
    
            # BOMBS COLLISION
            for index in range(len(up_bombs_x) - 1):
                if get_collision(lead_x, lead_y, up_bombs_x[index], up_bombs_y[index], block_size, block_size):
                    game_over = True
            for index in range(len(left_bombs_x) - 1):
                if get_collision(lead_x, lead_y, left_bombs_x[index], left_bombs_y[index], block_size, block_size):
                    game_over = True
    
            # APPLE COLLISION
            if get_collision(rand_apple_x, rand_apple_y, lead_x, lead_y, block_size, block_size):
                rand_apple_x = round(random.randrange(0, display_width - block_size) / block_size) * block_size
                rand_apple_y = round(random.randrange(0, display_height - block_size) / block_size) * block_size
                snake_length += 1
                score += score_add
                display_score(str(score))
                background_color = (random.randrange(255), random.randrange(255), random.randrange(255))
            # POWER-UP COLLISION
            if get_collision(powerup_x, powerup_y, lead_x, lead_y, block_size * 2, block_size * 2):
                score += 50
                powerup_x = 1000
                powerup_y = 1000
    
            # CHECK IF OUT OF BOUNDS
            if up_bombs_y[0] >= display_height + 200 or up_bombs_y[0] <= 0:
                up_bombs_x = [random.randrange(0, display_width - block_size),
                              random.randrange(0, display_width - block_size),
                              random.randrange(0, display_width - block_size),
                              random.randrange(0, display_width - block_size),
                              random.randrange(0, display_width - block_size)]
                up_bombs_y = [0, 0, 0, 0]
    
            if left_bombs_x[0] >= display_width + 200 or left_bombs_y[0] <= 0:
                left_bombs_y = [random.randrange(0, display_width - block_size * 2),
                                random.randrange(0, display_width - block_size * 2),
                                random.randrange(0, display_width - block_size * 2),
                                random.randrange(0, display_width - block_size * 2),
                                random.randrange(0, display_width - block_size * 2)]
                left_bombs_x = [0, 0, 0, 0]
    
            if down_bombs_y[0] <= -300:
                down_bombs_x = [random.randrange(0, display_width - block_size),
                                random.randrange(0, display_width - block_size),
                                random.randrange(0, display_width - block_size),
                                random.randrange(0, display_width - block_size),
                                random.randrange(0, display_width - block_size)]
                down_bombs_y = [display_height, display_height, display_height, display_height]
            # ------------------------------------
    
            # POWER-UP POSITION RANDOMIZATION
            random_spawn_powerup = random.randrange(1000)
            if powerup_x >= display_width or powerup_y >= display_height:
                if random_spawn_powerup == 3:
                    powerup_x = 0
                    powerup_y = 0
            clock.tick(fps)
    
        pygame.quit()
        quit()
    
    
    game_loop()

print("Thank you for playing,come soon next time :P")
    
        