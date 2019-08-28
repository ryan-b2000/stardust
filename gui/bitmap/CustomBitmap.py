import wx
import numpy as np

HEIGHT = 150
WIDTH = 300
COLOR_FILL = '#DD0022'
BLOCK_ROW_PIXELS = 10
BLOCK_COL_PIXELS = 10

# Default colors
COLOR_DEF_R = 240
COLOR_DEF_G = 240
COLOR_DEF_B = 240

# Fill in colos
COLOR_FILL_R = 50
COLOR_FILL_G = 50
COLOR_FILL_B = 50


class CustomBitmap():

    def __init__(self, parent):
        self.__parent = parent
        self.pixels = np.ones([HEIGHT, WIDTH])
        self.pixels.fill(self.CreateRGBval(COLOR_DEF_R, COLOR_DEF_G, COLOR_DEF_B))
        self.SetBitmap()

    def SetBlock(self, row, col, color):
        for r in range (0, BLOCK_ROW_PIXELS):
            for c in range (0, BLOCK_COL_PIXELS):
                self.pixels[row + r, col + c] = color
        self.DestroyBitmap()
        self.SetBitmap()

    def SetButton(self, row, col):
        self.SetBlock(row, col, 0x555555)
        self.sbmp.Destroy()
        self.SetBitmap()
        
        self.__parent.Layout()

    def ClearButton(self, row, col):
        self.SetBlock(row, col, 0xFFFFFF)
        self.sbmp.Destroy()
        self.SetBitmap()
        self.__parent.Layout()

    def SetPixel(self, row, col, RGBval):
        self.pixels[row, col] = RGBval

    def CreateRGBval(self, red, green, blue):
        rgb = (red << 16) | (green << 8) | (blue)
        return rgb

    def SetBitmap(self):
        bmp = wx.Bitmap.FromBufferRGBA(WIDTH, HEIGHT, self.pixels)
        self.sbmp = wx.StaticBitmap(self.__parent, id=wx.ID_ANY, bitmap=bmp, pos=wx.DefaultPosition, size=wx.DefaultSize)

    def DestroyBitmap(self):
        self.sbmp.Destroy()