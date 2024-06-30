from sqlalchemy import select

from api import app, database
from api.models import *
from api.models.pydantic import *


async def get_db_short_url(short_url: str) -> URL | None:
    query = select(URL).where(URL.short_url == short_url)
    db_url = await database.fetch_one(query)
    return db_url
