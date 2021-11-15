import PySimpleGUI
from subprocess import STDOUT, Popen, TimeoutExpired, check_output, PIPE, run

"""
Stores the menu functions that require their own windows.

Reads and flushes stdin/stdout from subprocess called process. Also holds a function that basically spams 0 a few times to get back to the main menu.
"""

class Menu():
    """
    A simple menu class that takes in two parameters:

        process = subprocess called with Popen

        window = PySimpleGUI window that you wish to open
    """
    def __init__(self, process, window):
        self.process = process
        self.window = window

    def __del__(self):
        """
        Gonna be honest, I don't know what this does but it crashes without this so ¯\_(ツ)_/¯
        """
        self._TKOut.__del__()

    def MainMenu():
        #// Handles navigating main menu
        pass

    def UtilityMenu(self):

        print('7', file=self.process.stdin) #// Acess Menu
        self.process.stdin.flush()
        
        event, value = self.window.read() #// Read events
        print(event, value)

        if event == 'Back':
            print('0', file=self.process.stdin)
            self.process.stdin.flush()
            
        if event == "Extract All Textures":
            print('1', file=self.process.stdin)
            self.process.stdin.flush()

            #// Reads stdout 
            while True:
                line = self.process.stdout.readline()
                print(line)
                if not line: break    
            
        if event == "Extract All Textures w/ Dolphin Filenames":
            print('2', file=self.process.stdin)
            self.process.stdin.flush()

            while True:
                line = self.process.stdout.readline()
                print(line)
                if not line: break 

    def RandomMenu(self):
        """
        Function for accessing and using the Randomizer Menu.

        Returns a dict of form {option_index:bool}, checks the bool value and then applies the options by writing to buffer then flushing
        """
        print('8', file=self.process.stdin)
        self.process.stdin.flush()

        event, value = self.window.read()

        if event == "Go!":
            for i in value:
                if value[i] == True:
                    print(str(i), file=self.process.stdin)
                    self.process.stdin.flush()

            print("start", file=self.process.stdin)
            self.process.stdin.flush()
            #// Generates stdout
            while True:
                line = self.process.stdout.readline()
                print(line)
                if not line: break 
            print("\n", file=self.process.stdin)
            self.process.stdin.flush()

    def PatchesMenu():
        """
        Function for patches
        """


