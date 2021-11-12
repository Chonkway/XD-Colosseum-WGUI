from inspect import Parameter
from math import trunc
from random import Random
import subprocess
from sys import stdin, stdout
import sys
from tkinter.constants import TRUE
import PySimpleGUI as sg
import os
import pathlib
from subprocess import STDOUT, Popen, TimeoutExpired, check_output, PIPE, run
from PySimpleGUI.PySimpleGUI import ToolTip
from numpy.core.fromnumeric import std


sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#3b4071',
										'TEXT': '#FFCC66',
										'INPUT': '#339966',
										'TEXT_INPUT': '#000000',
										'SCROLL': '#99CC99',
										'BUTTON': ('#003333', '#FFCC66'),
										'PROGRESS': ('#D1826B', '#CC8019'),
										'BORDER': 1, 'SLIDER_DEPTH': 0,
'PROGRESS_DEPTH': 0, }

#--
tool_path = os.path.join(pathlib.Path(__file__).parent.resolve())
sg.theme('MyCreatedTheme') # // Edit Theme

#---

#---Menu Definition---#
menu_def = [
    ['Help', ['About...']]
]

#---Layout of Main Window---#
layout = [
[sg.Menu(menu_def, tearoff=True)],
[sg.Text('Pokemon XD GoD/Colosseum Tool GUI Test', size=(40, 1), justification='center', font=("Impact", 15), relief=sg.RELIEF_FLAT)],

[sg.Button("Import/Export Files", tooltip="Use this to export files for manual editing and reimport them")],
[sg.Button("Add File", tooltip="Add a file into the ISO")], 
[sg.Button("Patches", tooltip="Apply patches to the ISO")], 
[sg.Button("Utilities", tooltip="Useful code functions for editing the game")],
[sg.Button("Randomizer", tooltip="Select options to randomize the ISO (Rebuild ISO after this)")], 
[sg.Button("Data Tables", tooltip="Export, Import or Document game data such as Pokemon stats")],
[sg.Button("Rebuild ISO", tooltip="Rebuild the ISO using files edited in this tool")], 
[sg.Button("Delete Unused Files in ISO.", tooltip="Use this if there is not enough space to rebuild the ISO")], 
[sg.Button("List Files", tooltip="List files in the ISO")], 

[sg.Button("Exit")],

]

#---Window for Utilities---#
utilmenu = [
[sg.Menu(menu_def, tearoff=True)],
[sg.Text('Pokemon XD GoD/Colosseum Utilities', size=(40, 1), justification='center', font=("Impact", 15), relief=sg.RELIEF_FLAT)],

[sg.Button("Extract All Textures")],
[sg.Button("Extract All Textures w/ Dolphin Filenames")],

[sg.Button("Back")]
]

#---Window for Randomizer---#
randommenu = [
[sg.Menu(menu_def, tearoff=True)],
[sg.Text('Pokemon XD GoD/Colosseum Randomizer', size=(40, 1), justification='center', font=("Impact", 15), relief=sg.RELIEF_FLAT)],

[sg.Checkbox("1 - Randomize All Trainer/Wild Pokemon")],
[sg.Checkbox("2 - Randomize Shadow Pokemon Only")],
[sg.Checkbox("3 - Randomize Pokemon Using Similar BST")],
[sg.Checkbox("4 - Randomize Moves")],
[sg.Checkbox("5 - Randomize Pokemon Types")],
[sg.Checkbox("6 - Randomize Abilities")],
[sg.Checkbox("7 - Randomize Pokemon BST")],
[sg.Checkbox("8 - Randmoize Move Types")],
[sg.Checkbox("9 - Randomize TM and Tutor Moves")],
[sg.Checkbox("10 - Randmoize Evolutions")],
[sg.Checkbox("11 - Randomize Battle Bingo")],
[sg.Button("Go!", tooltip="Apply Randomizer Settings")]

]




#--- Window Definitions ---#
window = sg.Window('Pokemon XD/Colosseum Test GUI', layout, alpha_channel=0.95)

window2 = sg.Window('Pokemon XD/Colosseum Test GUI - Utility Window', utilmenu, alpha_channel=0.95)

window3 = sg.Window('Pokemon XD/Colosseum Test GUI - Randomizer Window', randommenu, alpha_channel=0.95)
# ---- 

cmd = "GoD-Tool.exe XDGoD.iso"

process = Popen(cmd, text=True, shell=True, stdin=PIPE)
#--- Window Functions ---#


def UtilityMenu():

    """
    Function for Utility Menu.
    """

    print('7', file=process.stdin) #// Acess Menu

    
    event, value = window2.read() #// Read events
    if event == 'Back':
        print('0', file=process.stdin)
        window2.close()

    if event == "Extract All Textures":
        print('1', file=process.stdin)
        process.stdin.flush
        # sg.popup_no_wait("This may take a while, please be patient.")


    if event == "Extract All Textures w/ Dolphin Filenames":
        print('2', file=process.stdin)

def RandomMenu():
    """
    Function for accessing and using the Randomizer Menu.

    Returns a dict of form {option_index:bool}, checks the bool value and then applies the options by writing to buffer
    """
    print('8', file=process.stdin)

    event, value = window3.read()

    if event == "Go!":
        for i in value:
            if value[i] == True:
                print(str(i), file=process.stdin)
                process.stdin.flush()
        print("start", file=process.stdin)
        process.stdin.flush()
        sg.PopupNoWait("This may take a while, please be patient.")

while True: #// Event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Utilities': #// Open Utility Menu
        UtilityMenu()
    if event == 'Randomizer':
        RandomMenu()
    # if event == "Apply":
        # process.communicate()

window.close()


