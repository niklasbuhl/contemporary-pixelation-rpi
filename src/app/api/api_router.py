from fastapi import APIRouter
from fastapi import Depends
from .v1 import v1_router

router = APIRouter(
    prefix="/api"
)

@router.get("/")
def read_api():
    return {"api"}

router.include_router(v1_router.router)