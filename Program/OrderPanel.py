import wx
from enum import Enum
from db_functions import *
import datetime
import time
from Recipies import *



class InventoryStatus(Enum):
    OUT = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3




class OrderPanel(wx.Panel):

    def __init__(self, *args, **kw):
        super(OrderPanel, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        # create buttons and display them
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        spacer = wx.FlexGridSizer(2, 3, 20, 50)

        # Create a button for every recipie
        buttons = [None]
        buttons.clear()
        looper = firstRecipie
        numItems = Recipies.getNumRecipies()
        i = 0

        # Create all buttons and add them to buttons[]
        while i < numItems:
            buttons.append(OrderButton(self, label=looper.name))
            print(i)
            looper = looper.next
            i += 1

        # Add all buttons to spacer
        for button in buttons:
            print(button.food)
            spacer.Add(button, 1, wx.EXPAND)


        hbox.Add(spacer, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        self.SetSizer(hbox)

        #self.Bind(wx.EVT_BUTTON, OrderButton.OnButtonClicked, button1)


class OrderButton(wx.Button):

    def __init__(self, *args, **kw):
        super(OrderButton, self).__init__(*args, **kw)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.food = self.GetLabel()

    # Activates on button press
    def OnButtonClicked(self, e):

        # open database
        conn = opendb("food.db")

        if self.food == "Sandwitch":
            print("sandwitch")
        elif self.food == "Pasta":
            print("pasta")
        elif self.food == "Hamburger":
            print("hamburger")
        elif self.food == "Hot Dog":
            print("hot dog")
        elif self.food == "Steak":
            print("steak")
        elif self.food == "Soup":
            print("soup")
        else:
            print("ERROR: ADD BUTTON LABEL TO: OrderButton OnButtonClicked()")

    # Updates button appearance based on inventory
    def updateStatus(self):
        print("Placeholder, will complete later")

    # Updates the inventory status for the given items
    def updateInventoryStatus(self):
        print("Placeholder, will complete later")





class OrderFrame(wx.Frame):

    def __init__(self, *args, **kw):
         super(OrderFrame, self).__init__(*args, **kw)
         self.InitUI()

    def InitUI(self):
        panel = OrderPanel(self)
        self.SetTitle('Take Orders')
        self.Centre()
