#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 运行前手工修改wx.lib.analogclock.helpers.HandSet._draw的生成时间规则
import wx
import wx.lib.analogclock as ac

class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)

        def makeClock(parent):
            ctrl = ac.AnalogClock(parent, size=(300,300), hoursStyle=ac.TICKS_DECIMAL,
                    clockStyle=ac.SHOW_HOURS_TICKS | ac.SHOW_HOURS_HAND | ac.SHOW_MINUTES_HAND  )
            ctrl.SetBackgroundColour(wx.Colour(255,255,255))
            ctrl.SetFaceFillColour(wx.Colour(255,255,255))
            return ctrl

        ROW, COL = 4, 10
        sizer_clock=wx.GridSizer(ROW,COL,80,10)
        for i in range(ROW*COL):
            sizer_clock.Add( makeClock(self), 0, wx.EXPAND )
         
        sizer_main=wx.BoxSizer(wx.VERTICAL)
        sizer_main.Add( (20, 20), 0, 0 )
        sizer_main.Add( sizer_clock, 1, wx.EXPAND )
        sizer_main.Add( (20, 50), 0, 0 )
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


