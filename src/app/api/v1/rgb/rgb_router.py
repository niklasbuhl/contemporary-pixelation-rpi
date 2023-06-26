from fastapi import APIRouter, Request
from acrylic import Color

from ....controllers.rgb_controller import rgb

router = APIRouter(
    prefix="/rgb"
)

# RGB API
@router.get("/")
def rgb_root():
    return {"api/v1/rgb"}

# Set Pixel
@router.post("/pixel")
async def rgb_set_pixel(request: Request):
	data = await request.json()

	x = data['x']
	y = data['x']
	r = data['red']
	g = data['green']
	b = data['blue']

	c = Color(rgb=[r,g,b])

	rgb.set_pixel(x, y, c)

# Set Frame
@router.post("/frame")
def rgb_set_frame():
	rgb.set_frame()


# Sync Frame
@router.post("/sync")
def rgb_sync():
	rgb.sync()

# Start
@router.post("/animation/start")
def rgb_animation_start():
	rgb.start_animation()

# Stop (command)
@router.post("/animation/stop")
def rgb_animation_stop():
	rgb.stop_animation()

# Status
@router.get("/animation")
def rgb_get_animation():
	result = rgb.animation_status()
	return {"result": result}

# Command
@router.post("/animation/command")
async def rgb_command_animation(request: Request):
	data = await request.json()
	# print(data['command'])
	rgb.command_animation(data["command"])