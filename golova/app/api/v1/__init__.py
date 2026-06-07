from fastapi import APIRouter
from .face_detection import router
v1_router = APIRouter(prefix="/v1")

v1_router.include_router(router)