import PySimpleGUI as sg


EditingTools = [
[sg.Text('Main Development Options', size=(40, 1), justification='center', font=("Impact", 15), relief=sg.RELIEF_FLAT)],
[sg.Button("Rebuild ISO", tooltip="Rebuild the ISO using files edited in this tool", key='ISORebuild')],
[sg.Button("Delete Unused Files in ISO.", tooltip="Use this if there is not enough space to rebuild the ISO", key='DeleteFiles')],
[sg.Button("List Files", tooltip="List files in the ISO", key='ListFiles')],
[sg.Button("Add File", tooltip="Add a file into the ISO", key='AddFiles')], 
[sg.Button("Data Tables", tooltip="Export, Import or Document game data such as Pokemon stats", key='DataTables')],

]

#---Utility Window---#
utilmenu = [
[sg.Text('Pokemon XD GoD/Colosseum Utility Functions', size=(40, 1), justification='center', font=("Impact", 15), relief=sg.RELIEF_FLAT)],

[sg.Button("Extract All Textures", key='ExtractAll')],
[sg.Button("Extract All Textures w/ Dolphin Filenames", key='DolphinExtractAll')],
[sg.Button("Increase NPC Levels by 10%", key='NPC10')],
[sg.Button("Increase NPC Levels by 20%", key='NPC20')],
[sg.Button("Increase NPC Levels by 50%", key='NPC50')]
]

#---Window for Randomizer---#
randommenu = [
[sg.Text('Pokemon XD GoD/Colosseum Randomizer Options', size=(40, 1), justification='center', font=("Impact", 15), relief=sg.RELIEF_FLAT)],

[sg.Checkbox("Randomize All Trainer/Wild Pokemon", key='1.0')],
[sg.Checkbox("Randomize Shadow Pokemon Only", key='2.0')],
[sg.Checkbox("Randomize Pokemon Using Similar BST", key='3.0')],
[sg.Checkbox("Randomize Moves", key='4.0')],
[sg.Checkbox("Randomize Pokemon Types", key='5.0')],
[sg.Checkbox("Randomize Abilities", key='6.0')],
[sg.Checkbox("Randomize Pokemon BST", key='7.0')],
[sg.Checkbox("Randomize Move Types", key='8.0')],
[sg.Checkbox("Randomize TM and Tutor Moves", key='9.0')],
[sg.Checkbox("Randmoize Evolutions", key='10.0')],
[sg.Checkbox("Randomize Item Boxes", key='11.0')],
[sg.Checkbox("Randomize Battle Bing", key='12.0')],
[sg.Button("Start", tooltip="Apply Randomizer Settings", key='StartRandomizer')],

]

#-------------------------------------------------------------------------------------------------------------------------#
#---Window for Patches---#
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
patchmenu = [[sg.TabGroup([[sg.Tab('Page 1', patchmenutab1), sg.Tab('Page 2', patchmenutab2)]])]
		  ]
#---------------------------------------------------------------------------------------------------------------------#


#---Import/Export Options---#
ImpExpMenu = [
[sg.Text('Pokemon XD GoD/Colosseum Tool Import/Export Menu', size=(40, 1), justification='center', font=("Impact", 15), relief=sg.RELIEF_FLAT)],

[sg.Frame('Hover over the buttons for an explaination',layout=[
[sg.Button("Export", tooltip="Extract and then decode files from all ISO files", key='Export')],
[sg.Button("Extract", tooltip="Extract but do not decode files from all ISO files", key='Extract')],
[sg.Button("Decode", tooltip="Decodes previously -extracted- files from all ISO files\n Decoding is used to decompile scripts, extract textures, etc.", key='Decode')],

[sg.Button("Import", tooltip="Encode and then import all ISO files", key='Import')],
[sg.Button("Insert", tooltip="Import but do not reencode for all ISO files", key='Insert')],
[sg.Button("Encode", tooltip="Encode but do not reimport files for all ISO files", key='Encode')],

[sg.Button("Delete", tooltip="Delete files containing all ISO files", key='Delete')],
[sg.Button("List", tooltip="Lists all ISO files", key='List')],
])]

]


#---Windows for Data Tables---#
#----------------------------------------------------------------------------------------------------------------#
DataTables1 = [
[sg.Button('Battle', key='1.00')],
[sg.Button('Battle Bingo Card', key='2.00')],
[sg.Button('Battle CD', key='3.00')],
[sg.Button('Battle Layout', key='4.00')],
[sg.Button('Battlefield', key='5.00')],
[sg.Button('Character', key='6.00')],
[sg.Button('Character Model', key='7.00')],
[sg.Button('Door', key='8.00')],
[sg.Button('Flags', key='9.00')],
[sg.Button('Interaction Point', key='10.00')],
[sg.Button('Item', key='11.00')]
]
DataTables2 = [

[sg.Button('Mirror B Data', key='12.00')],
[sg.Button('Move', key='13.00')],
[sg.Button('Multiplier', key='14.00')],
[sg.Button('Nature', key='15.00')],
[sg.Button('Pokeface', key='16.00')],
[sg.Button('Pokemon Stats', key='17.00')],
[sg.Button('Pokespot', key='18.00')],
[sg.Button('Pokespot All', key='19.00')],
[sg.Button('Pokespot Caves', key='20.00')],
[sg.Button('Pokespot Oasis', key='21.00')],
[sg.Button('Item', key='22.00')]

]

DataTables3 = [
[sg.Button('Pokespot Rock', key='23.00')],
[sg.Button('Room', key='24.00')],
[sg.Button('Sounds', key='25.00')],
[sg.Button('Sounds Metadata', key='26.00')],
[sg.Button('Trainer Class', key='27.00')],
[sg.Button('Treasure', key='28.00')],
[sg.Button('Tutor Move', key='29.00')],
[sg.Button('Type', key='30.00')],
[sg.Button('Trainer Pokemon DeckData_Story.bin', key='31.00')],
[sg.Button('Trainer Pokemon DeckData_Colosseum.bin', key='32.00')],
]

DataTables4 = [
[sg.Button('Trainer Pokemon DeckData_Hundred.bin', key='33.00')],
[sg.Button('Trainer Pokemon DeckData_Virtual.bin', key='34.00')],
[sg.Button('Trainer Pokemon DeckData_Imasugu.bin', key='35.00')],
[sg.Button('Trainer Pokemon DeckData_Bingo.bin', key='36.00')],
[sg.Button('Trainer Pokemon DeckData_Sample.bin', key='37.00')],
[sg.Button('Shadow Pokemon', key='38.00')],
[sg.Button('Trainer DeckData_Story.bin', key='39.00')],
[sg.Button('Type', key='40.00')],
[sg.Button('Trainer Pokemon DeckData_Story.bin', key='41.00')],
[sg.Button('Trainer Pokemon DeckData_Colosseum.bin', key='42.00')],
[sg.Button('Trainer DeckData_Hundred.bin', key='43.00')],
[sg.Button('Trainer DeckData_Virtual.bin', key='44.00')]
]

DataTables5 = [
[sg.Button('Trainer DeckData_Imasugu.bin', key='45.00')],
[sg.Button('Trainer DeckData_Bingo.bin', key='46.00')],
[sg.Button('Trainer DeckData_Sample.bin', key='47.00')],
[sg.Button('Trainer AI DeckData_Story.bin', key='48.00')],
[sg.Button('Trainer AI DeckData_Colosseum.bin', key='49.00')],
[sg.Button('Trainer AI DeckData_Hundred.bin', key='50.00')],
[sg.Button('Trainer AI DeckData_Virtual.bin', key='51.00')],
[sg.Button('Trainer AI DeckData_Imasugu.bin', key='52.00')],
[sg.Button('Trainer AI DeckData_Bingo.bin', '53.00')],
[sg.Button('Trainer AI DeckData_Sample.bin', key='54.00')]
]

DataTables6 = [
[sg.Button('Ability', key='55.00')],
[sg.Button('PKX Pokemon Model', key='56.00')],
[sg.Button('PKX Trainer Model', key='57.00')],
[sg.Button('Status Effects', key='58.00')],
[sg.Button('TM or HM', key='59.00')],
[sg.Button('Texture', key='60.00')],
[sg.Button('WZX Animation', key='59.00')],
[sg.Button('Colosseum Gift Pokemon', key='61.00')],
[sg.Button('Demo Starter Pokemon', key='62.00')],
[sg.Button('Gift Shadow Pokemon', key='63.00')]

]

DataTables7=[
[sg.Button('Mt. Battle Prize Pokemon', key='64.00')],
[sg.Button('Starter Pokemon', key='65.00')],
[sg.Button('Trades', key='66.00')]
]

#// Similar to Patches, there are far too many DataTable options to fit onto one window
DataTables = [[sg.TabGroup([[sg.Tab('Page 1', DataTables1, key='DataPage1'), sg.Tab('Page 2', DataTables2, key='DataPage2'), 
							sg.Tab('Page 3', DataTables3, key='DataPage3'), sg.Tab('Page 4', DataTables4, key='DataPage4'),
							sg.Tab('Page 5', DataTables5, key='DataPage5'), sg.Tab('Page 6', DataTables6, key='DataPage6'),
							sg.Tab('Page 7', DataTables7, key='DataPage7')
							
					]]
					)
					]]
#---------------------------------------------------------------------------------------------------------#



#---TabGroup that holds every window definition---#
maintabgrp = [[sg.TabGroup([[sg.Tab('Editing', EditingTools, title_color='Blue',tooltip='Personal details', element_justification= 'center', key='EditingTools'),
                    sg.Tab('Patch Options', patchmenu, title_color='Blue', element_justification='center', key='PatchOptions'),
					sg.Tab('Import/Export', ImpExpMenu,title_color='Blue', element_justification='center', key='Import/Export'),
					sg.Tab('Randomizer', randommenu, key='Randomizer'),
					sg.Tab('Utilities', utilmenu , title_color='Blue', key='UtilityMenu'),
					sg.Tab('Data Tables', DataTables ,title_color='Blue', key='AllDataTables')

]], enable_events=True, key='MainMenu')],
[sg.Multiline(enter_submits=False, reroute_stdout=True, reroute_stderr=True)]]

