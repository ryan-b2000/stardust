
class EventManager():

    def __init__(self, mainWindow):
        self.__mainWindow = mainWindow

    def SetActiveBitmap(self, bitmap):
        self.__bitmap = bitmap

    def SequencerButton(self, id, state):
        print("ID:", id)
        row = int(round((id / 16), 0))
        col = int(round(id - (16 * (row - 1)), 0))
        print("row", row)
        print("col", col)
        if (state == "BUTTON_ON"):
            self.__bitmap.SetButton(row, col)
        else:
            self.__bitmap.ClearButton(row, col)
