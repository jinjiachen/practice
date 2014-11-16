import wx

class CheckBoxFrame(wx.Frame):
	def __init__(self):
                wx.Frame.__init__(self,None,-1,'CheckBox Example',size=(150,200))
                panel=wx.Panel(self)
                self.checkbox1=wx.CheckBox(panel,-1,'Alpha',(35,40),(150,20))
                wx.CheckBox(panel,-1,'Beta',(35,60),(150,20))
                wx.CheckBox(panel,-1,'Gamma',(35,80),(150,20))
                mybutton=wx.Button(panel,-1,'confirm',(35,100),(150,20))
                self.Bind(wx.EVT_CHECKBOX,self.msg,self.checkbox1)
#                checkbox1.SetValue(True)
        def msg(self,event):
 #             if  self.checkbox1.IsChecked()==True:
                        print("Alpha is changed")

if __name__=='__main__':
        app=wx.PySimpleApp()
        myFrame=CheckBoxFrame()
        myFrame.Show()
        app.MainLoop()
