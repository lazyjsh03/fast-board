from fastapi import APIRouter
from app.api.v1.endpoints import router as items_router
from app.api.v1.auth import router as auth_router
from app.api.v1.posts import router as posts_router

api_router = APIRouter()
api_router.include_router(items_router, prefix="/items", tags=["items"])
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(posts_router, prefix="/posts", tags=["posts"])
