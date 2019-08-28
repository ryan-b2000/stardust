import wx
from CustomBitmap import *

'''
    Panel Manager
    
    Responsible for dividing the window up into manageable pieces
'''

COLOR_RED = '#FF0000'
COLOR_GREEN = '#00FF00'
COLOR_BLUE = '#0000FF'
COLOR_B1 = '#0055FF'
COLOR_B2 = '#AA55FF'

class PanelManager():

    def __init__(self, mainWindow):
        self.__mainWindow = mainWindow

    def PanelizeMainWindow(self):

        # Split the main window into two parts
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.actionPanel = self.CreatePanel(self.__mainWindow, wx.Point(x=0, y=0), wx.Size(height=600, width=200), COLOR_RED)
        self.workPanel = self.CreatePanel(self.__mainWindow, wx.Point(x=0, y=0), wx.Size(height=600, width=wx.EXPAND), '#FFFFFF')
        sizer.Add(self.actionPanel, 0, 0, 0)
        sizer.Add(self.workPanel, 0, 0, 0)
        self.__mainWindow.SetSizer(sizer)

        # Split the right panel into the sections for the inputs and the piano roll
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.sequencerPanel = self.CreatePanel(self.workPanel, wx.Point(x=0, y=0), wx.Size(height=400, width=wx.EXPAND), COLOR_GREEN)
        self.inputPanel = self.CreatePanel(self.workPanel, wx.Point(x=0, y=0), wx.Size(height=200, width=wx.EXPAND), COLOR_BLUE)
        sizer.Add(self.inputPanel, 0, 0, 0)
        sizer.Add(self.sequencerPanel, 0, 0, 0)
        self.workPanel.SetSizer(sizer)

        #sizer = wx.BoxSizer(wx.HORIZONTAL)
        #panelLeft = self.CreatePanel(pianoPanel, wx.Point(x=0, y=0), wx.Size(height=wx.EXPAND, width=50), COLOR_B1)
        #panelRight = self.CreatePanel(pianoPanel, wx.Point(x=0, y=0), wx.Size(height=wx.EXPAND, width=wx.EXPAND), COLOR_B2)
        #sizer.Add(panelLeft, 0, 0, 0)
        #sizer.Add(panelRight, 0, 0, 0)
        #pianoPanel.SetSizer(sizer)
        #self.__sequencerFrame = panelRight

        # Split the top part into the 4 sequences to interpolate
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panelA = self.CreatePanel(self.inputPanel, wx.Point(x=0, y=0), wx.Size(height=wx.EXPAND, width=205), '#DDDDDD')
        self.panelB = self.CreatePanel(self.inputPanel, wx.Point(x=0, y=0), wx.Size(height=wx.EXPAND, width=205), '#BBDCDC')
        self.panelC = self.CreatePanel(self.inputPanel, wx.Point(x=0, y=0), wx.Size(height=wx.EXPAND, width=205), '#77DBDB')
        self.panelD = self.CreatePanel(self.inputPanel, wx.Point(x=0, y=0), wx.Size(height=wx.EXPAND, width=205), '#11DADA')
        sizer.Add(self.panelA, 0, 0, 0)
        sizer.Add(self.panelB, 0, 0, 0)
        sizer.Add(self.panelC, 0, 0, 0)
        sizer.Add(self.panelD, 0, 0, 0)
        self.inputPanel.SetSizer(sizer)

    def GetPanel(self, panel):
        if panel == "sequencer":
            return self.sequencerPanel
        if panel == "action":
            return self.actionPanel
        if panel == "inputA":
            return self.panelA
        if panel == "inputB":
            return self.panelB
        if panel == "inputC":
            return self.panelC
        if panel == "inputD":
            return self.panelD

    def CreatePanel(self, parent, position, size, background):
        panel = wx.Panel(parent, id=wx.ID_ANY, pos=position, size=size)
        panel.SetBackgroundColour(background)
        return panel

    def GetSequencerFrame(self):
        return self.__sequencerFrame


def CreatePanel(parent, position, size, background):
    panel = wx.Panel(parent, id=wx.ID_ANY, pos=position, size=size)
    panel.SetBackgroundColour(background)
    return panel