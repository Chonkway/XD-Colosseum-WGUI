from inspect import Parameter
from math import trunc
import subprocess
from sys import stdin, stdout
from tkinter.constants import TRUE
import PySimpleGUI as sg
import os
import pathlib
from subprocess import STDOUT, Popen, check_output, PIPE
from PySimpleGUI.PySimpleGUI import ToolTip


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

[sg.Button("Exit")]

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

]




#--- Window Definitions ---#
window = sg.Window('Pokemon XD/Colosseum Test GUI', layout, alpha_channel=0.95)

window2 = sg.Window('Pokemon XD/Colosseum Test GUI - Utility Window', utilmenu, alpha_channel=0.95)

window3 = sg.Window('Pokemon XD/Colosseum Test GUI - Randomizer Window', randommenu, alpha_channel=0.95)
# ---- 

cmd = "GoD-Tool.exe XDGoD.iso"

process = Popen(cmd, text=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
#--- Window Functions ---#



def UtilityMenu():
    """
    Function for Utility Menu
    """
    process.communicate("7")
    ev2, val2 = window2.read()
    if ev2 == 'Back':
        window2.close()
    if ev2 == "Extract All Textures":
        process.communicate("1")

while True: #// Event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Utilities': #// Open Utility Menu
        UtilityMenu()

window.close()


