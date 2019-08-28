import wx
import os
from ActionMenu import *
from ButtonGrid import *
from TextParam import *
from MenuBar import *
from PanelManager import *
from Sequencer import *
from CustomBitmap import *
from MainWindow import *
from EventManager import *

def CreateWindowPanels(window):
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 1024


# ----------------------------------------------------------------------------------------------------------------------
#       MAIN
# ----------------------------------------------------------------------------------------------------------------------
app = wx.App(False)

# Initialize the Main Window
mainWindow = MainWindow(None, "Sample editor")

# Initialize Event Manager
eventManager = EventManager(mainWindow)

# Create the Window Menu Bar
CreateMenuBar(mainWindow)

# Partition the window into panels
panelManager = PanelManager(mainWindow)
panelManager.PanelizeMainWindow()

# Create Sequencer
sequencer = Sequencer(mainWindow)
sequencer.SetEventManager(eventManager)
sequencer.CreateSequencer(panelManager.GetPanel("sequencer"))

# Create Pianoroll Bitmaps
bitmapA = CustomBitmap(panelManager.GetPanel("inputA"))
bitmapB = CustomBitmap(panelManager.GetPanel("inputB"))
bitmapC = CustomBitmap(panelManager.GetPanel("inputC"))
bitmapD = CustomBitmap(panelManager.GetPanel("inputD"))

eventManager.SetActiveBitmap(bitmapA)


mainWindow.Show()
app.MainLoop()

