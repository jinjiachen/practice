import wx


if __name__=='__main__':
        app=wx.PySimpleApp()
        app.MainLoop()
	dlg=wx.GetNumberFromUser('Input Numbers:','Get Number','123',None) #bad
#	retCode=dlg.ShowModal()
#	if dlg.ShowModal()==wx.ID_OK:
#		print 'you entered:%s'% dlg.GetValue()
#	dlg.ShowModal()
#	dlg.Destroy()
	print `dlg`
