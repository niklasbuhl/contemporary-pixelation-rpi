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
matrix.SwapOnVSync(frame_canvas)

while True:

	start = time.time()

	for x in range(32):
		for y in range(32):
			frame_canvas.SetPixel(x,y,255, 0, 255)
			# frame_canvas.SetPixel(x,y,random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

	end = time.time()

	print(f"run: ${end - start}")

	time.sleep(0.05)