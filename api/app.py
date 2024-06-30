from contextlib import asynccontextmanager
from fastapi import FastAPI
from api import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan, title="URL Shortener API", version="0.1.0")
