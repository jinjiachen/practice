import wx


if __name__=='__main__':
        app=wx.PySimpleApp()
        app.MainLoop()
	dlg=wx.TextEntryDialog(None,'Is this ok?','TextEntry Example','default value',wx.YES_NO)
#	retCode=dlg.ShowModal()
#	if dlg.ShowModal()==wx.ID_OK:
#		print 'you entered:%s'% dlg.GetValue()
	dlg.ShowModal()
	dlg.Destroy()
