# XD-Colosseum-WGUI

 WIP of Python based GUI for the XD/Colosseum Windows Tool by [Stars](https://github.com/PekanMmd/)

 
 ## Dependencies 
 For the dependencies of the tool itself, you will need the latest releases of [Swift for Windows](https://swift.org/builds/swift-5.3-release/windows10/swift-5.3-RELEASE/swift-5.3-RELEASE-windows10.exe)
 
 Additionally if you're doing any encoding/decoding with the tool you may want [Cygwin](https://cygwin.com/setup-x86_64.exe)
 
 You will also need to install PySimpleGUI as it is the library almost all of this project uses to generate the GUI:
 > pip install pysimplegui


### Usage

Drag and drop all the GUI files into the root of your tool. If you're using the binary, ensure the `.exe` is also in the root of the tool.

The program will first ask you to point to your game file and then give you the main menu. Give it a couple seconds to load the tool and then you should be good to go. You can edit the colors using the `MyCreatedTheme` table in the `MenuDef` python file.


### Notes

This is still very much a WIP. Some of the buttons will not send the inputs required to return to the main menu so the GUI might not send any inputs the tool can use. If you begin clicking buttons but nothing happens, you will need to reopen the GUI. I do plan to fix this very soon.

This only works for Gale of Darkness for now, once the Gale of Darkness tool functionality is solid I will add the option for the Colosseum tool.

I do have plans to make a much nicer looking tool with custom graphics but that will be my last focus, I want to make the GUI work well first.
