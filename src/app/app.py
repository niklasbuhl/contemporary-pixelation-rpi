import sys
from fastapi import FastAPI
from contextlib import asynccontextmanager

from .middleware.auth_middleware import AuthMiddleware
from .api import api_router
# from .integrations.pusher_integration import pusher

# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    # pusher.connect()
    yield
    # Clean up the ML models and release the resources
    # pusher.disconnect()

# App
app = FastAPI(lifespan=lifespan)
app.add_middleware(AuthMiddleware)  # Add the middleware to the FastAPI application

# Routes
@app.get("/")
def root():
    return {"Hello": "World 🪐"}

# API
app.include_router(api_router.router) 

# Run
# uvicorn main:app --reload