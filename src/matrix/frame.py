from acrylic import Color
if(PLATFORM == "rpi"):
	from rgbmatrix import RGBMatrix, RGBMatrixOptions

class Frame:
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.frame_canvas
		self.twin_canvas = []

		pass

	def set_pixel(self, r, g, b):

		pass

	def get_frame(self):
		pass

	def set_frame(self):
		pass