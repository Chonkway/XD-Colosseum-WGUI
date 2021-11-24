from tkinter import Event
import WinDef
from math import trunc
import PySimpleGUI as sg
from subprocess import STDOUT, Popen, TimeoutExpired, check_output, PIPE, run

class MenuFunction():
    """
    Class made to pass in events, values and the subprocess for use in individual tab menu functions
    """
    def __init__(self, process, event, values) -> None:
        self.process = process
        self.event = event
        self.values = values


    def EditingMenu(self): 
        """
        Handles options for Rebuilding, Deleting, Listing and Adding Files and Data Tables
        """
        if self.event == 'ISORebuild':
            print('1', file=self.process.stdin)
            self.process.stdin.flush()
            confirm = sg.PopupYesNo('This will overwrite the current ISO. Is this OK?')
            if confirm == 'Yes':
                print('Y', file=self.process.stdin)
            else:
                print('N', file=self.process.stdin)
            self.process.stdin.flush()

        if self.event == 'DeleteFiles':
            print('2', file=self.process.stdin)
            self.process.stdin.flush()
        
        if self.event == 'ListFiles':       #// Current plans are to generate a pandas GUI popup or just log the file list to a logfile
            print('3', file=self.process.stdin)
            self.process.stdin.flush()
        
        if self.event == 'AddFiles':
            print('5', file=self.process.stdin)
            self.process.stdin.flush()
            filequery = sg.PopupGetFile('Select the file you wish to add.')
            if filequery == None:
                print('\n', file = self.process.stdin) #// Returns to main menu if file is invalid or user cancels
                print('exit', file=self.process.stdin)
                self.process.stdin.flush()
            else:
                print(filequery, file = self.process.stdin)#// Writes filepath to tool for file addition
                self.process.stdin.flush()
                print('exit', file=self.process.stdin)
                self.process.stdin.flush()



    def RandomMenu(self):       #// Can't figure out where it's happening but it writes in 'Move Types' (8) no matter what

        print(8, file=self.process.stdin)
        self.process.stdin.flush()

        if self.event == 'StartRandomizer':
            for i in self.values:
                if self.values[i] == True:
                    print(int(float(i)), file=self.process.stdin)
                    self.process.stdin.flush()

        print('start', file=self.process.stdin)
        self.process.stdin.flush()
        print('', file=self.process.stdin)
        self.process.stdin.flush()

    def UtilityMenu(self):

        if self.event == 'ExtractAll':
            print(1 , file=self.process.stdin)
            self.process.stdin.flush()
        if self.event == 'DolphinExtractAll':
            print(2 , file=self.process.stdin)
            self.process.stdin.flush()
        if self.event == 'NPC10':
            print(3 , file=self.process.stdin)
            self.process.stdin.flush()
        if self.event == 'NPC20':
            print(4, file=self.process.stdin)
            self.process.stdin.flush()
        if self.event == 'NPC50':
            print(5, file=self.process.stdin)
            self.process.stdin.flush()
    
    def PatchMenu(self):

        print(6, file=self.process.stdin)
        self.process.stdin.flush

        print(self.event, file=self.process.stdin)
        self.process.stdin.flush()

    def ImportExport(self):

        print(4, file=self.process.stdin)
        self.process.stdin.flush()
            
        print(str(self.event).lower(), file=self.process.stdin)
        self.process.stdin.flush()

    def DataTables():
        """
        placeholder, want to read stdout and create popups for datatable information
        """
        pass