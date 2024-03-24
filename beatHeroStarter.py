from SimpleGame.simplegame import *
from random import choice

BEAT_DIRECTIONS = ['up', 'down', 'left', 'right']

generation_speed = 0.6
movement_speed = 3


#Game variables
game_ended = False
game_started = False
frame_counter = 0

# Use the following list to keep track of all your beats.
beatList = []
timeleft = 30
score = 0
clock = create_element("timer", (WIDTH-50,50))
scoreElement = create_element('blackbox', (50,50))
dir_arrow = create_element("arrow-key", (WIDTH/2, HEIGHT-50))
dir_arrow['baseImage'] = 'arrow-key'



def draw():
    """
    - Called automatically everytime there's a change in the screen
    - Do not include any operations other than drawing inside this function.
    - The only allowed statements/functions are the ones that have draw_ in the name like
    draw_background_image(), draw_element(), etc
    """

    # You may set different background for each step!
    draw_background('background4')
    if not game_started:
        # What you want to show *before* the game starts goes here. eg 'Press Space to Start!'
        draw_text_on_screen('press Space to Start!', (WIDTH / 2, HEIGHT / 2), color='black')

    elif game_ended:
        # What you want to show *after* the game ends goes here. eg 'You Scored x Beats!'
        draw_text_on_screen('Game Over! Your Score: ' + str(len(beatList)), (WIDTH / 2, HEIGHT / 2), color='black')

    else:
        # What you want to show *during* the game goes here. e.g. beats, timer, etc
        draw_element(beatList[0])
        draw_element(scoreElement)
        draw_text_on_screen(str(score), (50, 50))
        draw_element(clock)
        draw_text_on_screen(str(timeleft), (WIDTH-50, 50))
        draw_element(dir_arrow)

        # What you want to show *during* the game goes here. e.g. beats, timer, etc
        for beat in beatList:
            draw_element(beat)



def update():
    """
    - Called automatically 60 times per second (every 1/60th of a second) to
    maintain a smooth frame rate of 60 fps.
    - Ideal for game logic e.g. moving objects, updating score, and checking game conditions.
    """
    # The frame counter keeps track of which frame we're on, this can be helpful for
    # operations that are time sensitive. You may also use the callback functions instead of
    # using the frame_counter.

    global frame_counter, game_ended, timeleft
    frame_counter += 1
    if frame_counter % 60 == 0:
        timeleft -= 1
    if timeleft == 0:
        end_game()

    # Uncomment the following line and see what happens when you run the program
    #print(f'{frame_counter/60:.1f}')

    if not game_started:
        # Game logic if any *before* the game starts.
        pass
    elif game_ended:
        # Game logic if any *after* the game ends.
        pass
    else:
        # Game logic if any *during* the game.
        # Move the beat 3 pixels down.
        # Try changing the number and see what happens!
        if beatList[0]['isMoving']:
            move_by_offset(beatList[0], (0, 3))



def on_key_down(key):
    """
    Called when a key is pressed on the keyboard.
    - Do not use this function for game logic.

    Parameters:
    - key: An integer representative of the key that was pressed.
    In order to get a str value of the key pressed, use get_key() instead.
    """

    key_pressed = get_key_pressed(key)
    if key_pressed == 'space' and not game_started:
        start_game()

    if key_pressed in BEAT_DIRECTIONS:
        if key_pressed == "right":
            rotate_by(dir_arrow, 90)






def start_game():
    # user-defined function
    # only put logic that'll happen once when the game starts
    global game_started
    game_started = True
    manage_background_music('winter', 'play')
    generate_beat()


def end_game():
    # user-defined function
    global game_ended
    game_ended = True


def generate_beat():
    # user-defined function
    # To make an arrow that is pointing right
    beatDirection = choice(BEAT_DIRECTIONS)
    beat = create_element('arrow-orange', centerPos=(WIDTH / 2, 0))
    rotate_by(beat, 90)
    beat['side'] = choice([-1, 1])
    beat['direction'] = beatDirection
    beat['scoreStatus'] = ''
    beat['isMoving'] = True
    beatList.append(beat)

# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # DO NOT REMOVE THIS LINE!! # # # # # # # #
run_game()
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
