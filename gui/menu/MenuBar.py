import wx
from ActionMenu import *

def CreateMenuBar(mainWindow):
    menuBar = wx.MenuBar()
    # Create the menu bar items
    fileMenu = ActionMenu(menuBar, "File");
    songMenu = ActionMenu(menuBar, "Song");
    learningMenu = ActionMenu(menuBar, "Learning");
    settingMenu = ActionMenu(menuBar, "Setting");
    helpMenu = ActionMenu(menuBar, "Help")

    # Create the menu bar and add the sub-menus
    menuBar.Append(fileMenu, "&File")  # Adding the File Menu to the MenuBar
    menuBar.Append(songMenu, "&Song")  # Adding the Song Menu
    menuBar.Append(settingMenu, "&Setting")
    menuBar.Append(learningMenu, "&Learning")
    menuBar.Append(helpMenu, "&Help")
    mainWindow.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
