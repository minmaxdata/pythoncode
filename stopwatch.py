# template for "Stopwatch: The Game"

import simplegui
# define global variables
milliseconds = 0
total_attempts = 0
wins = 0
single_seconds = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(milliseconds):
    global single_seconds
    time = int(milliseconds)
    
    minutes = time // 600  
    tens_of_seconds = time // 10
    excess_seconds = tens_of_seconds %  60
    leftover_tenths = excess_seconds /10
    single_seconds = excess_seconds % 10
    ms = time % 10
    
    
    formatted_minutes = str(minutes) + ':'
    formatted_ten_seconds = str(leftover_tenths)
    formatted_ones_seconds = str(single_seconds)
    formatted_ms = '.' +str(ms)
    
    return formatted_minutes + formatted_ten_seconds + formatted_ones_seconds + formatted_ms
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    increment()
    timer.start()
    
def stop():
    global total_attempts
    global wins
    global single_seconds
    global running
    total_attempts +=1
   
    if (single_seconds == 0):
        
        wins = wins + 1
        print wins
    
    print wins, single_seconds, single_seconds == 0
    timer.stop()
    
def reset():
    global milliseconds
    global total_attempts
    global wins
    global single_seconds
    
    milliseconds = 0
    total_attempts = 0
    wins = 0
    single_seconds = 0

    
    
# define event handler for timer with 0.1 sec interval
def increment():
    global milliseconds
    milliseconds = milliseconds + 1
    

# define draw handler
def draw(canvas):
    global wins
    global total_attempts
    game = str(wins) + '/' + str(total_attempts)
    canvas.draw_text(format(milliseconds),[125, 100], 24, 'white')
    canvas.draw_text(game,[265, 15], 24, 'red')

    
# create frame
frame = simplegui.create_frame("StopWatch", 300, 200) 


# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Restart", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, increment)


# start frame
frame.start()

# Please remember to review the grading rubric
