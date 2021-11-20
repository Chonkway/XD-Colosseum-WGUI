from math import trunc
import PySimpleGUI as sg
from subprocess import STDOUT, Popen, TimeoutExpired, check_output, PIPE, run



class Menu():
    """
    A simple menu class that serves to pass in the subprocess, events and values from the main window into menu functions
    """
    def __init__(self, process, event, value):
        self.process = process
        self.event = event
        self.value = value


#// Currently has a bug where it inputs an '8' into the randomizer selection for some reason?
    def RandomMenu(self):
        """
        Function for accessing and using the Randomizer Menu.

        Returns a dict of form {option_index:bool}, checks the bool value and then applies the options by writing to buffer then flushing
        """
        print('8', file=self.process.stdin)
        self.process.stdin.flush()

        if self.event == "Go!":
            for i in self.value:
                if self.value[i] == True:
                    print(int(float(i)), file=self.process.stdin)       #// Each option requires a unique key, I've opted to create floats to create similar numerical keys that are still unique
                    self.process.stdin.flush()

            print("start", file=self.process.stdin)
            self.process.stdin.flush()

            print("", file=self.process.stdin)
            self.process.stdin.flush()

    def EditingMenu(self):
        """
        Handles options for Rebuilding, Deleting, Listing and Adding Files and Data Tables
        """

        if self.event == 'Rebuild':
            print('1', file=self.process.stdin)
            self.process.stdin.flush()
            confirmation = sg.PopupYesNo('This will overwrite the current ISO. Do you still wish to continue?')
            print(confirmation[0], file=self.process.stdin)
            self.process.stdin.flush()

        if self.event == 'Delete':
            print('2', file=self.process.stdin)
            self.process.stdin.flush()
        if self.event == 'List':                #// PandasGUI
            print('3', file=self.process.stdin)
            self.process.stdin.flush()
        if self.event == 'Add':
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

        if self.event == 'DataTables':         #// PandasGUI
            sg.Popup('This function does not work quite yet...sorry')
    
    def UtilityMenu(self):#// Not sure what the exit screen is like after this is finished, need to let it run

        print('7', file=self.process.stdin) #// Access Menu
        self.process.stdin.flush()
        
        if self.event == "ExtractAll":
            print('1', file=self.process.stdin)
            self.process.stdin.flush()
        if self.event == "DolphinExtractAll":
            print('2', file=self.process.stdin)
            self.process.stdin.flush()
        if self.event == "NPC10":
            print('3', file=self.process.stdin)
            self.process.stdin.flush()
        if self.event == "NPC20":
            print('4', file=self.process.stdin)
            self.process.stdin.flush()
        if self.event == "NPC50":
            print('5', file=self.process.stdin)
            self.process.stdin.flush()
    
    def PatchMenu(self):
        """
        Patches menu keys are simply integers that coorespond to the patch.
        """
        
        print('6', file=self.process.stdin)
        self.process.stdin.flush()

        print(self.event, file=self.process.stdin)
        self.process.stdin.flush()
        
    def ImportExportMenu(self):
        """

        """
        print('4', file=self.process.stdin)
        self.process.stdin.flush()
            
        print(str(self.event), file=self.process.stdin)

