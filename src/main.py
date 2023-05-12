import pusher
import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

CHANNEL = os.environ.get("CHANNEL")

pusher_client = pusher.Pusher(
    app_id=os.environ.get("APP_ID"),
    key=os.environ.get("KEY"),
    secret=os.environ.get("SECRET"),
    cluster=os.environ.get("CLUSTER"),
    ssl=True
)

@app.get("/")
async def read_root():
    pusher.trigger(CHANNEL, 'my-event', {'message': 'Hello, world!'})
    return {"message": "Hello, World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
