''' 1. '''
# Search
class QuestCurtain(ui.Window):

# Add above
class CellItemToolTipImageBox(ui.ImageBox):
	def __init__(self):
		ui.ImageBox.__init__(self)
		self.pos = 0
		self.window_type = 0
		self.DestroyToolTip()

	def __del__(self):
		ui.ImageBox.__del__(self)

	def CreateToolTip(self, parent, x, y, window_type, pos):
		import uiToolTip
		self.toolTip = uiToolTip.ItemToolTip()
		self.toolTip.SetWindowHorizontalAlignCenter()
		self.toolTip.SetFollow(False)
		self.toolTip.SetPosition(x, y)
		self.window_type = window_type
		self.pos = pos
		self.toolTip.SetInventoryItem(pos, window_type)
		self.toolTip.ResizeToolTip()
		self.toolTip.Hide()

	def DestroyToolTip(self):
		self.toolTip = None

	def OnMouseOverIn(self):
		if self.toolTip:
			self.toolTip.SetTop()
			self.toolTip.SetInventoryItem(self.pos, self.window_type)
			self.toolTip.Show()

	def OnMouseOverOut(self):
		if self.toolTip:
			self.toolTip.Hide()

''' 2. '''
# Search
	def OnSize(self, width, height):

# Add above
	def OnInsertImageShowItemToolTipByCell(self, window_type, cell):
		if not self.board:
			return

		import item, player
		vnum = player.GetItemIndex(window_type, cell)
		item.SelectItem(vnum)
		filename = item.GetIconImageFileName()

		event.AddEventSetLocalYPosition(self.descIndex, 24)

		y = event.GetEventSetLocalYPosition(self.descIndex)
		xBoard, yBoard = self.board.GetGlobalPosition()

		try:
			img = CellItemToolTipImageBox()
			img.SetParent(self.board)
			img.LoadImage(filename)
			pos_x = (self.board.GetWidth() / 2) - (img.GetWidth() / 2)
			img.SetPosition(pos_x, y)
			img.DestroyToolTip()
			img.CreateToolTip(self.board, 0, yBoard + y + img.GetHeight(), window_type, cell)
			img.Show()
			self.images.append(img)
		except RuntimeError:
			pass

		event.AddEventSetLocalYPosition(self.descIndex, img.GetHeight() - 20)

		itemname = item.GetItemName()

		if itemname:
			event.AddEventSetLocalYPosition(self.descIndex, 3)
			event.InsertTextInline(self.descIndex, itemname, (self.board.GetWidth() / 2))
		else:
			event.AddEventSetLocalYPosition(self.descIndex, 4)