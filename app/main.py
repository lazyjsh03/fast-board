from fastapi import FastAPI
from app.api.v1 import api_router
from contextlib import asynccontextmanager
from app.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Board API", version="0.1.0", lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}
