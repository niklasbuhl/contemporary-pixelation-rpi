import uvicorn
from app.app import app
from decouple import config

HOST = config("HOST")
PORT = config("PORT")
RELOAD = config("RELOAD")
LOG_LEVEL = config("LOG_LEVEL")

if __name__ == '__main__':
	uvicorn.run("app", host=HOST, port=int(PORT), log_level=LOG_LEVEL, reload=RELOAD)