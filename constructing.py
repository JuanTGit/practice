

class GamePanel:
	originalTileSize = 16
	scale = 3
	tileSize = originalTileSize * scale
	maxScreenCol = 16
	maxScreenRow = 12
	screenWidth = tileSize * maxScreenCol
	screenHeight = tileSize * maxScreenRow

	def __init__(self, color):
		self.setPreferredSize = [self.screenWidth, self.screenHeight]
		self.setBackground = color
