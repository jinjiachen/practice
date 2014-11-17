import wx


class SplitterExampleFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title)
		self.MakeMenuBar()
		self.minpane=0
		self.initpos=0
		self.sp=wx.SplitterWindow(self)
		self.pl=wx.Panel(self.sp,style=wx.SUNKEN_BORDER)
		self.p2=wx.Panel(self.sp,style=wx.SUNKEN_BORDER)
		self.p1.SetBackgroundColour('pink')
		self.p2.SetBackgroundColour('sky blue')
		self.p1.Hide()
		self.p2.Hide()
		self.sp.Initialize(self.sp1)
		self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGING,self.OnSashChanging,self.sp)
		self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGING,self.OnSashChanged,self.sp)


		


if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=MiniFrame()
	frame.Show()
	app.MainLoop()

					
