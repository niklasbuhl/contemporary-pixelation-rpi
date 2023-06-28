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

start = time.time()

from PIL import Image

# Create a new empty image with a white background
width = 32
height = 32
color = (255, 255, 255)  # RGB color value for white
image = Image.new("RGB", (width, height))

for y in range(height):
    for x in range(width):
		
		color = (randint(0, 255), randint(0, 255), randint(0, 255))  # RGB color value for white

		image.putpixel((x, y), color)


# Then scroll image across matrix...
for n in range(-32, 33):  # Start off top-left, move off bottom-right
    matrix.Clear()
    matrix.SetImage(image, n, n)
    time.sleep(0.05)

end = time.time()

print(f"run: ${end - start}")

while True:
	time.sleep(0.05)