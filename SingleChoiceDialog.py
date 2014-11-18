import wx


if __name__=='__main__':
        app=wx.PySimpleApp()
        app.MainLoop()
	choices=['alpha','beta','gemar']
	dlg=wx.SingleChoiceDialog(None,'Please choose','headline',choices) 
	feedback=dlg.ShowModal()
	if feedback==wx.ID_OK:
		print 'you selected:%s\n'% dlg.GetStringSelection()
	dlg.Destroy()
#	retCode=dlg.ShowModal()
#	if dlg.ShowModal()==wx.ID_OK:
#		print 'you entered:%s'% dlg.GetValue()
#	dlg.ShowModal()
#	dlg.Destroy()
#	print `dlg`
