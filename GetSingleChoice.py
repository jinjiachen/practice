import wx


if __name__=='__main__':
        app=wx.PySimpleApp()
        app.MainLoop()
	choices=['alpha','beta','gemar']
	dlg=wx.GetSingleChoice('Please choose:','headline',choices) 
	print 'you choose:%s'%dlg
