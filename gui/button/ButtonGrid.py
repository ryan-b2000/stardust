import wx
from Button import *

'''
Class ButtonGrid creates a grid of buttons within a boxsizer

Must pass in the parent Box Sizer and Main Window
'''
BUTTON_STATE_OFF = 0
BUTTON_STATE_ON = 1

class ButtonGrid():

    # mainWindow = the main window of the application
    # boxSizer = the parent box sizer for the button grid
    def __init__(self, parent):
        self.__parent = parent
        self.__buttonState = BUTTON_STATE_OFF
        self.buttons = []


    # Set the starting position of the button grid
    def SetStartingPos(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def SetPosition(self, x, y):
        print("Set position")

    # Create a row of buttons to be used for the button grid
    #
    # num = the number of buttons to create
    def CreateGrid(self, num):
        for i in range(0, num):
            button = Button(self.parent, self.x_pos, self.y_pos)
            self.buttons.append(button)
            self.x_pos = self.x_pos + 25
