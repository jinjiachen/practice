#/usr/bin/env python
#coding=utf-8
def calc():
    import wx
    import math
#def calc():
    class myframe(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self,None,-1,'方板质量计算')
            panel=wx.Panel(self)
            wx.StaticText(panel,-1,'请输入钢板的长度:',pos=(50,50))
            wx.StaticText(panel,-1,'请输入钢板的宽度:',pos=(50,100))
            wx.StaticText(panel,-1,'请输入钢板的高度:',pos=(50,150))
            self.text1=wx.TextCtrl(panel,-1,'',pos=(160,45))
            self.text2=wx.TextCtrl(panel,-1,'',pos=(160,95))
            self.text3=wx.TextCtrl(panel,-1,'',pos=(160,145))
            self.text4=wx.TextCtrl(panel,-1,'',pos=(200,250))
#        textvalue1=text1.GetStringSelection()
            self.button=wx.Button(panel,-1,'计算',pos=(100,245))
            self.Bind(wx.EVT_BUTTON,self.calcu,self.button)
        def calcu(self,event):
            length=float(self.text1.GetValue())
            width=float(self.text2.GetValue())
            height=float(self.text3.GetValue())
            density=7850
            ans=length*width*height*7850/pow(10,9)
            self.text4.SetValue(`ans`)
    if __name__=='__main__':
            myapp=wx.PySimpleApp()
            frame=myframe()
            frame.Show()
            myapp.MainLoop()
