import wx
import os

if __name__=='__main__':
	app=wx.PySimpleApp()
	dialog=wx.DirDialog(None,'Choose a dirctory',style=wx.DD_DEFAULT_STYLE|wx.DD_NEW_DIR_BUTTON)
	if dialog.ShowModal()==wx.ID_OK:
		print dialog.GetPath()
	dialog.Destroy()