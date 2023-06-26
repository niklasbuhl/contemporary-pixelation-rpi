import uvicorn
from app.app import app
from decouple import config
# import multiprocessing as mp
# PLATFORM = config("PLATFORM")

# if (PLATFORM == "mac"):
# 	from p5 import *

# def setup():
# 	size(1024, 1024)
# 	color_mode(HSB)

# def draw():
# 	background(0, 0, 255)

if __name__ == '__main__':
	# if (PLATFORM == "mac"):
	# 	p5process = mp.Process(target=run)
	# 	p5process.start()

	uvicorn.run("main:app", host='0.0.0.0', port=8080, log_level='info', reload=True)