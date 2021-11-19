import PySimpleGUI as sg
import _tkinter


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

#// To be reworked for integration into new window style
#---Layout of Main Window---#
layout = [
[sg.Text('Pokemon XD GoD/Colosseum Tool GUI Pre-Build', size=(40, 1), justification='center', font=("Impact", 15), relief=sg.RELIEF_FLAT)],
[sg.Button("Rebuild ISO", tooltip="Rebuild the ISO using files edited in this tool", key='1')],
[sg.Button("Delete Unused Files in ISO.", tooltip="Use this if there is not enough space to rebuild the ISO", key='2')],
[sg.Button("List Files", tooltip="List files in the ISO", key='3')],
[sg.Button("Add File", tooltip="Add a file into the ISO", key='5')], 
[sg.Button("Data Tables", tooltip="Export, Import or Document game data such as Pokemon stats", key='9')],

]


#---Window for Utilities---#
utilmenu = [
[sg.Text('Pokemon XD GoD/Colosseum Utilities', size=(40, 1), justification='center', font=("Impact", 15), relief=sg.RELIEF_FLAT)],

[sg.Button("Extract All Textures", key='1')],
[sg.Button("Extract All Textures w/ Dolphin Filenames", key='2')],
[sg.Button("Increase NPC Levels by 10%", key='3')],
[sg.Button("Increase NPC Levels by 20%", key='4')],
[sg.Button("Increase NPC Levels by 50%", key='5')]
]

#---Window for Randomizer---#
randommenu = [
[sg.Text('Pokemon XD GoD/Colosseum Randomizer', size=(40, 1), justification='center', font=("Impact", 15), relief=sg.RELIEF_FLAT)],

[sg.Checkbox("1 - Randomize All Trainer/Wild Pokemon", key='-1-')],
[sg.Checkbox("2 - Randomize Shadow Pokemon Only", key='-2-')],
[sg.Checkbox("3 - Randomize Pokemon Using Similar BST", key='-3-')],
[sg.Checkbox("4 - Randomize Moves", key='-4-')],
[sg.Checkbox("5 - Randomize Pokemon Types", key='-5-')],
[sg.Checkbox("6 - Randomize Abilities", key='-6-')],
[sg.Checkbox("7 - Randomize Pokemon BST", key='-7-')],
[sg.Checkbox("8 - Randomize Move Types", key='-8-')],
[sg.Checkbox("9 - Randomize TM and Tutor Moves", key='-9-')],
[sg.Checkbox("10 - Randmoize Evolutions", key='-10-')],
[sg.Checkbox("11 - Randomize Battle Bingo", key='-11-')],
[sg.Button("Go!", tooltip="Apply Randomizer Settings")],

]

#---Window for Patches---#
#// There are two menus in order to create two tabs of buttons to fit them on screen.
patchmenutab1 = [
[sg.Button("Remove foreign language text", tooltip="USA Version Only", key='1')],
[sg.Button("Gen IV physical/special split", tooltip="Will also set moves to their default category", key='2')], 
[sg.Button("Remove physical/special split", key='3')], 
[sg.Button("Disable select save file checks", tooltip="Can help prevent save file from corrupting", key='4')],
[sg.Button("Infinite Use TMs", tooltip="Allows for TMs to be reused indefinitely like in more recent generations", key='5')], 
[sg.Button("Allow female starter Pokemon", key='6')],
[sg.Button("Allow player to have 2 starters", key='7')], 
[sg.Button("Revert to player having 1 starter", key='8')], 
[sg.Button("Fix shiny glitch", tooltip="Allows Pokemon to be shiny in XD", key='9')], 
[sg.Button("Revert to default shiny behavior", tooltip="Removes the ability for a Pokemon to be shiny in XD", key='10')],
[sg.Button("Allow Shadow Pokemon to be shiny", key='11')],
]

patchmenutab2 = [
[sg.Button("Never allow Shadow Pokemon to be shiny", key='12')], 
[sg.Button("Always make Shadow Pokemon Shiny",key='13')], 
[sg.Button("Trade evolutions happen at level 40", tooltip="Allows evolutions that would require trade to be a normal event at level 40", key='14')],
[sg.Button("Stone evolutions happen at level 40", tooltip="Allows evolutions that would require a stone to be a normal event at level 40", key='15')], 
[sg.Button("Enable Debug Logs", tooltip="Only useful for development purposes", key='16')],
[sg.Button("All Pokemon can learn any TM", key='17')], 
[sg.Button("All Pokemon catch rates set to 255", key='18')],
[sg.Button("EV total above 510", tooltip="Allows you to exceed the typical 510 stat EV total", key='19')], 
[sg.Button("Gen 7+ crit chance", tooltip="Changes the crit probability to the stage formula used in later generations", key='20')], 
[sg.Button("Set all battles to single battles", key='21')],
[sg.Button("Set all battles to double battles", key='22')], 
[sg.Button("Make engine treat ??? as normal", tooltip="A ??? type in the game will be treated as normal type in the battle engine", key='23')]
]

#// Patches menu creates a TabGroup of two menus to fit all the patches in.
patchmenu = [[sg.TabGroup([[sg.Tab('Page 1', patchmenutab1), sg.Tab('Page 2', patchmenutab2)]], enable_events=True)]
		  ]  

ImpExpMenu = [
# [sg.Menu(menu_def, tearoff=True)],
[sg.Text('Pokemon XD GoD/Colosseum Tool Import/Export Menu', size=(40, 1), justification='center', font=("Impact", 15), relief=sg.RELIEF_FLAT)],

[sg.Frame('Hover over the buttons for an explaination',layout=[
[sg.Button("Export", tooltip="Extract and then decode files from all ISO files")],
[sg.Button("Extract", tooltip="Extract but do not decode files from all ISO files")],
[sg.Button("Decode", tooltip="Decodes previously -extracted- files from all ISO files\n Decoding is used to decompile scripts, extract textures, etc.")],

[sg.Button("Import", tooltip="Encode and then import all ISO files")],
[sg.Button("Insert", tooltip="Import but do not reencode for all ISO files")],
[sg.Button("Encode", tooltip="Encode but do not reimport files for all ISO files")],

[sg.Button("Delete", tooltip="Delete files containing all ISO files")],
[sg.Button("List", tooltip="Lists all ISO files")],
])]

]

#// Makes the main tabgroup easier to read


maintabgrp = [[sg.TabGroup([[sg.Tab('Editing', layout, title_color='Red',border_width =10, background_color='Green',
                                tooltip='Personal details', element_justification= 'center', key='Editing'),
                    sg.Tab('Patch Options', patchmenu, title_color='Blue',background_color='Yellow', element_justification='center', key='Patches'),
					sg.Tab('Import/Export', ImpExpMenu,title_color='Blue',background_color='Yellow', element_justification='center', key='Import/Export'),
					sg.Tab('Randomizer', randommenu, key='Random'),
					sg.Tab('Utilities', utilmenu ,title_color='Blue',background_color='Yellow', key='Utilites'),

                    sg.Button('Close')]], enable_events=True)
]]