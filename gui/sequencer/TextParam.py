import wx

class TextParam():

    def __init__(self, parent):
        self.__parent = parent
        self.__xpos = 0
        self.__ypos = 0
        self.__width = 100
        self.__height = 100
        #self.SetText("test")

    def SetText(self, text):
        if (isinstance(text, int)):
            text = str(text)

        self.__staticText = wx.StaticText(self.__parent,
                             id=wx.ID_ANY,
                             label=text,
                             pos=wx.Point(self.__xpos, self.__ypos),
                             size=wx.Size(self.__width, self.__height))

    def GetObject(self):
        return self.__staticText


