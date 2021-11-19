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
                    print(str(i[1]), file=self.process.stdin)
                    self.process.stdin.flush()

            print("start", file=self.process.stdin)
            self.process.stdin.flush()

            print("", file=self.process.stdin)
            self.process.stdin.flush()



                            
                
        