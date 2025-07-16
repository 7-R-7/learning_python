import random
import curses

# create screen
screen = curses.initscr()

# hide the mouse
curses.curs_set(0)

# getmax screen height and width
screen_height, screen_width = screen.getmaxyx()

# create a new window
window = curses.newwin(screen_height, screen_width, 0, 0)

# allow window to receive input from the keyboard 
window.keypad(1)

# set the delay for updating the screen
window.timeout(100)

# set the coordinates 
snk_x = screen_width // 4 #int div
snk_y = screen_height // 2

# define position of the snake
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# create the food
food = [screen_height // 2, screen_width // 2]

# add the food
window.addch(food[0], food[1], curses.ACS_PI)

# set direction to right
key = curses.KEY_RIGHT

# create game loop
while True :
    
    # get the next key
    next_key = window.getch()
    
    #key remians the same if there is no input
    key = key if next_key == -1 else next_key
    
    # check if the snake collided with the wall or itself
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        curses.endwin() # close the window
        quit() # quit the program
        
    # set the new position bqsed on direction
    new_head = [snake[0][0], snake[0][1]]
    
    if key == curses.KEY_DOWN:
        new_head[0] += 1
        
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
         new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
        
    # insert the new head
    snake.insert(0, new_head)
    
    # check if the snake ate the food
    
    if snake[0] == food :
        food = None # remove food if snake ate it
        while food is None : 
            new_food = [
                random.randint(1, screen_height-1),
                random.randint(1, screen_width-1)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else :
        # remove last segment of snake
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')
    
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
    