import PySimpleGUI as sg
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

    # def __del__(self):
    #     """
    #     Gonna be honest, I don't know what this does but it used to crash without this so ¯\_(ツ)_/¯
    #     """
    #     self._TKOut.__del__()


#//////// I am going to need to create a new window for Import/Export
    def MainMenu(self):
        """
        Navigating the main menu. 
        
        This is intended to be called as an 'else' for the main loop for any options that don't require a separate window.
        """
        while True:
            event, value = self.window.read()

            print(str(event[0]), file=self.process.stdin)
            self.process.stdin.flush()

            if str(event[0]) == "1":#// Confirming rebuild
                print(str(event[0]), file=self.process.stdin)
                self.process.stdin.flush()
            if str(event[0]) == "5":
                pass #// Create a file popup
        


    def UtilityMenu(self):
        """
        Utility menu has 2 options both of which require () input.
        """

        print('7', file=self.process.stdin) #// Acess Menu
        self.process.stdin.flush()
        
        event, value = self.window.read() #// Read events

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

    def PatchesMenu(self):
        """
        Patches menu of the tool stays open until exited, so this takes in reads using a simple while loop until its closed.
        """

        print('6', file=self.process.stdin)
        self.process.stdin.flush()
        while True:
            event, value = self.window.read()

            print(str(event[0]), file=self.process.stdin)
            self.process.stdin.flush()

            for i in range(0,50):
                line = self.process.stdout.readline()
                print(line)
            pass #// Note to self, somewhere during the execution of the loop it is entering a command infintely again. 

            if event == sg.WIN_CLOSED or event == 'Exit':
                print("0", file=self.process.stdin)
                self.process.stdin.flush()
                self.window.close()
                break
        


