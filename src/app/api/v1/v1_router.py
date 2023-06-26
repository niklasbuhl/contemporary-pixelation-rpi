from fastapi import APIRouter
from .rgb import rgb_router
# from ...main import rgb

router = APIRouter(
    prefix="/v1"
)

@router.get("/")
def read_v1():
    return {"api/v1"}

router.include_router(rgb_router.router)