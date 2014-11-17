import wx

class ListBoxFrame(wx.Frame):
	def __init__(self):
                wx.Frame.__init__(self,None,-1,'ListBox Example',size=(250,200))
                panel=wx.Panel(self)
		sampleList=['one','two','three','four','five']
		listbox=wx.ComboBox(panel,-1,'label',(20,20),(80,120),sampleList,wx.CB_READONLY)
#		listbox.SetSelection(3)
		listbox.Append('six')
                
if __name__=='__main__':
        app=wx.PySimpleApp()
        myFrame=ListBoxFrame()
        myFrame.Show()
        app.MainLoop()
