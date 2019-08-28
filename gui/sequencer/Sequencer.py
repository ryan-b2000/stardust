import wx
from Button import *
from PanelManager import *
from TextParam import *

class Sequencer(wx.Panel):

    def __init__(self, mainWindow):
        self.__mainWindow = mainWindow
        self.buttons = []
        self.x_pos = 0
        self.y_pos = 0
        self.bitmapA = 'A'


    def SetBitmaps(self, bmpA, bmpB, bmpC, bmpD):
        self.bitmapA = bmpA
        self.bitmapB = bmpB
        self.bitmapC = bmpC
        self.bitmapD = bmpD

    # Master sequence to fill in the parent panel with the sequencer stuff
    # ------------------------------------------------------------------------------------------------------------------
    def CreateSequencer(self, parent):
        rows = wx.BoxSizer(wx.VERTICAL)         # Rows for each sequencer note number
        for row in range (0, 10):
            # Create the row panel that manages the entire row
            rowPanel = CreatePanel(parent=parent, position=wx.Point(x=0, y=0), size=wx.Size(height=25, width=wx.EXPAND),
                                   background='#CCCCCC')
            self.__CreateRowPartition(rowPanel, row)
            # Add the sub-panel to the parent panel
            rows.Add(rowPanel, 0, 0, 0)
        parent.SetSizer(rows)

    def SetEventManager(self, eventManager):
        self.__eventManager = eventManager

    # Create the row of buttons for the piano roll
    # ------------------------------------------------------------------------------------------------------------------
    def __CreateButtonRow(self, parent, rownum, size):
        for col in range(0, size):
            x = col * 25
            y = 0
            button = Button(parent, x, y)
            button.SetButtonID(rownum, col)
            button.SetEventManager(self.__eventManager)
            #button.SetBitmap()

    # Create a row partition with the MIDI number and the sequencer buttons
    # ------------------------------------------------------------------------------------------------------------------
    def __CreateRowPartition(self, rowPanel, rownum):
        # Make the sub-sizer for each row
        cols = wx.BoxSizer(wx.HORIZONTAL)

        # Make the panels that go into the sub-sizer
        numPanel = CreatePanel(parent=rowPanel, position=wx.Point(x=0, y=0),
                               size=wx.Size(height=wx.EXPAND, width=35),
                               background='#BBBBBB')
        buttonPanel = CreatePanel(parent=rowPanel, position=wx.Point(x=0, y=0),
                                  size=wx.Size(height=wx.EXPAND, width=wx.EXPAND),
                                  background='#CCCCCC')

        # Add the panels to the sub-sizer
        cols.Add(numPanel, 0, 0, 0)
        cols.Add(buttonPanel, 0, 0, 0)

        # Add sizer to parent panel
        rowPanel.SetSizer(cols)

        # Add the the text to the row ID panel
        text = TextParam(numPanel)
        text.SetText(rownum)

        # Add the buttons to the button panel
        self.__CreateButtonRow(buttonPanel, rownum, 16)

