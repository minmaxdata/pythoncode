# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

guesses_used = 0
guesses_max = 7
range_max = 100
my_guess = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global guesses_used, my_guess
    my_guess = random.randrange(0, range_max)
    guesses_used = 0
    
    print
    print
    print "New Game. Range is from 0 to", range_max
    print "Number of remaining guesses is", guesses_max - guesses_used
    print


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_max, guesses_max
    
    range_max = 100
    guesses_max = 7
    new_game()
    return None


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_max, guesses_max
    
    range_max = 1000
    guesses_max = 10
    new_game()
    return None

    
def input_guess(guess):
    # main game logic goes here	
    global guesses_used, range_max
    
    guesses_used = guesses_used + 1
    player_guess = float(guess)
    remaining_guesses = guesses_max - guesses_used
   
    if remaining_guesses == -1:
        print
        print "Maximum number of guesses reached.", my_guess
        new_game()
        return None
    
    
    print
    print "Guess was", guess
    print "Number of remaining guesses is", remaining_guesses
    
    
    if player_guess < range_max and player_guess > -1:
        
        if player_guess > my_guess:
            print "Lower!"
        elif player_guess < my_guess:
            print "Higher!"
        elif player_guess == my_guess:
            print "Correct!"
            range_max = 100
            new_game();
    else:      
        print "error"
        
    return None
            
     
        
        
    

    
# create frame
frame = simplegui.create_frame("Guess The Number", 300, 300)


# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter Guess:", input_guess, 200)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
