#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade f172c83ff51d+ on Wed Mar  8 08:45:49 2017
#

import wx
import wx.grid

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
import wx.stc
from wx.stc import StyledTextCtrl
# end wxGlade


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.combo_box_type = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.CB_SORT)
        self.text_ctrl_number = wx.TextCtrl(self, wx.ID_ANY, _("100"))
        self.text_ctrl_rules = StyledTextCtrl(self, wx.ID_ANY)
        self.label_info = wx.StaticText(self, wx.ID_ANY, "")
        self.button_generate = wx.Button(self, wx.ID_ANY, _(u"\u51fa\u9898"))
        self.button_copy_result = wx.Button(self, wx.ID_ANY, _(u"\u590d\u5236\u7ed3\u679c"))
        self.button_about = wx.Button(self, wx.ID_ANY, _(u"\u5173\u4e8e"))
        self.grid_result = wx.grid.Grid(self, wx.ID_ANY, size=(1, 1))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.OnSelectType, self.combo_box_type)
        self.Bind(wx.EVT_BUTTON, self.OnGenerate, self.button_generate)
        self.Bind(wx.EVT_BUTTON, self.OnCopyResult, self.button_copy_result)
        self.Bind(wx.EVT_BUTTON, self.OnAbout, self.button_about)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle(_(u"\u81ea\u52a8\u51fa\u9898\u673a"))
        self.SetSize((931, 818))
        self.button_generate.SetMinSize((100, -1))
        self.grid_result.CreateGrid(100, 26)
        self.grid_result.EnableEditing(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add((20, 20), 0, 0, 0)
        sizer_2.Add((20, 20), 0, 0, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, _(u"\u9009\u62e9\u9898\u578b\uff1a"))
        sizer_6.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6.Add(self.combo_box_type, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, _(u"\u6570\u91cf\uff1a"))
        sizer_6.Add(label_5, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6.Add(self.text_ctrl_number, 0, 0, 0)
        sizer_5.Add(sizer_6, 0, wx.EXPAND, 0)
        sizer_5.Add((20, 20), 0, 0, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, _(u"\u89c4\u5219\u5b9a\u4e49\uff1a"))
        sizer_9.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(self.text_ctrl_rules, 1, wx.EXPAND, 0)
        sizer_5.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_5.Add((20, 20), 0, 0, 0)
        sizer_5.Add(self.label_info, 0, wx.EXPAND, 0)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_3.Add((20, 20), 0, 0, 0)
        sizer_4.Add(self.button_generate, 2, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 0, 0, 0)
        sizer_4.Add(self.button_copy_result, 1, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 0, 0, 0)
        sizer_4.Add(self.button_about, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_2.Add((20, 20), 0, 0, 0)
        sizer_2.Add(self.grid_result, 1, wx.EXPAND, 0)
        sizer_2.Add((20, 20), 0, 0, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add((20, 20), 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnSelectType(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'OnSelectType' not implemented!")
        event.Skip()

    def OnGenerate(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'OnGenerate' not implemented!")
        event.Skip()

    def OnCopyResult(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'OnCopyResult' not implemented!")
        event.Skip()

    def OnAbout(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'OnAbout' not implemented!")
        event.Skip()

# end of class MyDialog
