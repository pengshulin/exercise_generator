#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 运行前手工修改wx.lib.analogclock.helpers.HandSet._draw的生成时间规则
import wx
import wx.lib.analogclock as ac
from random import randint, choice

class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)

        def makeClock(parent, has_hand=True):
            style = ac.SHOW_HOURS_TICKS
            if has_hand:
                style |= ac.SHOW_HOURS_HAND | ac.SHOW_MINUTES_HAND
            ctrl = ac.AnalogClock(parent, size=(300,300), hoursStyle=ac.TICKS_DECIMAL, clockStyle=style )
            ctrl.SetBackgroundColour(wx.Colour(255,255,255))
            ctrl.SetFaceFillColour(wx.Colour(255,255,255))
            return ctrl
        
        def makeText(parent, text='____:____'):
            ctrl = wx.TextCtrl(parent, wx.ID_ANY, text, style=wx.TE_CENTRE|wx.NO_BORDER )
            ctrl.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1, ""))
            ctrl.SetBackgroundColour(wx.Colour(255,255,255))
            return ctrl

        ROW, COL = 4, 10
        sizer_clock=wx.GridSizer(ROW,COL,10,10)
        for i in range(ROW):
            for j in range(COL):
                sizer = wx.BoxSizer(wx.VERTICAL)
                sizer.Add( makeClock(self, False), 1, wx.EXPAND )
                sizer.Add( (20, 10), 0, 0 )
                h, m = randint(1,12), choice([0,30])
                s = ' %d:%02d '%(h,m)
                sizer.Add( makeText(self, s), 0, wx.EXPAND )
                sizer_clock.Add(sizer, 1, wx.EXPAND) 
         
        sizer_main=wx.BoxSizer(wx.VERTICAL)
        sizer_main.Add( (20, 20), 0, 0 )
        sizer_main.Add( sizer_clock, 1, wx.EXPAND )
        sizer_main.Add( (20, 20), 0, 0 )
        self.SetSizer(sizer_main)
        self.SetBackgroundColour(wx.Colour(255,255,255))
        self.SetSize( (297*3, 210*3)) 
        self.Center()
        self.ShowFullScreen(True)

    
    def OnClose(self, event):
        self.Destroy()
        event.Skip()
 

if __name__ == "__main__":
    app = wx.App(0)
    dialog_1 = MyDialog(None, wx.ID_ANY, "")
    app.SetTopWindow(dialog_1)
    dialog_1.Show()
    app.MainLoop()


