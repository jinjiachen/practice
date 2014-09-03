#/usr/bin/env python
#coding=utf-8
import wx
import squares
class myframe(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'�������')
        panel=wx.Panel(self)
        mymenubar=wx.MenuBar()
        mymenu1=wx.Menu()
        mymenu2=wx.Menu()
        myexit=mymenu1.Append(wx.NewId(),'&�˳�')
        item1=mymenu2.Append(-1,'��������')
        item2=mymenu2.Append(-1,'Բ������')
        item3=mymenu2.Append(-1,'�ֹ�')
        mymenu2.Append(-1,'������ƫ��')
        mymenu2.Append(-1,'��ȫ����С�ھ�')
        mymenubar.Append(mymenu1,'�ļ�')
        mymenubar.Append(mymenu2,'����')
        self.SetMenuBar(mymenubar)
        self.Bind(wx.EVT_MENU,self.exit,myexit)
        self.Bind(wx.EVT_MENU,self.squ,item1)
        self.Bind(wx.EVT_MENU,self.cir,item2)
        self.Bind(wx.EVT_MENU,self.cyl,item3)
    def squ(self,event):
        frame1=myframe1()
        frame1.Show()
    def cir(self,event):
        frame2=myframe2()
        frame2.Show()
    def cyl(self,event):
        frame3=myframe3()
        frame3.Show()
    def exit(self,event):
        self.Close(True)
class myframe1(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self,None,-1,'������������')
            panel=wx.Panel(self)
            wx.StaticText(panel,-1,'����(mm):',pos=(50,50))
            wx.StaticText(panel,-1,'���(mm):',pos=(50,100))
            wx.StaticText(panel,-1,'�߶�(mm):',pos=(50,150))
            self.text1=wx.TextCtrl(panel,-1,'',pos=(160,45))
            self.text2=wx.TextCtrl(panel,-1,'',pos=(160,95))
            self.text3=wx.TextCtrl(panel,-1,'',pos=(160,145))
            self.text4=wx.TextCtrl(panel,-1,'',pos=(200,250))
#        textvalue1=text1.GetStringSelection()
            self.button=wx.Button(panel,-1,'����',pos=(100,245))
            self.Bind(wx.EVT_BUTTON,self.calcu,self.button)
        def calcu(self,event):
            length=float(self.text1.GetValue())
            width=float(self.text2.GetValue())
            height=float(self.text3.GetValue())
            density=7850
            ans=length*width*height*7850/pow(10,9)
            self.text4.SetValue(`ans`)
class myframe2(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self,None,-1,'Բ����������')
            panel=wx.Panel(self)
            wx.StaticText(panel,-1,'ֱ��(mm):',pos=(50,50))
            wx.StaticText(panel,-1,'���(mm):',pos=(50,100))
            wx.StaticText(panel,-1,'����(mm):',pos=(50,150))
            self.text1=wx.TextCtrl(panel,-1,'',pos=(160,45))
            self.text2=wx.TextCtrl(panel,-1,'',pos=(160,95))
            self.text3=wx.TextCtrl(panel,-1,'',pos=(160,145))
            self.text4=wx.TextCtrl(panel,-1,'',pos=(200,250))
#        textvalue1=text1.GetStringSelection()
            self.button=wx.Button(panel,-1,'����',pos=(100,245))
            self.Bind(wx.EVT_BUTTON,self.calcu,self.button)
        def calcu(self,event):
            pi=3.14159265357
            D=float(self.text1.GetValue())
            t=float(self.text2.GetValue())
            quantity=float(self.text3.GetValue())
            density=7850
            ans=pi*D*D/4*t*quantity*7850/pow(10,9)
            self.text4.SetValue(`ans`)
class myframe3(wx.Frame):
        def __init__(self):
            wx.Frame.__init__(self,None,-1,'������������')
            panel=wx.Panel(self)
            wx.StaticText(panel,-1,'ֱ��(mm):',pos=(50,50))
            wx.StaticText(panel,-1,'�ں�(mm):',pos=(50,100))
            wx.StaticText(panel,-1,'����(mm):',pos=(50,150))
            self.text1=wx.TextCtrl(panel,-1,'',pos=(160,45))
            self.text2=wx.TextCtrl(panel,-1,'',pos=(160,95))
            self.text3=wx.TextCtrl(panel,-1,'',pos=(160,145))
            self.text4=wx.TextCtrl(panel,-1,'',pos=(200,250))
#        textvalue1=text1.GetStringSelection()
            self.button=wx.Button(panel,-1,'����',pos=(100,245))
            self.Bind(wx.EVT_BUTTON,self.calcu,self.button)
        def calcu(self,event):
            pi=3.14159265357
            D=float(self.text1.GetValue())
            t=float(self.text2.GetValue())
            d=D-2*t
            length=float(self.text3.GetValue())
            density=7850
            ans=pi/4*(D*D-d*d)*length*7850/pow(10,9)
            self.text4.SetValue(`ans`)
if __name__=='__main__':
    myapp=wx.PySimpleApp()
    frame=myframe()
    frame.Show()
    myapp.MainLoop()
