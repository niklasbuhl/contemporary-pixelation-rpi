from decouple import config
import multiprocessing as mp

from ..animation_scripts.test import TestAnimation

PLATFORM = config("PLATFORM")

if(PLATFORM == "rpi"):
	from rgbmatrix import RGBMatrix, RGBMatrixOptions

RGB_ROWS = config("RGB_ROWS")
RGB_CHAIN_LENGTH = config("RGB_CHAIN_LENGTH")
RGB_PARALLEL = config("RGB_PARALLEL")
RGB_DISABLE_HARDWARE_PULSING = config("RGB_DISABLE_HARDWARE_PULSING")
RGB_HARDWARE_MAPPING = config("RGB_HARDWARE_MAPPING")
RGB_GPIO_SLOWDOWN = config("RGB_GPIO_SLOWDOWN")

class RGB():

	def __init__(self):

		print("Init RGB Controller")
		print(f"RGB_ROWS {RGB_ROWS}")
		print(f"RGB_CHAIN_LENGTH {RGB_CHAIN_LENGTH}")
		print(f"RGB_PARALLEL {RGB_PARALLEL}")
		print(f"RGB_DISABLE_HARDWARE_PULSING {RGB_DISABLE_HARDWARE_PULSING}")
		print(f"RGB_HARDWARE_MAPPING {RGB_HARDWARE_MAPPING}")
		print(f"RGB_GPIO_SLOWDOWN {RGB_GPIO_SLOWDOWN}")

		if(PLATFORM == "rpi"):
			options = RGBMatrixOptions()
			options.rows = int(RGB_ROWS)
			options.chain_length = int(RGB_CHAIN_LENGTH)
			options.parallel = int(RGB_PARALLEL)
			options.disable_hardware_pulsing = RGB_DISABLE_HARDWARE_PULSING
			options.hardware_mapping = RGB_HARDWARE_MAPPING
			options.gpio_slowdown = float(RGB_GPIO_SLOWDOWN)

			self.matrix = RGBMatrix(options = options)
			self.frame_canvas = self.matrix.CreateFrameCanvas()

			# Set "on" pixel
			self.frame_canvas.SetPixel(0,0,0,255,0)
			self.sync()
			# self.frame_canvas = self.matrix.SwapOnVSync(self.frame_canvas)

		else:
			self.matrix = "matrix"

		# Connection
		self.conn_top, self.conn_bottom = mp.Pipe()
		
		# Test Animation
		self.ta = TestAnimation(self.conn_bottom, self.matrix)

	def set_pixel(self, x, y, c):
		print("set pixel")

	def set_frame(self):
		print("set frame")

	def get_frame(self):
		print(self.frame_canvas)
	
	def clear_frame(self):
		print("clear frame")

		if(PLATFORM == "rpi"):
			self.frame_canvas.Clear()
			self.sync()

	def sync():
		self.frame_canvas = self.matrix.SwapOnVSync(self.frame_canvas)
	
	def start_animation(self):
		try:
			if not self.ta.is_alive():
				self.ta.start()
				return "Animation started."
			else:
				return "Animation is already started."
		except:
			return "Something went wrong."

	def stop_animation(self):
		try:
			if self.ta.is_alive():
				self.conn_top.send("stop")
				return "Animation stopped."
			else:
				return "Animation is not started."
		except:
			return "Something went wrong."

	def animation_status(self):
		return self.ta.is_alive()

	def command_animation(self, command):
		self.conn_top.send(command)

rgb = RGB()