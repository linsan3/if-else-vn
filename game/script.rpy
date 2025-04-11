# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("???")
#define r = Character(roomie, color="#3bceba")
define r = Character("[roomie]")
define y = Character("[povname]", color="#ffdf27")
#define company = Character("geneSYS", color="#3bceba")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #ASK ANI IF YOU NEED HELP !!!

    #with fade -> fade to black
    #with dissolve -> blends scenes
    #naming an image with no file will result in a grey screen
    #scene black is a black screen
    #return ends the entire game
    #\"visual novel?\" allows quotation marks to be used in dialogue
    #{b}Bad Ending{/b}. bolds text
    #USE BRACKETS...... for python variables that can be changed
    # use python: OR $ for python elements
    # jump can be used with or without a menu (pure dialogue)

    # show bottom_bar with dissolve
    # show top_bar with dissolve

    scene background_pattern
    with fade
    
    show top_bar at top with dissolve
    show basic_badge behind top_bar with dissolve
    
    python:
        roomie = "R0-Mi"
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "MC"

    y "My name is [povname]!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene train_bg
    with dissolve
    show top_bar at top with dissolve

    "Oh look, the city! A whole new life awaits for me there."

    "I recently accepted a job as a new engineer at one of the top companies in the world: {color=#0000ffff}geneSYS{/color}."

    "Truth be told, I'm actually quite scared... I have no idea what to expect..."

    "I'm sure everything will be okay, though!"

    "I wonder how much longer this train ride will take..."

    scene apartment_inside
    with dissolve
    show top_bar at top with dissolve #make separate top bars?

    show romi at left
    with dissolve 

    # These display lines of dialogue.
    "You open the door to your new apartment. Someone is there to greet you."

    show romi at center
    with moveinright

    m "Hey, how's it going? You must be [povname]!"

    m "You must be the new guy at {color=#0000ffff}geneSYS{/color}, right?"

    r "My name is R0-Mi, but you can also call me Rommie!"

    menu:
        r "Do you have a preference on what my name looks like?"

        "Rommie":
            $ roomie = "Rommie"
            r "Okay, it'll look like this from now on!"
        "R0-Mi":
            $ roomie = "R0-Mi"
            r "Glad you like it the way it is!"    

    menu:
        "Do you have something to say?"

        "I think you're really cool.":
            jump cool
        "(You have nothing to say.)":
            jump leave

# #good ending
label cool:

    scene r0mi_test with dissolve
    hide romi with dissolve

    r "I think you are too! We should totally kiss..."
    r "(I am lying. My programming does not have the properties to support this action.)"

    jump restart

# #bad ending
label leave:
    y "..."
    r "Okay well anyways I gotta go bye!!"
    "You missed your opportunity to kiss a robot... maybe next time?"

    jump restart

#go back to the beginning
label restart:

    scene ending
    with fade

    "You have reached the end of the game, thanks for playing!"

    menu:
        "Would you like to restart?"

        "Yes":
            jump start
        "No":
            return