from rgbmatrix import RGBMatrix, RGBMatrixOptions
import random
import time

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.disable_hardware_pulsing = True
options.hardware_mapping = "adafruit-hat"
options.gpio_slowdown = 1

matrix = RGBMatrix(options = options)
frame_canvas = matrix.CreateFrameCanvas()
from PIL import Image

# Create a new empty image with a white background
width = 32
height = 32
color = (255, 255, 255)  # RGB color value for white
image = Image.new("RGB", (width, height))

while True:
	start = time.time()
	for y in range(height):
		for x in range(width):
			# color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # RGB color value for white
			color = (255,0,255)
			image.putpixel((x, y), color)

	matrix.SetImage(image)
	end = time.time()
	print(f"run: ${end - start}")
	time.sleep(0.05)