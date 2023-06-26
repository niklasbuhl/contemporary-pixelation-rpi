from fastapi import APIRouter, Request
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
def rgb_set_pixel():
	rgb.set_pixel()

# Set Frame
@router.post("/frame")
def rgb_set_frame():
	rgb.set_frame()

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