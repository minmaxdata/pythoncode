# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global cards,  exposed, state, first_card, second_card, turn
    turn = 0
    state = 0
    cards = range(0,8) + range(0,8)
    exposed = [False] * 16
    first_card = None
    second_card = None
    random.shuffle(cards);
   

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, first_card, second_card, exposed, cards, turn
    card_no = pos[0] // 50
    if (state == 0) :       
        exposed[card_no] = True
        first_card = card_no
        state = 1           
    elif (state == 1) :
        if(exposed[card_no] == False):
            exposed[card_no] = True
            second_card = card_no
            turn += 1
            state = 2   
            label.set_text( "Turns = " + str(turn))

    else :
        if(cards[first_card] != cards[second_card]):
            exposed[first_card] = False
            exposed[second_card] = False            
        first_card =  card_no
        exposed[first_card] = True
        state = 1

# cards are logically 50x100 pixels in size    
def draw(canvas):
 
    for e_index in range(len(exposed)):
        width = 50/2
        if (exposed[e_index] == False) :
            vertical = 50 * e_index
            canvas.draw_line((vertical + width, 1), (vertical + width, 99), 49, 'Green')
        elif (exposed[e_index] == True) :
            card_pos = 50 * e_index
            canvas.draw_text(str(cards[e_index]), [card_pos + 18, 68], 36, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric