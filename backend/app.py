from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from backend import database
from fastapi.staticfiles import StaticFiles


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


api_v1_router = APIRouter(prefix="/api/v1")

app = FastAPI(lifespan=lifespan, title="URL Shortener API", version="1.0.0")
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
