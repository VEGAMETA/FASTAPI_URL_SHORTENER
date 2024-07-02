from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend import database
from backend.middlewares import *
from fastapi.staticfiles import StaticFiles


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


api_v1_app = FastAPI(root_path="/api/v1")

app = FastAPI(lifespan=lifespan, title="URL Shortener API", version="0.1.0")
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
app.mount("/api/v1", api_v1_app)
