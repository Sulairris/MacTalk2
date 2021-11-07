import os
import sys
# program settings [0] = highlighting, [1] = voice
settings = ['-i','alex']
# this is so i dont have to type os.system('clear') all the time
def clear():
    os.system('clear')
while True:
    clear()
    # main menu
    print('S: Speak\nR: Read File\nP: Preferences\nQ: Quit\n\n')
    startchoice = raw_input('?')
    # code for speaking
    if startchoice == 's':
        while True:
            os.system('clear')
            print('Type and I will speak\nPress return with an empty line to quit\n\n')
            type = input('?')
            # will break out of loop if the user enters nothing
            if len(type) == 0:
                break
            else:
                # passes users data to the say program with flags set in Preferences
                os.system('say ' + settings[0] + ' -v ' + settings[1] + ' "' + type + '"')
    if startchoice == 'r':
        while True:
            clear()
            print('Please input file name to speak\nType list to list files\npress enter to exit\n\n')
            readfile = input('?')
            if readfile == 'list':
                os.system('ls | say -i -v ' + settings[1])
            if len(readfile) == 0:
                break
            else:
                os.system('say ' + settings[0] + ' -v ' + settings[1] + ' ' + '-f ' + readfile)
    # Preferences
    if startchoice == 'p':
        while True:
            clear()
            # prints what settings can be changed
            print('--PREFERENCES--\n')
            print('-VOICE-\n')
            print('1: Alex(Defult)\n2: Yuri\n')
            print('-HIGHLIGHTING-\n')
            print('H: On\nNH: Off\n')
            print('-CURRENT PREFERENCES-\n')
            print('Voice: ' + settings[1])
            # determines the state of the highlighting setting and prints the state in a user friendly way
            if settings[0] == '-i':
                print('Highlighting: On\n')
            else:
                print('Highlighting: Off\n')
            print('T: Test preferences')
            print('E: Exit\n\n')
            # logic for changing settings
            set = input('?')
            if set == '1':
                settings[1] = 'alex'
            if set == '2':
                settings[1] = 'yuri'
            if set == 'h':
                settings[0] = '-i'
            if set == 'nh':
                settings[0] = ''
            if set == 't':
                os.system('say ' + settings[0] + ' -v ' + settings[1] + ' "Hello my name is ' + settings[1] + ', and this is a test"')
            if set == 'e':
                break
    # quits program
    if startchoice == 'q':
        clear()
        sys.exit()
        # now stop reading my code
