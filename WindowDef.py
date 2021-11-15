import PySimpleGUI as sg



"""
Stores window layouts to keep main code tidy. 
"""

#---Menu Definition---#
menu_def = [
    ['Help', ['About...']]
]

#---Customizable Theme---#

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
sg.theme('MyCreatedTheme') # // Edit Theme
#---

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
[sg.Output(size=(50,10), key='-OUTPUT-',)],
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
[sg.Button("Go!", tooltip="Apply Randomizer Settings")],
[sg.Output(size=(50,10), key='-OUTPUT-')],

]

#---Window for Patches---#
patchmenu = [

[sg.Menu(menu_def, tearoff=True)],
[sg.Button("1 - Remove foreign language text", tooltip="USA Version Only")],
[sg.Button("2 - Gen IV physical/special split", tooltip="Will also set moves to their default category")], 
[sg.Button("3 - Remove physical/special split")], 
[sg.Button("4 - Disable select save file checks", tooltip="Can help prevent save file from corrupting")],
[sg.Button("5 - Infinite Use TMs", tooltip="Allows for TMs to be reused indefinitely like in more recent generations")], 
[sg.Button("6 - Allow female starter Pokemon")],
[sg.Button("7 - Allow player to have 2 starters")], 
[sg.Button("8 - Revert to player having 1 starter")], 
[sg.Button("9 - Fix shiny glitch", tooltip="Allows Pokemon to be shiny in XD")], 
[sg.Button("10 - Revert to default shiny behavior", tooltip="Removes the ability for a Pokemon to be shiny in XD")],
[sg.Button("11 - Allow Shadow Pokemon to be shiny")],
[sg.Button("12 - Never allow Shadow Pokemon to be shiny")], 
[sg.Button("13 - Always make Shadow Pokemon Shiny")], 
[sg.Button("14 - Trade evolutions happen at level 40", tooltip="Allows evolutions that would require trade to be a normal event at level 40")],
[sg.Button("15 - Stone evolutions happen at level 40", tooltip="Allows evolutions that would require a stone to be a normal event at level 40")], 
[sg.Button("16 - Enable Debug Logs", tooltip="Only useful for development purposes")],
[sg.Button("17 - All Pokemon can learn any TM")], 
[sg.Button("18 - All Pokemon catch rates set to 255")],

[sg.Button("19 - EV total above 510", tooltip="Allows you to exceed the typical 510 stat EV total")], 
[sg.Button("20 - Gen 7+ crit chance", tooltip="Changes the crit probability to the stage formula used in later generations")], 
[sg.Button("21 - Set all battles to single battles")],
[sg.Button("22 - Set all battles to double battles")], 
[sg.Button("23 - Make engine treat ??? as normal", tooltip="A ??? type in the game will be treated as normal type in the battle engine")],
[sg.Output(size=(50,10), key='-OUTPUT-')],
[sg.Button("Exit")],
]

