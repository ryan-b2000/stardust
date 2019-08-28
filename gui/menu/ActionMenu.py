import wx

class ActionMenu(wx.Menu):

    def __init__(self, menubar, type):
        wx.Frame.__init__(self)
        print("test")
        if type == "File":
            self.__initFile()
        if type == "Learning":
            self.__initLearning()
        if type == "Song":
            self.__initSong()
        if type == "Setting":
            self.__initSettings()
        if type == "Help":
            self.__initHelp()

    #   Learning Menu
    # ------------------------------------------------------------------------------------------------------------------
    def __initLearning(self):
        self.__addMenuItem("Select Model", self.onModelSelect)

    def onModelSelect(self):
        pass

    #   Help Menu
    # ------------------------------------------------------------------------------------------------------------------
    def __initHelp(self):
        self.__addMenuItem("About", self.onViewAbout)

    def onViewAbout(self):
        pass



    #   Settings Menu
    # ------------------------------------------------------------------------------------------------------------------
    def __initSettings(self):
        self.__addMenuItem("Wifi", self.onWifiSettings)

    def onWifiSettings(self):
        pass

    #   Song Menu
    # ------------------------------------------------------------------------------------------------------------------
    def __initSong(self):
        self.__addMenuItem("Save Song", self.onSongSave)
        self.__addMenuItem("Load Song", self.onSongLoad)

    def onSongSave(self):
        pass

    def onSongLoad(self):
        pass

    #   File Menu
    # ------------------------------------------------------------------------------------------------------------------
    def __initFile(self):
        self.__addMenuItem("Restart", self.onRestart)
        self.__addMenuItem("Quit", self.onQuit)

    def onQuit(self, e):
        print("Close")

    def onRestart(self, e):
        print("Restart")

    #   Helper Functions
    # ------------------------------------------------------------------------------------------------------------------
    def __addMenuItem(self, title, event):
        item = self.Append(wx.ID_ANY, title)
        self.Bind(wx.EVT_MENU, event, item)
