#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
from __future__ import unicode_literals
import os
import re
import sys
import math
import time
import random
import keyword
from random import *
from ExerciseGeneratorDlg import *
    
import pypinyin
from pypinyin import pinyin, lazy_pinyin

ABOUT_INFO = '''\
Python自动出题程序 V1.2
将生成结果复制粘帖到Excel/WPS中排版

规则说明：
1. 定义必须包含generator函数，其返回值必须为字符串列表，作为单次出题结果。
2. 用ASSERT函数筛除不符合规则的出题。
3. 用STOP函数结束出题循环。
4. random库的所有函数已导入，可直接使用。
6. 支持pypinyin库，可直接使用pinyin，lazy_pinyin函数。
6. 支持unicode字符串。
7. 当返回结果项为字符串“EOL”时，换行输出。

URL: https://github.com/pengshulin/exercise_generator
Peng Shullin <trees_peng@163.com> 2017
'''

CONFIGS_LIST = [
['生成随机数', '''\
def generator():
    MIN, MAX = 0, 100
    a = randint(MIN, MAX)
    return [ a ]
'''],

['加减法（2个数）', '''\
def generator():
    MIN, MAX = 0, 100
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    oper = choice( ['-', '+'] ) 
    if oper == '+':
        c = a + b
    else:
        c = a - b
    ASSERT( 0 <= c <= MAX )
    #return [ a, oper, b, '=', '□' ]
    #return [ '%s%s%s='% (a, oper, b) ] 
    #return [ '%s%s%s='% (a, oper, b), c ] 
    #return [ '%s%s%s'% (a, oper, b), '=', c ] 
    #return [ a, oper, '□', '=', c  ]
    return [ a, oper, b, '=', c ]
'''],

['乘法（2个数）', '''\
def generator():
    MIN, MAX = 1, 10
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    c = a * b
    ASSERT( 0 <= c <= 100 )
    return [ a, '*', b, '=', c ]
'''],

['比较大小（2个数）', '''\
def generator():
    MIN, MAX = 0, 100
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    if a > b:
        oper = '>'
    elif a < b:
        oper = '<'
    else:
        oper = '='
    #return [ a, '○', b ]
    return [ a, oper, b ]
'''],

['连加连减（3个数）', '''\
def generator():
    MIN, MAX = 0, 100
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    c = randint(MIN, MAX)
    oper1 = choice( ['-', '+'] ) 
    oper2 = choice( ['-', '+'] ) 
    if oper1 == '+':
        ab = a + b
    else:
        ab = a - b
    ASSERT( 0 <= ab <= MAX )
    if oper2 == '+':
        d = ab + c
    else:
        d = ab - c 
    ASSERT( 0 <= d <= MAX )
    #return [ '%s%s%s%s%s=%s'% (a, oper1, b, oper2, c, d) ]
    #return [ '%s%s%s%s%s='% (a, oper1, b, oper2, c) ]
    return [ a, oper1, b, oper2, c, '=', d ]
'''],

['三角分解', '''\
def generator():
    MIN, MAX = 0, 20
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    c = randint(MIN, MAX)
    ab = a + b
    bc = b + c
    ac = a + c
    ASSERT( 0 <= bc <= MAX )
    ASSERT( 0 <= ac <= MAX )
    return [ 'EOL','EOL',ab,'',a,'',ac,'EOL','EOL','',b,'',c,'EOL','EOL','','',bc]
'''],


['数墙（3层）', '''\
def generator():
    MIN, MAX = 0, 20
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    c = randint(MIN, MAX)
    ab = a + b
    bc = b + c
    abc = ab + bc
    ASSERT( 0 <= ab <= MAX )
    ASSERT( 0 <= bc <= MAX )
    ASSERT( 0 <= abc <= MAX )
    return [ 'EOL','','',abc,'EOL','',ab,'',bc,'EOL',a,'',b,'',c]
'''],

['数墙（4层）', '''\
def generator():
    MIN, MAX = 0, 20
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    c = randint(MIN, MAX)
    d = randint(MIN, MAX)
    ab = a + b
    bc = b + c
    cd = c + d
    abc = ab + bc
    bcd = bc + cd
    abcd = abc + bcd
    ASSERT( 0 <= ab <= MAX )
    ASSERT( 0 <= bc <= MAX )
    ASSERT( 0 <= cd <= MAX )
    ASSERT( 0 <= abc <= MAX )
    ASSERT( 0 <= bcd <= MAX )
    ASSERT( 0 <= abcd <= MAX )
    return [ 'EOL','','','',abcd,'EOL','','',abc,'',bcd,'EOL','',ab,'',bc,'',cd,'EOL',a,'',b,'',c,'',d]
'''],

['排序（4个数）', '''\
def generator():
    MIN, MAX = 0, 100
    lst = [randint(MIN, MAX) for i in range(4)]
    lst.sort()
    a, b, c, d = lst
    ASSERT( a < b < c < d )
    #r=[a,b,c,d]; shuffle(r); return r
    return [ a, '<', b, '<', c, '<', d ]
'''],

['排序（5个数）', '''\
def generator():
    MIN, MAX = 0, 100
    lst = [randint(MIN, MAX) for i in range(5)]
    lst.sort()
    a, b, c, d, e = lst
    ASSERT( a < b < c < d < e )
    r=[a,b,c,d,e]; shuffle(r); s=', '.join(map(str,r))
    return [ s, '>'.join(['____']*5) ]
'''],

['算术题排序（5个算术题）', '''\
def generator():
    MIN, MAX = 0, 20
    def generate_single():
        a, b = randint(MIN, MAX), randint(MIN, MAX)
        return (a,b,a+b)

    a1, a2, a = generate_single()  
    ASSERT( MIN <= a <= MAX )
    b1, b2, b = generate_single()  
    ASSERT( MIN <= b <= MAX )
    ASSERT( b != a )
    c1, c2, c = generate_single()  
    ASSERT( MIN <= c <= MAX )
    ASSERT( c not in [a,b] )
    d1, d2, d = generate_single()  
    ASSERT( MIN <= d <= MAX )
    ASSERT( d not in [a,b,c] )
    e1, e2, e = generate_single()  
    ASSERT( MIN <= e <= MAX )
    ASSERT( e not in [a,b,c,d] )

    r=[[a1,a2],[b1,b2],[c1,c2],[d1,d2],[e1,e2]]
    shuffle(r)
    s=', '.join(['%s+%s'% (x,y) for x,y in r])
    return [ s, '>'.join(['________']*5) ]
'''],

['凑整数', '''\
def generator():
    MIN, MAX = 0, 100
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)
    ASSERT( 1 <= b <= 9 )
    #oper = choice( ['-', '+'] ) 
    oper = '+'
    if oper == '+':
        c = a + b
    else:
        c = a - b
    ASSERT( 10 <= c <= MAX )
    ASSERT( c % 10 == 0 )
    return [ a, oper, b, '=', c ]
'''],

['带拼音汉字', '''\
source=[
'天', '地', '玄', '黄', '宇', '宙', '洪', '荒',
'日月盈昃','成宿列张',
]

compact_mode = False
# 紧缩模式
if compact_mode:
    source=list(''.join(source))

copies=1
# 创建副本
if copies > 1:
    source=[i*copies for i in source]

two_column=True
# 预处理: 截断或填充
if two_column:
    columns, rows = 10, 8
    source = source[:2*rows]
    while len(source) < 2*rows:
        source.append('')
else:
    columns, rows = 13, 11
    source = source[:rows]
    while len(source) < rows:
        source.append('')

def generator():
    global source, copies, two_column, columns, rows
    if not source:
        STOP()
    if two_column:
        lb = source.pop(len(source)/2)
        la = source.pop(0)
        la = la[:columns]
        lb = lb[:columns]
        laspace=[' ' for i in range(columns-len(la))]
        lbspace=[' ' for i in range(columns-len(lb))]
        pa = [i[0] for i in pinyin(la)]
        pb = [i[0] for i in pinyin(lb)]
        ret = pa + laspace + pb + lbspace + ['EOL'] 
        ret += list(la) + laspace + list(lb) + lbspace
    else:
        l = source.pop(0)
        l = l[:columns]
        lspace=[' ' for i in range(columns-len(l))]
        p = [i[0] for i in pinyin(l)]
        ret = p + lspace + ['EOL'] + list(l) + lspace
    return ret
'''],



]

CONFIGS_DICT = {}
for k,v in CONFIGS_LIST:
    CONFIGS_DICT[k] = v

###############################################################################

class AssertError(Exception):
    pass

class StopError(Exception):
    pass


def ASSERT(condition):
    if not condition:
        raise AssertError()

def STOP():
    raise StopError()



class MainDialog(MyDialog):

    def __init__(self, *args, **kwds):
        MyDialog.__init__( self, *args, **kwds )
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)
        self.init_text_ctrl_rules()
        self.button_generate.Enable(False)
        self.button_copy_result.Enable(False)
        self.combo_box_type.SetValue('请选择出题类型...')
        self.combo_box_type.AppendItems([c[0] for c in CONFIGS_LIST]) 
        self.text_ctrl_number.SetValue('100')
        self.clrAllResult()

    def OnClose(self, event):
        self.Destroy()
        event.Skip()
        
    def OnSelectType(self, event):
        self.info('')
        tp = self.combo_box_type.GetValue()
        if CONFIGS_DICT.has_key(tp):
            self.text_ctrl_rules.SetValue( CONFIGS_DICT[tp] )
            self.button_generate.Enable(True)
        else:
            self.button_generate.Enable(False)
        event.Skip()

    def clrAllResult( self ):
        self.grid_result.ClearGrid()
        lines = self.grid_result.GetNumberRows()
        if lines:
            self.grid_result.DeleteRows(numRows=lines)

    def addResult( self, result ):
        if self.grid_result.AppendRows():
            line = self.grid_result.GetNumberRows()
            index = 0
            for item in result:
                if isinstance(item, unicode) and item == 'EOL':
                    if self.grid_result.AppendRows():
                        line += 1
                        index = 0
                    else:
                        return 
                else:
                    self.grid_result.SetCellValue( line-1, index, unicode(item) )
                    index += 1
        else:
            return
     
    def info( self, info, info_type=wx.ICON_WARNING ):
        if info:
            self.window_info.ShowMessage(info, info_type)
        else:
            self.window_info.Dismiss()
 
    def OnGenerate(self, event):
        self.info('')
        rules = self.text_ctrl_rules.GetValue()
        try:
            num = int(self.text_ctrl_number.GetValue())
            if num <= 0 or num > 10000:
                raise Exception
        except:
            self.info('出题数量错误', wx.ICON_ERROR)
            return
        counter = 0
        try:
            code = compile(rules, '', 'exec')
            exec( code )
            generator
        except Exception as e:
            self.info(str(e), wx.ICON_ERROR)
            return
        self.clrAllResult()
        t0 = time.time()
        while counter < num:
            try:
                result = generator()
                counter += 1 
                self.addResult( result )
            except AssertError:
                pass
            except StopError:
                break
            except Exception as e:
                self.info(str(e))
                return
        t1 = time.time()
        print( 'time elapsed: %.1f seconds'% (t1-t0) )
        self.button_copy_result.Enable(True)
        event.Skip()

    def OnCopyResult(self, event):
        self.info('')
        lines = self.grid_result.GetNumberRows()
        if lines:
            ret = []
            for l in range(lines):
                items = [self.grid_result.GetCellValue( l, c ) \
                         for c in range(26)]
                cp = '\t'.join(items).rstrip('\t')
                print cp
                ret.append( cp )
            copy = '\r\n'.join(ret)
            import pyperclip
            pyperclip.copy( copy )
        event.Skip()

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, ABOUT_INFO, '关于', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
 
    def init_text_ctrl_rules(self):
        ctrl = self.text_ctrl_rules
        faces = { 'times': 'Courier New',
                  'mono' : 'Courier New',
                  'helv' : 'Courier New',
                  'other': 'Courier New',
                  'size' : 12,
                  'size2': 10,
                }
        ctrl.SetLexer(wx.stc.STC_LEX_PYTHON)
        ctrl.SetKeyWords(0, " ".join(keyword.kwlist))
        ctrl.SetProperty("tab.timmy.whinge.level", "1")
        ctrl.SetMargins(0,0)
        ctrl.SetViewWhiteSpace(False)
        ctrl.Bind(wx.stc.EVT_STC_UPDATEUI, self.OnUpdateUI)
        ctrl.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,     "face:%(helv)s,size:%(size)d" % faces)
        ctrl.StyleClearAll()
        ctrl.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,     "face:%(helv)s,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_STYLE_LINENUMBER,  "back:#C0C0C0,face:%(helv)s,size:%(size2)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_STYLE_CONTROLCHAR, "face:%(other)s" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_STYLE_BRACELIGHT,  "fore:#FFFFFF,back:#0000FF,bold")
        ctrl.StyleSetSpec(wx.stc.STC_STYLE_BRACEBAD,    "fore:#000000,back:#FF0000,bold")
        ctrl.StyleSetSpec(wx.stc.STC_P_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_COMMENTLINE, "fore:#007F00,face:%(other)s,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_NUMBER, "fore:#007F7F,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_STRING, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_CHARACTER, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_WORD, "fore:#00007F,bold,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_TRIPLE, "fore:#7F0000,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_TRIPLEDOUBLE, "fore:#7F0000,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_CLASSNAME, "fore:#0000FF,bold,underline,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_DEFNAME, "fore:#007F7F,bold,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_OPERATOR, "bold,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_IDENTIFIER, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_COMMENTBLOCK, "fore:#7F7F7F,size:%(size)d" % faces)
        ctrl.StyleSetSpec(wx.stc.STC_P_STRINGEOL, "fore:#000000,face:%(mono)s,back:#E0C0E0,eol,size:%(size)d" % faces)
        ctrl.SetCaretForeground("BLACK")
        ctrl.SetMarginType(1, wx.stc.STC_MARGIN_NUMBER)
        ctrl.SetMarginWidth(1, 40)
    

    def OnUpdateUI(self, evt):
        ctrl = self.text_ctrl_rules
        # check for matching braces
        braceAtCaret = -1
        braceOpposite = -1
        charBefore = None
        caretPos = ctrl.GetCurrentPos()

        if caretPos > 0:
            charBefore = ctrl.GetCharAt(caretPos - 1)
            styleBefore = ctrl.GetStyleAt(caretPos - 1)

        # check before
        if charBefore and (32 < charBefore < 128):
            if chr(charBefore) in "[]{}()" and styleBefore == wx.stc.STC_P_OPERATOR:
                braceAtCaret = caretPos - 1

        # check after
        if braceAtCaret < 0:
            charAfter = ctrl.GetCharAt(caretPos)
            styleAfter = ctrl.GetStyleAt(caretPos)
            if charAfter and (32 < charAfter < 128):
                if chr(charAfter) in "[]{}()" and styleAfter == wx.stc.STC_P_OPERATOR:
                    braceAtCaret = caretPos

        if braceAtCaret >= 0:
            braceOpposite = ctrl.BraceMatch(braceAtCaret)
        if braceAtCaret != -1  and braceOpposite == -1:
            ctrl.BraceBadLight(braceAtCaret)
        else:
            ctrl.BraceHighlight(braceAtCaret, braceOpposite)



if __name__ == "__main__":
    gettext.install("app")
    app = wx.App(0)
    app.SetAppName( 'ExerciseGeneratorApp' )
    dialog_1 = MainDialog(None, wx.ID_ANY, "")
    app.SetTopWindow(dialog_1)
    dialog_1.Show()
    app.MainLoop()
