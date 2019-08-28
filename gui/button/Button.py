import wx

'''
This classes manages the button creation process.
'''

STATE_OFF = 0
STATE_ON = 1
WIDTH = 25
HEIGHT = 25

class Button():

    # Constructor
    # ------------------------------------------------------------------------------------------------------------------
    # mainWindow = the main window of the application
    # boxSizer = the parent box sizer for the button grid
    def __init__(self, mainWindow, x, y):
        self.__parent = mainWindow
        self.__buttonState = STATE_OFF
        self.x_pos = x
        self.y_pos = y
        self.bitmap = 0
        self.CreateImageButton(x, y, 25, 25)

    # Set the button size
    # ------------------------------------------------------------------------------------------------------------------
    def SetButtonSize(self, w, h):
        self.width = w
        self.height = h


    # Create a button
    # ------------------------------------------------------------------------------------------------------------------
    def CreateButton(self, x, y, w, h):
        button = wx.Button(self.__parent,
                           id=wx.ID_ANY,
                           label=' ',
                           pos=wx.Point(x, y),
                           size=wx.Size(width=w, height=h),
                           name=' ')



    # Create a Bitmap Button
    # ------------------------------------------------------------------------------------------------------------------
    def CreateBitmapButton(self, x, y):
        bmp = wx.Bitmap("images/button_off.bmp", wx.BITMAP_TYPE_ANY)
        button = wx.BitmapButton(self.__parent,
                                 id=wx.ID_ANY, bitmap=bmp,
                                 pos=wx.Point(self.x_pos, self.y_pos),
                                 size=wx.DefaultSize,
                                 style=0,
                                 validator=wx.DefaultValidator,
                                 name=' ')



    # Create an Image Button
    # ------------------------------------------------------------------------------------------------------------------
    def CreateImageButton(self, x, y, w, h):
        bmp = wx.Bitmap("images/button_off.bmp", wx.BITMAP_TYPE_ANY)
        self.__imageButton = wx.StaticBitmap(self.__parent, id=wx.ID_ANY, bitmap=bmp,
                                             pos=wx.Point(self.x_pos, self.y_pos), size=wx.Size(height=h, width=w))
        self.__imageButton.Bind(wx.EVT_LEFT_DOWN, self.onClick, id=wx.ID_ANY)

    def SetBitmap(self, bitmap):
        self.bitmap = bitmap
        print("bitmap set")

    def SetEventManager(self, eventManager):
        self.__eventManager = eventManager

    # Set the On Click Event for the button
    # ------------------------------------------------------------------------------------------------------------------
    def onClick(self, e):
        if (self.__buttonState == STATE_ON):
            print("Press", self.__id, "OFF")
            bmp = wx.Bitmap("images/button_off.bmp", wx.BITMAP_TYPE_ANY)
            self.__buttonState = STATE_OFF
            self.__eventManager.SequencerButton(self.__id, "BUTTON ON")
        else:
            print("Press", self.__id, "ON!")
            bmp = wx.Bitmap("images/button_on.bmp", wx.BITMAP_TYPE_ANY)
            self.__buttonState = STATE_ON
            self.__eventManager.SequencerButton(self.__id, "BUTTON OFF")
        self.__imageButton.SetBitmap(bmp)


    def GetButton(self):
        return self.__imageButton

    def SetButtonID(self, row, col):
        self.__id = (row * 16) + col
